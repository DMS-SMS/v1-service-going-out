from domain.repository.student_repository import StudentRepository
from domain.entity.student import Student


class MockStudentRepository(StudentRepository):
    mock_student = Student(
        student_uuid="student-aaaabbbbcccc",
        grade=1,
        group=1,
        student_number=11,
        name="스윙스",
        phone_number="11122223333",
        profile_image_uri="/swings-pork-cutlet",
    )

    @classmethod
    def get_student_by_uuid(cls, uuid: str) -> Student:
        return cls.mock_student
