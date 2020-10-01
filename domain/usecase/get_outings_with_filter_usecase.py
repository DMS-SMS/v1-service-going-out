from domain.repository import OutingRepository
from domain.service.outing_domain_service import OutingDomainService


class GetOutingsWithFilterUseCase:
    def __init__(self, outing_repository, outing_domain_service):
        self.outing_repository: OutingRepository = outing_repository
        self.outing_domain_service: OutingDomainService = outing_domain_service

    def run(self, status, grade, class_, start, count):
        return self.outing_domain_service.paging_outings(
            self.outing_repository.get_outings_with_filter(
                status, grade, class_
            ),
            start,
            count,
        )