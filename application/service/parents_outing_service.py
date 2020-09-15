from proto.python.outing import outing_parents_pb2 as proto

from application.decorator.error_handling import error_handling

from domain.repository.outing_repository import OutingRepository


class ParentsOutingService:
    def __init__(self, outing_repository):
        self.outing_repository: OutingRepository = outing_repository

    @error_handling(proto.ConfirmOutingByOCodeResponse)
    def approve_outing(self, request):
        self.outing_repository.approve_by_outing_for_parents(request.o_code)

        return proto.ConfirmOutingByOCodeResponse(status=200)

    @error_handling(proto.ConfirmOutingByOCodeResponse)
    def reject_outing(self, request):
        self.outing_repository.reject_by_outing_for_parents(request.o_code)

        return proto.ConfirmOutingByOCodeResponse(status=200)
