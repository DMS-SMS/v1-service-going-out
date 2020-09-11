from abc import abstractmethod, ABCMeta
from typing import List

from domain.entity.outing import Outing


class OutingRepository(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def save_and_get_oid(cls, outing: Outing) -> str:
        pass

    @classmethod
    @abstractmethod
    def set_and_get_parents_outing_code(cls, oid: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_outing_by_oid(cls, oid: str) -> Outing:
        pass

    @classmethod
    @abstractmethod
    def get_outings_by_student_id(cls, oid: str) -> List["Outing"]:
        pass