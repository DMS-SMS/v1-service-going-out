from application.service.parents_outing_service import ParentsOutingService
from proto.python.outing import outing_parents_pb2_grpc


class ParentsOutingServicer(outing_parents_pb2_grpc.OutingParentsServicer):
    def ApproveOutingByOCode(self, request, context):
        return ParentsOutingService().approve_outing(request)

    def RejectOutingByOCode(self, request, context):
        return ParentsOutingService().reject_outing(request)