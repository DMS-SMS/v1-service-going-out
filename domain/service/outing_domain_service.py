from typing import List
from abc import ABCMeta, abstractmethod

from domain.entity.outing import Outing


class OutingDomainService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def paging_outings(cls, outings: List["Outing"], start: int, count: int) -> List["Outing"]:
        pass


    @classmethod
    @abstractmethod
    def compare_uuid_and_sid(cls, uuid, sid):
        pass