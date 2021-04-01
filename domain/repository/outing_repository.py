from abc import ABCMeta, abstractmethod
from typing import List, Optional

from domain.entity import Outing


class OutingRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, outing: Outing): pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional["Outing"]: pass

    @abstractmethod
    def find_all_by_status(self, status: str) -> List["Outing"]: pass

    @abstractmethod
    def find_all_by_student_uuid(self, student_id): pass

    @abstractmethod
    def find_all_by_student_uuid_and_status(self, student_uuid: str, status: str) -> List["Outing"]: pass

    @abstractmethod
    def find_by_student_uuid_and_time(self, student_uuid: str, time: int) -> Optional["Outing"]: pass

    @abstractmethod
    def find_all_by_student_uuid_and_status_and_term(
            self, student_uuid: str, status: str, start_time: int, end_time: int): pass

    @abstractmethod
    def find_all_by_status_and_term(self, status: str, start_time: str, end_time: int): pass
