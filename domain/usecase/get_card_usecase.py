from domain.entity import Outing, Student
from domain.repository import OutingRepository, StudentRepository
from domain.service.outing_domain_service import OutingDomainService


class GetCardUseCase:
    def __init__(self, outing_repository, student_repository, outing_domain_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.outing_domain_service: OutingDomainService = outing_domain_service

    def run(self, uuid, o_id):
        outing: Outing = self.outing_repository.get_outing_by_oid(o_id)
        student: Student = self.student_repository.get_student_by_uuid(
            outing._student_uuid
        )

        self.outing_domain_service.compare_uuid_and_sid(
            uuid, outing._student_uuid
        )

        return outing, student