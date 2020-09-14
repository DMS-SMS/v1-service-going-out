from proto.python.outing import outing_teacher_pb2_grpc

from application.service.teacher_outing_service import TeacherOutingService


class TeacherOutingServicer(outing_teacher_pb2_grpc.OutingTeacherServicer):
    def GetOutingWithFilter(self, request, context):
        return TeacherOutingService().get_outings_with_filter(request)

    def ApproveOuting(self, request, context):
        return TeacherOutingService().approve_outing(request)

    def RejectOuting(self, request, context):
        return TeacherOutingService().reject_outing(request)

    def CertifyOuting(self, request, context):
        return TeacherOutingService().certify_outing(request)
