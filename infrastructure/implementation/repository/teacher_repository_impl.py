from typing import Optional, List

from domain.entity.teacher import Teacher
from domain.repository.teacher_repository import TeacherRepository

from infrastructure.implementation.repository.mapper.teacher_repository_mapper import get_teacher_mapper
from infrastructure.auth.auth_handler import AuthHandler


class TeacherRepositoryImpl(TeacherRepository):
    def __init__(self):
        self.auth = AuthHandler()

    def find_by_uuid(self, uuid: str, account_uuid: str, x_request_id: str) -> Optional["Teacher"]:
        return get_teacher_mapper(uuid, self.auth.get_teacher_inform(uuid, account_uuid, x_request_id))

    def find_by_grade_and_group(self, uuid: str, grade: int, group: int, x_request_id: str) -> List["str"]:
        return self.auth.get_teacher_uuids_with_inform(uuid, grade, group, x_request_id)
