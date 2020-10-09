from domain.repository import OutingRepository
from domain.service.paging_service import pagingService


class GetOutingsWithFilterUseCase:
    def __init__(self, outing_repository, paging_service):
        self.outing_repository: OutingRepository = outing_repository
        self.paging_service: pagingService = paging_service

    def run(self, status, grade, group, start, count):
        return self.paging_service.paging_outings(
            self.outing_repository.get_outings_with_filter(
                status, grade, group
            ),
            start,
            count,
        )