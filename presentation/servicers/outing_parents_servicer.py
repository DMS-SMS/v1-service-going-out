from infrastructure.repository import OutingRepositoryImpl, StudentRepositoryImpl
from application.service.parents_outing_service import ParentsOutingService

from proto.python.outing import outing_parents_pb2_grpc


class ParentsOutingServicer(outing_parents_pb2_grpc.OutingParentsServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.service = ParentsOutingService(outing_repository=self.outing_repository)

    def ApproveOutingByOCode(self, request, context):
        return self.service.approve_outing(request)

    def RejectOutingByOCode(self, request, context):
        return self.service.reject_outing(request)
