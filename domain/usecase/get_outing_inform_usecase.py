from domain.entity import Outing
from domain.exception import Unauthorized, OutingNotFound
from domain.repository.outing_repository import OutingRepository
from domain.repository.parents_repository import ParentsRepository
from domain.repository.student_repository import StudentRepository
from domain.service.uuid_service import UuidService


class GetOutingInformUseCase:
    def __init__(self, outing_repository, student_repository, parents_repository, uuid_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.parents_repository: ParentsRepository = parents_repository
        self.uuid_service: UuidService = uuid_service

    def run(self, uuid, outing_id, x_request_id):
        if self.student_repository.find_by_uuid(uuid, x_request_id) is None:
            if self.parents_repository.find_by_uuid(uuid, uuid, x_request_id) is None: raise Unauthorized()

        outing: Outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()

        if outing.student_uuid != uuid: raise Unauthorized()
        return outing