from abc import abstractmethod, ABCMeta
from typing import Optional
from domain.entity.student import Student


class StudentRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_uuid(self, uuid: str, x_request_id: str) -> Optional["Student"]:
        pass

    @abstractmethod
    def find_all_by_inform(self, uuid: str, x_request_id: str, grade: Optional["int"] = None, group: Optional["int"] = None) -> ["str"]:
        pass