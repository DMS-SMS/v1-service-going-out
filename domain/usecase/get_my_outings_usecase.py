from domain.exception import Unauthorized
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.service.uuid_service import UuidService


class GetMyOutingsUseCase:
    def __init__(self, outing_repository, student_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository


    def run(self, uuid, student_id, x_request_id):
        if self.student_repository.find_by_uuid(uuid, x_request_id) is None: raise Unauthorized()
        else:
            if uuid != student_id: raise Unauthorized()

        return self.outing_repository.find_all_by_student_uuid(student_id)