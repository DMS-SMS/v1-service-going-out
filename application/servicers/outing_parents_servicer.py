from domain.usecase.get_account_by_uuid_usecase import GetAccountByUuidUseCase
from domain.usecase.get_outing_by_o_code_usecase import GetOutingByOCodeUseCase
from infrastructure.implementation.repository.confirm_code_repository_impl import ConfirmCodeRepositoryImpl
from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from service.parents_outing_service import ParentsOutingService
from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl

from proto.python.outing import outing_parents_pb2_grpc, outing_parents_pb2
from application.decorator.metadata import jagger_enable
from application.decorator.error_handling import error_handling


class ParentsOutingServicer(outing_parents_pb2_grpc.OutingParentsServicer):
    def __init__(self):
        self.confirm_code_repository = ConfirmCodeRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()
        self.outing_repository = OutingRepositoryImpl()
        self.service = ParentsOutingService(
            approve_outing_usecase=ApproveOutingUseCase(
                self.outing_repository,
                self.confirm_code_repository
            ),
            reject_outing_usecase=RejectOutingUseCase(
                self.outing_repository,
                self.confirm_code_repository
            ),
            get_account_by_uuid_usecase=GetAccountByUuidUseCase(
                self.student_repository
            ),
            get_outing_by_o_code_usecase=GetOutingByOCodeUseCase(
                self.outing_repository,
                self.confirm_code_repository
            )
        )

    @error_handling(outing_parents_pb2.ConfirmOutingByOCodeResponse)
    @jagger_enable
    def ApproveOutingByOCode(self, request, context):
        return self.service.approve_outing(request, context)

    @error_handling(outing_parents_pb2.ConfirmOutingByOCodeResponse)
    @jagger_enable
    def RejectOutingByOCode(self, request, context):
        return self.service.reject_outing(request, context)

    @error_handling(outing_parents_pb2.GetOutingByOCodeResponse)
    @jagger_enable
    def GetOutingByOCode(self, request, context):
        return self.service.get_outing(request, context)