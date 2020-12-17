from abc import ABCMeta, abstractmethod
from typing import Optional


class ConfirmCodeRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, outing_uuid: str, confirm_code: str): pass

    @abstractmethod
    def find_by_code(self, confirm_code: str) -> Optional["str"]: pass

    @abstractmethod
    def delete_by_code(self, confirm_code: str): pass