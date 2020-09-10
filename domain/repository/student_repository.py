from abc import abstractmethod, ABCMeta
from domain.entity.student import Student


class StudentRepository(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def get_student_by_uuid(cls, uuid: str) -> Student:
        pass
