from abc import abstractmethod, ABCMeta
from typing import Optional
from domain.entity.teacher import Teacher


class TeacherRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_uuid(self, uuid: str, account_uuid: str, x_request_id: str) -> Optional["Teacher"]:
        pass