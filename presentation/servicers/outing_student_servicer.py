from application.service.outing_service import OutingService

from proto.python.outing import outing_student_pb2_grpc, outing_student_pb2


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def CreateOuting(self, request, context):
        return OutingService().create_outing(request)

    def GetCardAboutOuting(self, request, context):
        pass

    def GetOutingInform(self, request, context):
        pass

    def GetStudentOutings(self, request, context):
        return OutingService().get_student_outings(request)