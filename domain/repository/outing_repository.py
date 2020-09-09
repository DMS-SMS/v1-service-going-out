from abc import abstractmethod, ABCMeta
from domain.entity.outing import Outing


class OutingRepository(metaclass=ABCMeta):
    @abstractmethod
    @classmethod
    def save(cls, outing: Outing):
        pass