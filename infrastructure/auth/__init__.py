import grpc

from proto.python.auth import auth_student_pb2, auth_student_pb2_grpc


class AuthService:
    def __init__(self):
        self.address = "192.168.123.24:10059"
        self.channel = grpc.insecure_channel(self.address)
        self.stub = auth_student_pb2_grpc.AuthStudentStub(self.channel)
        self.metadata = (("x-request-id", "f9ed4675f1c53513c61a3b3b4e25b4c0"),
                    ("span-context", "a:a:0:0"))

    def get_student_inform(self, uuid, student_uuid):
        return self.stub.GetStudentInformWithUUID(auth_student_pb2.GetStudentInformWithUUIDRequest(
            UUID=uuid,
            StudentUUID=student_uuid
        ), metadata=self.metadata)