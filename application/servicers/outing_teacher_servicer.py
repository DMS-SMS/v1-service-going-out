from proto.python.outing import outing_teacher_pb2_grpc

from application.service.teacher_outing_service import TeacherOutingService

from infrastructure.repository import OutingRepositoryImpl
from infrastructure.service.outing_domain_service_impl import OutingDomainServiceImpl


class TeacherOutingServicer(outing_teacher_pb2_grpc.OutingTeacherServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.outing_domain_service = OutingDomainServiceImpl()

        self.service = TeacherOutingService(
            outing_repository=self.outing_repository,
            outing_domain_service=self.outing_domain_service,
        )

    def GetOutingWithFilter(self, request, context):
        return self.service.get_outings_with_filter(request)

    def ApproveOuting(self, request, context):
        return self.service.approve_outing(request)

    def RejectOuting(self, request, context):
        return self.service.reject_outing(request)

    def CertifyOuting(self, request, context):
        return self.service.certify_outing(request)
