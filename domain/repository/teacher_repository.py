from abc import abstractmethod, ABCMeta
from typing import Optional, List
from domain.entity.teacher import Teacher


class TeacherRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_uuid(self, uuid: str, account_uuid: str, x_request_id: str) -> Optional["Teacher"]:
        pass

    @abstractmethod
    def find_by_grade_and_group(self, uuid: str, grade: int, group: int, x_request_id: str) -> List["str"]:
        pass