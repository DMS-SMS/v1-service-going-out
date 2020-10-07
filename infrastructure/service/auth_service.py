import grpc

from infrastructure.extension import consul, open_tracing
from proto.python.auth import auth_student_pb2, auth_student_pb2_grpc


class AuthService:
    def __init__(self):
        # TODO
        self.address = "127.0.0.1:10071"
        # self.address = consul.get_address("DMS.SMS.v1.service.auth")
        self.channel = grpc.insecure_channel(self.address)
        self.stub = auth_student_pb2_grpc.AuthStudentStub(self.channel)
        self.metadata: str

    def get_student_inform(self, uuid, student_uuid):
        self.metadata = (("x-request-id", "f9ed4675f1c53513c61a3b3b4e25b4c0"),
         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        return self.stub.GetStudentInformWithUUID(auth_student_pb2.GetStudentInformWithUUIDRequest(
            UUID=uuid,
            StudentUUID=student_uuid
        ), metadata=self.metadata)