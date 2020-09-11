from application.service.outing_service import OutingService

from proto.python.outing import outing_student_pb2_grpc


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def CreateOuting(self, request, context):
        return OutingService().create_outing(request)

    def GetCardAboutOuting(self, request, context):
        return OutingService().get_card_about_outing(request)

    def GetOutingInform(self, request, context):
        return OutingService().get_outing_inform(request)

    def GetStudentOutings(self, request, context):
        return OutingService().get_student_outings(request)