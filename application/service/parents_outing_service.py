from proto.python.outing import outing_parents_pb2 as proto

from application.decorator.error_handling import error_handling

from domain.repository.outing_repository import OutingRepository

from infrastructure.repository.outing_repository_impl import OutingRepositoryImpl


class ParentsOutingService:
    @classmethod
    @error_handling(proto.ConfirmOutingByOCodeResponse)
    def approve_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.approve_by_outing_for_parents(request.o_code)

        return proto.ConfirmOutingByOCodeResponse(status=200)

    @classmethod
    @error_handling(proto.ConfirmOutingByOCodeResponse)
    def reject_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.reject_by_outing_for_parents(request.o_code)

        return proto.ConfirmOutingByOCodeResponse(status=200)
