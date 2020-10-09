from application.service.parents_outing_service import ParentsOutingService
from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl

from proto.python.outing import outing_parents_pb2_grpc
from application.decorator.metadata import jagger_enable


class ParentsOutingServicer(outing_parents_pb2_grpc.OutingParentsServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.service = ParentsOutingService(
            approve_outing_usecase=ApproveOutingUseCase(
                self.outing_repository
            ),
            reject_outing_usecase=RejectOutingUseCase(
                self.outing_repository
            )
        )

    @jagger_enable
    def ApproveOutingByOCode(self, request, context):
        return self.service.approve_outing(request)

    @jagger_enable
    def RejectOutingByOCode(self, request, context):
        return self.service.reject_outing(request)
