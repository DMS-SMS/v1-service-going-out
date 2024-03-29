from domain.usecase.get_account_by_uuid_usecase import GetAccountByUuidUseCase
from domain.usecase.get_outing_by_o_code_usecase import GetOutingByOCodeUseCase
from infrastructure.implementation.repository.confirm_code_repository_impl import ConfirmCodeRepositoryImpl
from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from infrastructure.implementation.repository.teacher_repository_impl import TeacherRepositoryImpl
from infrastructure.sms.sms_service_impl import SMSServiceImpl
from service.parents_outing_service import ParentsOutingService
from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl

from proto.python.outing import outing_parents_pb2_grpc, outing_parents_pb2
from application.decorator.metadata import jaeger_enable
from application.decorator.error_handling import error_handling


class ParentsOutingServicer(outing_parents_pb2_grpc.OutingParentsServicer):
    def __init__(self):
        self.confirm_code_repository = ConfirmCodeRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()
        self.teacher_repository = TeacherRepositoryImpl()
        self.outing_repository = OutingRepositoryImpl()
        self.sms_service = SMSServiceImpl()

        self.service = ParentsOutingService(
            approve_outing_usecase=ApproveOutingUseCase(
                outing_repository=self.outing_repository,
                confirm_code_repository=self.confirm_code_repository,
                student_repository=self.student_repository,
                teacher_repository=self.teacher_repository,
                sms_service=self.sms_service
            ),
            reject_outing_usecase=RejectOutingUseCase(
                outing_repository=self.outing_repository,
                confirm_code_repository=self.confirm_code_repository,
                student_repository=self.student_repository,
                sms_service=self.sms_service
            ),
            get_account_by_uuid_usecase=GetAccountByUuidUseCase(
                student_repository=self.student_repository
            ),
            get_outing_by_o_code_usecase=GetOutingByOCodeUseCase(
                outing_repository=self.outing_repository,
                confirm_code_repository=self.confirm_code_repository
            )
        )

    @error_handling(outing_parents_pb2.ConfirmOutingByOCodeResponse)
    @jaeger_enable
    def ApproveOutingByOCode(self, request, context):
        return self.service.approve_outing(request, context)

    @error_handling(outing_parents_pb2.ConfirmOutingByOCodeResponse)
    @jaeger_enable
    def RejectOutingByOCode(self, request, context):
        return self.service.reject_outing(request, context)

    @error_handling(outing_parents_pb2.GetOutingByOCodeResponse)
    @jaeger_enable
    def GetOutingByOCode(self, request, context):
        return self.service.get_outing(request, context)