from application.service.student_outing_service import StudentOutingService
from domain.usecase.create_outing_usecase import CreateOutingUseCase
from domain.usecase.finish_go_out_usecase import FinishGoOutUseCase
from domain.usecase.get_card_usecase import GetCardUseCase
from domain.usecase.get_my_outings_usecase import GetMyOutingsUseCase
from domain.usecase.get_outing_inform_usecase import GetOutingInformUseCase
from domain.usecase.go_out_usecase import GoOutUseCase

from infrastructure.repository import OutingRepositoryImpl, StudentRepositoryImpl
from infrastructure.service.outing_domain_service_impl import OutingDomainServiceImpl
from infrastructure.service.sms_service_impl import SMSServiceImpl

from proto.python.outing import outing_student_pb2_grpc


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()
        self.outing_domain_service = OutingDomainServiceImpl()
        self.sms_service = SMSServiceImpl()

        self.service = StudentOutingService(
            create_outing_usecase=CreateOutingUseCase(
                self.outing_repository,
                self.student_repository,
                self.sms_service,
            ),
            get_my_outings_usecase=GetMyOutingsUseCase(
                self.outing_repository,
                self.outing_domain_service
            ),
            get_outing_inform_usecase=GetOutingInformUseCase(
                self.outing_repository,
                self.outing_domain_service
            ),
            get_card_usecase=GetCardUseCase(
                self.outing_repository,
                self.student_repository,
                self.outing_domain_service
            ),
            go_out_usecase=GoOutUseCase(
                self.outing_repository
            ),
            finish_go_out_usecase=FinishGoOutUseCase(
                self.outing_repository
            )
        )

    def CreateOuting(self, request, context):
        return self.service.create_outing(request)

    def GetCardAboutOuting(self, request, context):
        return self.service.get_card_about_outing(request)

    def GetOutingInform(self, request, context):
        return self.service.get_outing_inform(request)

    def GetStudentOutings(self, request, context):
        return self.service.get_student_outings(request)

    def GoOut(self, request, context):
        return self.service.go_out(request)

    def FinishGoOut(self, request, context):
        return self.service.finish_go_out(request)
