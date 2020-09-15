from proto.python.outing import outing_teacher_pb2 as proto

from application.decorator.error_handling import error_handling
from application.mapper.outing_mapper import get_outings_for_teacher_mapper

from domain.repository.outing_repository import OutingRepository
from domain.service.outing_domain_service import OutingDomainService


class TeacherOutingService:
    def __init__(self, outing_repository, outing_domain_service):
        self.outing_repository: OutingRepository = outing_repository

        self.outing_domain_service: OutingDomainService = outing_domain_service

    @error_handling(proto.ConfirmOutingResponse)
    def approve_outing(self, request):
        self.outing_repository.approve_by_outing_for_teacher(request.oid)
        return proto.ConfirmOutingResponse(status=200)

    @error_handling(proto.ConfirmOutingResponse)
    def reject_outing(self, request):
        self.outing_repository.reject_by_outing_for_teacher(request.oid)
        return proto.ConfirmOutingResponse(status=200)

    @error_handling(proto.ConfirmOutingResponse)
    def certify_outing(self, request):
        self.outing_repository.certify_by_outing_for_teacher(request.oid)
        return proto.ConfirmOutingResponse(status=200)

    @error_handling(proto.OutingResponse)
    def get_outings_with_filter(self, request):
        response = proto.OutingResponse()
        outings = self.outing_domain_service.paging_outings(
            self.outing_repository.get_outings_with_filter(
                request.status, request.grade, request.class_
            ),
            request.start,
            request.count,
        )

        response.status = 200
        response.outing.extend(get_outings_for_teacher_mapper(outings))

        return response
