from typing import List, Optional

from domain.entity.parents import Parents
from domain.repository.parents_repository import ParentsRepository
from infrastructure.implementation.repository.mapper.parents_repository_mapper import \
    get_parents_by_student_uuid_mapper, get_parents_mapper
from infrastructure.auth.auth_handler import AuthHandler


class ParentsRepositoryImpl(ParentsRepository):
    def __init__(self):
        self.auth = AuthHandler()

    def find_by_student_uuid(self, uuid: str, student_uuid: str, x_request_id: str) -> Optional["Parents"]:
        return get_parents_by_student_uuid_mapper(self.auth.get_parents_with_student_uuid(uuid, student_uuid, x_request_id))

    def find_by_uuid(self, uuid:str, parent_uuid, x_request_id: str) -> Optional["Parents"]:
        return get_parents_mapper(uuid, self.auth.get_parents_inform(uuid, parent_uuid, x_request_id))