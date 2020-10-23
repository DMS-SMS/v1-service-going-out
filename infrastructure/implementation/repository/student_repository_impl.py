from typing import List, Optional

from domain.repository.student_repository import StudentRepository
from domain.entity.student import Student

from infrastructure.implementation.repository.mapper.student_repository_mapper import get_student_mapper
from infrastructure.auth.auth_handler import AuthHandler


class StudentRepositoryImpl(StudentRepository):
    def __init__(self):
        self.auth = AuthHandler()

    def find_by_uuid(self, uuid: str, x_request_id: str) -> Student:
        return get_student_mapper(uuid, self.auth.get_student_inform(uuid, uuid, x_request_id))

    def find_all_by_inform(
            self, uuid: str, x_request_id: str, grade: Optional["int"] = None, group: Optional["int"] = None
    ) -> ["str"]:
        student_uuids = self.auth.get_uuid_with_inform(uuid, x_request_id, grade=grade, group=group)
        if student_uuids is None: return []

        return student_uuids