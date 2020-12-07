from abc import ABCMeta, abstractmethod
from typing import List, Optional

from domain.entity.club import Club


class ClubRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_all_by_floor(self, uuid: str, floor: int) -> List["Club"]: pass