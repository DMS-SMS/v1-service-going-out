import grpc

from infrastructure.consul.consul_handler import ConsulHandler
from infrastructure.open_tracing import open_tracing

from proto.python.auth import auth_student_pb2, auth_student_pb2_grpc


class AuthHandler:
    def __init__(self):
        self._consul = ConsulHandler()
        self._address = "127.0.0.1:10071"
        # self.address = self.consul.get_address("DMS.SMS.v1.service.auth")
        self._channel = grpc.insecure_channel(self._address)
        self._stub = auth_student_pb2_grpc.AuthStudentStub(self._channel)

    def get_student_inform(self, uuid, student_uuid):
        self.metadata = (("x-request-id", "f9ed4675f1c53513c61a3b3b4e25b4c0"),
         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        return self._stub.GetStudentInformWithUUID(auth_student_pb2.GetStudentInformWithUUIDRequest(
            UUID=uuid,
            StudentUUID=student_uuid
        ), metadata=self.metadata)