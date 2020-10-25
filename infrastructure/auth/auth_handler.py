import grpc

from infrastructure.consul.consul_handler import ConsulHandler
from infrastructure.open_tracing.open_tracing_handler import trace_service
from infrastructure.open_tracing import open_tracing

from proto.python.auth import auth_student_pb2, auth_student_pb2_grpc
from proto.python.auth import auth_teacher_pb2, auth_teacher_pb2_grpc
from const.topic.python.service_names import auth_service_name


class AuthHandler:
    def __init__(self):
        self._consul = ConsulHandler()
        self._address = "127.0.0.1:10027"
        # self._address = self._consul.get_address(auth_service_name)
        self._channel = grpc.insecure_channel(self._address)
        self._student_stub = auth_student_pb2_grpc.AuthStudentStub(self._channel)
        self._teacher_stub = auth_teacher_pb2_grpc.AuthTeacherStub(self._channel)


    @trace_service("Auth Handler (get_student_inform)", open_tracing)
    def get_student_inform(self, uuid, student_uuid, x_request_id):
        self.metadata = (("x-request-id", x_request_id),
         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = self._student_stub.GetStudentInformWithUUID(auth_student_pb2.GetStudentInformWithUUIDRequest(
            UUID=uuid,
            StudentUUID=student_uuid
        ), metadata=self.metadata)

        if response.Status != 200: return None

        return response

    @trace_service("Auth Handler (get_uuid_with_inform)", open_tracing)
    def get_uuid_with_inform(self, uuid, x_request_id, grade=None, group=None):
        self.metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = self._student_stub.GetStudentUUIDsWithInform(auth_student_pb2.GetStudentUUIDsWithInformRequest(
            UUID=uuid,
            Grade=grade,
            Group=group
        ), metadata=self.metadata)

        if response.Status != 200: return None

        return response.StudentUUIDs

    @trace_service("Auth Handler (get_teacher_inform)", open_tracing)
    def get_teacher_inform(self, uuid, teacher_uuid, x_request_id):
        self.metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = self._teacher_stub.GetTeacherInformWithUUID(auth_teacher_pb2.GetTeacherInformWithUUIDRequest(
            UUID=uuid,
            TeacherUUID=teacher_uuid
        ), metadata=self.metadata)

        if response.Status != 200: return None

        return response

