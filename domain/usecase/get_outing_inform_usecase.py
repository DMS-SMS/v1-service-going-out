from domain.entity import Outing
from domain.repository import OutingRepository
from domain.service.uuid_service import UuidService


class GetOutingInformUseCase:
    def __init__(self, outing_repository, uuid_service):
        self.outing_repository: OutingRepository = outing_repository
        self.uuid_service: UuidService = uuid_service

    def run(self, uuid, o_id):
        outing: Outing = self.outing_repository.get_outing_by_oid(o_id)

        self.uuid_service.compare_uuid_and_sid(
            uuid, outing._student_uuid
        )

        return outing