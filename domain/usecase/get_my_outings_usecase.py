from domain.repository import OutingRepository
from domain.service.uuid_service import uuidService
from domain.service.paging_service import pagingService


class GetMyOutingsUseCase:
    def __init__(self, outing_repository, paging_service, uuid_service):
        self.outing_repository: OutingRepository = outing_repository
        self.paging_service: pagingService = paging_service
        self.uuid_service: uuidService = uuid_service


    def run(self, uuid, s_id, start, count):
        self.uuid_service.compare_uuid_and_sid(uuid, s_id)

        return self.paging_service.paging_outings(
            self.outing_repository.get_outings_by_student_id(s_id),
            start,
            count,
        )