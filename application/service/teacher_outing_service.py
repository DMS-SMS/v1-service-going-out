from proto.python.outing import outing_teacher_pb2 as proto

from application.decorator.error_handling import error_handling

from domain.repository.outing_repository import OutingRepository

from infrastructure.repository.outing_repository_impl import OutingRepositoryImpl


class TeacherOutingService:
    @classmethod
    @error_handling(proto.ConfirmOutingResponse)
    def approve_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.approve_by_outing_for_teacher(request.oid)

        return proto.ConfirmOutingResponse(status=200)

    @classmethod
    @error_handling(proto.ConfirmOutingResponse)
    def reject_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.reject_by_outing_for_teacher(request.oid)

        return proto.ConfirmOutingResponse(status=200)