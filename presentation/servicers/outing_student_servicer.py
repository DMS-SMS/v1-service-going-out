from application.service.student_outing_service import StudentOutingService

from infrastructure.repository import OutingRepositoryImpl, StudentRepositoryImpl
from infrastructure.service.outing_domain_service_impl import OutingDomainServiceImpl
from infrastructure.util.sms_service import SMSService

from proto.python.outing import outing_student_pb2_grpc


class StudentOutingServicer(outing_student_pb2_grpc.OutingStudentServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()

        self.outing_domain_service = OutingDomainServiceImpl()

        self.sms_service = SMSService()

        self.service = StudentOutingService(
            outing_repository=self.outing_repository,
            student_repository=self.student_repository,
            outing_domain_service=self.outing_domain_service,
            sms_service=self.sms_service,
        )

    def CreateOuting(self, request, context):
        return self.service.create_outing(request)

    def GetCardAboutOuting(self, request, context):
        return self.service.get_card_about_outing(request)

    def GetOutingInform(self, request, context):
        return self.service.get_outing_inform(request)

    def GetStudentOutings(self, request, context):
        return self.service.get_student_outings(request)

    def GoOut(self, request, context):
        return self.service.go_out(request)

    def FinishGoOut(self, request, context):
        return self.service.finish_go_out(request)
