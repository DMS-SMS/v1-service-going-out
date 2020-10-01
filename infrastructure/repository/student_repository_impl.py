from domain.repository.student_repository import StudentRepository
from domain.entity.student import Student

from infrastructure.mapper.student_repository_mapper import get_student_mapper
from infrastructure.service.auth_service import AuthService


class StudentRepositoryImpl(StudentRepository):
    auth_service = AuthService()

    @classmethod
    def get_student_by_uuid(cls, uuid: str) -> Student:
        return get_student_mapper(uuid, cls.auth_service.get_student_inform(uuid, uuid))
