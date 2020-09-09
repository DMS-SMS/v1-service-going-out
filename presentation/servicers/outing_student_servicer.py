from proto.python.outing import outing_student_pb2_grpc


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def CreateOuting(self, request, context):
        pass

    def GetCardAboutOuting(self, request, context):
        pass

    def GetOutingInform(self, request, context):
        pass

    def GetStudentOutings(self, request, context):
        pass