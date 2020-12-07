import grpc

from infrastructure.consul.consul_handler import ConsulHandler
from infrastructure.open_tracing.open_tracing_handler import trace_service
from infrastructure.open_tracing import open_tracing

from proto.python.club import club_student_pb2, club_student_pb2_grpc

from const.topic.python.service_names import club_service_name


class ClubHandler:
    def __init__(self):
        self._consul = ConsulHandler()
        self._address = self._consul.get_address(club_service_name)
        self._channel = grpc.insecure_channel(self._address)
        self._student_stub = club_student_pb2_grpc.ClubStudentStub(self._channel)

    @trace_service("Club Handler (get_club_informs_with_floor)", open_tracing)
    def get_club_informs_with_floor(self, uuid, floor, x_request_id):
        self.metadata = (("x-request-id", x_request_id),
                         ("span-context", str(open_tracing.tracer.active_span).split()[0]))

        club_response = self._student_stub.GetClubUUIDsWithFloor(club_student_pb2.GetClubUUIDsWithFloorRequest(
            UUID=uuid,
            floor=str(floor)
        ), metadata=self.metadata)

        response = self._student_stub.GetClubInformsWithUUIDs(club_student_pb2.GetClubInformsWithUUIDsRequest(
            UUID=uuid,
            ClubUUIDs=club_response.ClubUUIDs
        ), metadata=self.metadata)

        if response.Status != 200: return None

        return response