from domain.repository.student_repository import StudentRepository
from domain.entity.student import Student

from infrastructure.mapper.student_repository_mapper import get_student_mapper
from infrastructure.extension import db_session
from infrastructure.model import StudentInformsModel


class StudentRepositoryImpl(StudentRepository):
    @classmethod
    def get_student_by_uuid(cls, uuid: str) -> Student:
        return get_student_mapper(db_session.query(StudentInformsModel)
                                  .filter(StudentInformsModel.student_uuid == uuid).first())