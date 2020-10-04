from domain.repository import OutingRepository, StudentRepository
from domain.service.outing_domain_service import OutingDomainService


class GetMyOutingsUseCase:
    def __init__(self, outing_repository, outing_domain_service):
        self.outing_repository: OutingRepository = outing_repository
        self.outing_domain_service: OutingDomainService = outing_domain_service


    def run(self, uuid, s_id, start, count):
        self.outing_domain_service.compare_uuid_and_sid(uuid, s_id)

        return self.outing_domain_service.paging_outings(
            self.outing_repository.get_outings_by_student_id(s_id),
            start,
            count,
        )