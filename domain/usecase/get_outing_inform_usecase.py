from domain.entity import Outing
from domain.repository import OutingRepository
from domain.service.outing_domain_service import OutingDomainService


class GetOutingInformUseCase:
    def __init__(self, outing_repository, outing_domain_service):
        self.outing_repository: OutingRepository = outing_repository
        self.outing_domain_service: OutingDomainService = outing_domain_service

    def run(self, uuid, o_id):
        outing: Outing = self.outing_repository.get_outing_by_oid(o_id)

        self.outing_domain_service.compare_uuid_and_sid(
            uuid, outing._student_uuid
        )

        return outing