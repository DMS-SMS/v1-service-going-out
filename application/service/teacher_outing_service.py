from proto.python.outing import outing_teacher_pb2 as proto

from application.decorator.error_handling import error_handling
from application.mapper.outing_mapper import get_outings_for_teacher_mapper

from domain.repository.outing_repository import OutingRepository
from domain.service.outing_domain_service import OutingDomainService

from infrastructure.repository.outing_repository_impl import OutingRepositoryImpl
from infrastructure.service.OutingDomainServiceImpl import OutingDomainServiceImpl


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

    @classmethod
    @error_handling(proto.ConfirmOutingResponse)
    def certify_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.certify_by_outing_for_teacher(request.oid)

        return proto.ConfirmOutingResponse(status=200)

    @classmethod
    @error_handling(proto.OutingResponse)
    def get_outings_with_filter(cls, request):
        response = proto.OutingResponse()
        repository: OutingRepository = OutingRepositoryImpl()
        domain_service: OutingDomainService = OutingDomainServiceImpl()


        outings = domain_service.paging_outings(
            repository.get_outings_with_filter(request.status, request.grade, request.class_), request.start, request.count)


        response.status = 200
        response.outing.extend(get_outings_for_teacher_mapper(outings))

        return response