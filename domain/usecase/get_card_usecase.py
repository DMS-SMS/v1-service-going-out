from domain.entity import Outing, Student
from domain.exception import OutingNotFound
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.service.uuid_service import UuidService
from domain.exception.business_exception.unauthorized import Unauthorized


class GetCardUseCase:
    def __init__(self, outing_repository, student_repository, uuid_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.uuid_service: UuidService = uuid_service

    def run(self, uuid, outing_id, x_request_id):
        student: Student = self.student_repository.find_by_uuid(uuid, x_request_id)
        if student is None: raise Unauthorized()

        outing: Outing = self.outing_repository.find_by_id(outing_id)
        if outing == None: raise OutingNotFound()

        if uuid != outing.student_uuid: raise Unauthorized()

        return outing, student