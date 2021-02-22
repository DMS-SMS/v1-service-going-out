import grpc

from infrastructure.consul.consul_handler import ConsulHandler
from infrastructure.open_tracing.open_tracing_handler import trace_service
from infrastructure.open_tracing import open_tracing

from proto.python.auth import auth_student_pb2, auth_student_pb2_grpc
from proto.python.auth import auth_teacher_pb2, auth_teacher_pb2_grpc
from proto.python.auth import auth_parent_pb2, auth_parent_pb2_grpc
from const.topic.python.service_names import auth_service_name


class AuthHandler:
    @trace_service("Auth Handler (get_student_inform)", open_tracing)
    def get_student_inform(self, uuid, student_uuid, x_request_id):
        address = ConsulHandler().auth_address
        channel = grpc.insecure_channel(address)
        student_stub = auth_student_pb2_grpc.AuthStudentStub(channel)

        metadata = (("x-request-id", x_request_id),
         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = student_stub.GetStudentInformWithUUID(auth_student_pb2.GetStudentInformWithUUIDRequest(
            UUID=uuid,
            StudentUUID=student_uuid
        ), metadata=metadata)

        if response.Status != 200: return None

        return response

    @trace_service("Auth Handler (get_uuid_with_inform)", open_tracing)
    def get_uuid_with_inform(self, uuid, x_request_id, grade=None, group=None):
        address = ConsulHandler().auth_address
        channel = grpc.insecure_channel(address)
        student_stub = auth_student_pb2_grpc.AuthStudentStub(channel)

        metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = student_stub.GetStudentUUIDsWithInform(auth_student_pb2.GetStudentUUIDsWithInformRequest(
            UUID=uuid,
            Grade=grade,
            Group=group
        ), metadata=metadata)

        if response.Status != 200: return None

        return response.StudentUUIDs

    @trace_service("Auth Handler (get_teacher_inform)", open_tracing)
    def get_teacher_inform(self, uuid, teacher_uuid, x_request_id):
        address = ConsulHandler().auth_address
        channel = grpc.insecure_channel(address)
        teacher_stub = auth_teacher_pb2_grpc.AuthTeacherStub(channel)

        metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = teacher_stub.GetTeacherInformWithUUID(auth_teacher_pb2.GetTeacherInformWithUUIDRequest(
            UUID=uuid,
            TeacherUUID=teacher_uuid
        ), metadata=metadata)

        if response.Status != 200: return None

        return response

    @trace_service("Auth Handler (get_teacher_uuids_with_inform)", open_tracing)
    def get_teacher_uuids_with_inform(self, uuid, grade, group, x_request_id):
        address = ConsulHandler().auth_address
        channel = grpc.insecure_channel(address)
        teacher_stub = auth_teacher_pb2_grpc.AuthTeacherStub(channel)

        metadata = (("x-request-id", x_request_id),
                    ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = teacher_stub.GetTeacherUUIDsWithInform(auth_teacher_pb2.GetTeacherUUIDsWithInformRequest(
            UUID=uuid,
            Grade=grade,
            Group=group
        ), metadata=metadata)

        if response.Status != 200: return []

        return response.TeacherUUIDs

    @trace_service("Auth Handler (get_parents_with_student_uuid)", open_tracing)
    def get_parents_with_student_uuid(self, uuid, student_uuid, x_request_id):
        address = ConsulHandler().auth_address
        channel = grpc.insecure_channel(address)
        student_stub = auth_student_pb2_grpc.AuthStudentStub(channel)

        metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = student_stub.GetParentWithStudentUUID(auth_student_pb2.GetParentWithStudentUUIDRequest(
            UUID=uuid,
            StudentUUID=student_uuid
        ), metadata=metadata)

        if response.Status != 200: return None

        return response

    @trace_service("Auth Handler (get_parents_inform)", open_tracing)
    def get_parents_inform(self, uuid, parents_uuid, x_request_id):
        address = ConsulHandler().auth_address
        channel = grpc.insecure_channel(address)
        parents_stub = auth_parent_pb2_grpc.AuthParentStub(channel)

        metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        response = parents_stub.GetParentInformWithUUID(auth_parent_pb2.GetParentInformWithUUIDRequest(
            UUID=uuid,
            ParentUUID=parents_uuid,
        ), metadata=metadata)

        if response.Status != 200: return None

        return response