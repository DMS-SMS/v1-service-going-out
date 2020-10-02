from application.service.parents_outing_service import ParentsOutingService
from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from infrastructure.repository import OutingRepositoryImpl

from proto.python.outing import outing_parents_pb2_grpc


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

    def ApproveOutingByOCode(self, request, context):
        return self.service.approve_outing(request)

    def RejectOutingByOCode(self, request, context):
        return self.service.reject_outing(request)
