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
    def get_outings_by_student_id(cls, sid: str) -> List["Outing"]:
        pass

    @classmethod
    @abstractmethod
    def approve_by_outing_for_teacher(cls, oid: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def approve_by_outing_for_parents(cls, o_code) -> None:
        pass

    @classmethod
    @abstractmethod
    def reject_by_outing_for_teacher(cls, oid: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def reject_by_outing_for_parents(cls, o_code: str) -> None:
        pass

    @classmethod
    @abstractmethod
    def certify_by_outing_for_teacher(cls, oid) -> None:
        pass

    @classmethod
    @abstractmethod
    def get_outings_with_filter(cls, status, grade, class_) -> List["Outing"]:
        pass

    @classmethod
    @abstractmethod
    def get_is_late(cls, oid) -> bool:
        pass

    @classmethod
    @abstractmethod
    def go_out(cls, oid) -> None:
        pass

    @classmethod
    @abstractmethod
    def finish_go_out(cls, oid) -> None:
        pass
