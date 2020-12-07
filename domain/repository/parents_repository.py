from abc import abstractmethod, ABCMeta
from typing import Optional
from domain.entity.parents import Parents


class ParentsRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_student_uuid(self, uuid: str, student_uuid: str, x_request_id: str) -> Optional["Parents"]:
        pass

    @abstractmethod
    def find_by_uuid(self, uuid:str, parent_uuid, x_request_id: str) -> Optional["Parents"]:
        pass