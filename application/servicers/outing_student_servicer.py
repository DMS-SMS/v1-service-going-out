from application.decorator.metadata import jagger_enable
from application.decorator.error_handling import error_handling
from infrastructure.implementation.repository.confirm_code_repository_impl import ConfirmCodeRepositoryImpl
from infrastructure.implementation.repository.parents_repository_impl import ParentsRepositoryImpl
from infrastructure.implementation.repository.teacher_repository_impl import TeacherRepositoryImpl
from infrastructure.pick.pick_service_impl import PickServiceImpl
from service.mapper.student_outing_mapper import StudentOutingMapper

from service.student_outing_service import StudentOutingService

from domain.usecase.create_outing_usecase import CreateOutingUseCase
from domain.usecase.finish_go_out_usecase import FinishGoOutUseCase
from domain.usecase.get_card_usecase import GetCardUseCase
from domain.usecase.get_my_outings_usecase import GetMyOutingsUseCase
from domain.usecase.get_outing_inform_usecase import GetOutingInformUseCase
from domain.usecase.go_out_usecase import GoOutUseCase

from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl
from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from infrastructure.implementation.service.uuid_service_impl import UuidServiceImpl
from infrastructure.sms.sms_service_impl import SMSServiceImpl

from proto.python.outing import outing_student_pb2_grpc, outing_student_pb2


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.confirm_code_repository = ConfirmCodeRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()
        self.teacher_repository = TeacherRepositoryImpl()
        self.parents_repository = ParentsRepositoryImpl()
        self.uuid_service = UuidServiceImpl()
        self.sms_service = SMSServiceImpl()
        self.pick_service = PickServiceImpl()

        self.service = StudentOutingService(
            create_outing_usecase=CreateOutingUseCase(
                outing_repository=self.outing_repository,
                confirm_code_repository=self.confirm_code_repository,
                student_repository=self.student_repository,
                teacher_repository=self.teacher_repository,
                parents_repository=self.parents_repository,
                uuid_service=self.uuid_service,
                sms_service=self.sms_service
            ),
            get_my_outings_usecase=GetMyOutingsUseCase(
                outing_repository=self.outing_repository,
                student_repository=self.student_repository
            ),
            get_outing_inform_usecase=GetOutingInformUseCase(
                outing_repository=self.outing_repository,
                student_repository=self.student_repository,
                parents_repository=self.parents_repository,
                uuid_service=self.uuid_service
            ),
            get_card_usecase=GetCardUseCase(
                outing_repository=self.outing_repository,
                student_repository=self.student_repository,
                uuid_service=self.uuid_service
            ),
            go_out_usecase=GoOutUseCase(
                outing_repository=self.outing_repository,
                student_repository=self.student_repository,
                parents_repository=self.parents_repository,
                sms_service=self.sms_service,
                pick_service=self.pick_service
            ),
            finish_go_out_usecase=FinishGoOutUseCase(
                outing_repository=self.outing_repository,
                student_repository=self.student_repository,
                teacher_repository=self.teacher_repository
            ),
            student_outing_mapper=StudentOutingMapper()
        )

    @error_handling(outing_student_pb2.CreateOutingResponse)
    @jagger_enable
    def CreateOuting(self, request, context):
        return self.service.create_outing(request, context)

    @error_handling(outing_student_pb2.GetCardAboutOutingResponse)
    @jagger_enable
    def GetCardAboutOuting(self, request, context):
        return self.service.get_card_about_outing(request, context)

    @error_handling(outing_student_pb2.GetOutingInformResponse)
    @jagger_enable
    def GetOutingInform(self, request, context):
        return self.service.get_outing_inform(request, context)

    @error_handling(outing_student_pb2.GetStudentOutingsResponse)
    @jagger_enable
    def GetStudentOutings(self, request, context):
        return self.service.get_student_outings(request, context)

    @error_handling(outing_student_pb2.GoOutResponse)
    @jagger_enable
    def StartGoOut(self, request, context):
        return self.service.go_out(request, context)

    @error_handling(outing_student_pb2.GoOutResponse)
    @jagger_enable
    def FinishGoOut(self, request, context):
        return self.service.finish_go_out(request, context)
