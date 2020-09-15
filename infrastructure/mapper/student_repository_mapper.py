from infrastructure.model import StudentInformsModel

from domain.entity.student import Student


def get_student_mapper(student_model: StudentInformsModel) -> Student:
    return Student(
        student_uuid=student_model.student_uuid,
        grade=student_model.grade,
        class_=student_model.class_,
        student_number=student_model.student_number,
        name=student_model.name,
        phone_number=student_model.phone_number,
        profile_uri=student_model.profile_uri,
    )
