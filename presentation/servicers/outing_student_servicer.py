from application.service.student_outing_service import StudentOutingService
from proto.python.outing import outing_student_pb2_grpc


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def CreateOuting(self, request, context):
        return StudentOutingService().create_outing(request)

    def GetCardAboutOuting(self, request, context):
        return StudentOutingService().get_card_about_outing(request)

    def GetOutingInform(self, request, context):
        return StudentOutingService().get_outing_inform(request)

    def GetStudentOutings(self, request, context):
        return StudentOutingService().get_student_outings(request)

    def GoOut(self, request, context):
        return StudentOutingService().go_out(request)

    def FinishGoOut(self, request, context):
        return StudentOutingService().finish_go_out(request)