from proto.python.outing import outing_parent_pb2 as proto

from application.decorator.error_handling import error_handling

from domain.repository.outing_repository import OutingRepository

from infrastructure.repository.outing_repository_impl import OutingRepositoryImpl


class ParentsOutingService:
    @classmethod
    @error_handling(proto.ApproveOutingByOCodeResponse)
    def approve_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.approve_by_outing_for_parent(request.o_code)

        return proto.ApproveOutingByOCodeResponse(status=200)