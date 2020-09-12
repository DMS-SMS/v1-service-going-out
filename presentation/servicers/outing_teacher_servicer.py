from proto.python.outing import outing_teacher_pb2_grpc

from application.service.teacher_outing_service import TeacherOutingService


class TeacherOutingServicer(outing_teacher_pb2_grpc.OutingTeacherServicer):
    def GetOutingWithFilter(self, request, context):
        pass

    def GetOutingStudentWithSN(self, request, context):
        pass

    def GetOutingStudentWithFloor(self, request, context):
        pass

    def ApproveOuting(self, request, context):
        return TeacherOutingService().approve_outing(request)

    def RejectOuting(self, request, context):
        pass

    def CertifyOuting(self, request, context):
        pass
