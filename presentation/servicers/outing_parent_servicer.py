from application.service.parents_outing_service import ParentsOutingService
from proto.python.outing import outing_parent_pb2_grpc


class ParentOutingServicer(outing_parent_pb2_grpc.OutingParentServicer):
    def ApproveOutingByOCode(self, request, context):
        return ParentsOutingService().approve_outing(request)