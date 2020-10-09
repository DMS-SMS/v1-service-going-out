from application.service.student_outing_service import StudentOutingService
from application.decorator.metadata import jagger_enable

from domain.usecase.create_outing_usecase import CreateOutingUseCase
from domain.usecase.finish_go_out_usecase import FinishGoOutUseCase
from domain.usecase.get_card_usecase import GetCardUseCase
from domain.usecase.get_my_outings_usecase import GetMyOutingsUseCase
from domain.usecase.get_outing_inform_usecase import GetOutingInformUseCase
from domain.usecase.go_out_usecase import GoOutUseCase

from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl
from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from infrastructure.implementation.service.paging_service_impl import pagingServiceImpl
from infrastructure.implementation.service.uuid_service_impl import uuidServiceImpl
from infrastructure.implementation.service.sms_service_impl import SMSServiceImpl

from proto.python.outing import outing_student_pb2_grpc


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()
        self.paging_service = pagingServiceImpl()
        self.uuid_service = uuidServiceImpl()
        self.sms_service = SMSServiceImpl()

        self.service = StudentOutingService(
            create_outing_usecase=CreateOutingUseCase(
                self.outing_repository,
                self.student_repository,
                self.sms_service,
            ),
            get_my_outings_usecase=GetMyOutingsUseCase(
                self.outing_repository,
                self.paging_service,
                self.uuid_service
            ),
            get_outing_inform_usecase=GetOutingInformUseCase(
                self.outing_repository,
                self.uuid_service
            ),
            get_card_usecase=GetCardUseCase(
                self.outing_repository,
                self.student_repository,
                self.uuid_service
            ),
            go_out_usecase=GoOutUseCase(
                self.outing_repository
            ),
            finish_go_out_usecase=FinishGoOutUseCase(
                self.outing_repository
            )
        )

    @jagger_enable
    def CreateOuting(self, request, context):
        return self.service.create_outing(request)

    @jagger_enable
    def GetCardAboutOuting(self, request, context):
        return self.service.get_card_about_outing(request)

    @jagger_enable
    def GetOutingInform(self, request, context):
        return self.service.get_outing_inform(request)

    @jagger_enable
    def GetStudentOutings(self, request, context):
        return self.service.get_student_outings(request)

    @jagger_enable
    def GoOut(self, request, context):
        return self.service.go_out(request)

    @jagger_enable
    def FinishGoOut(self, request, context):
        return self.service.finish_go_out(request)
