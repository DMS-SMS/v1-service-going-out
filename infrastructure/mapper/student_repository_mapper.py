from proto.python.auth import auth_student_pb2

from domain.entity.student import Student


def get_student_mapper(student_uuid, student_model: auth_student_pb2.GetStudentInformWithUUIDResponse) -> Student:
    return Student(
        student_uuid=student_uuid,
        grade=student_model.Grade,
        class_=student_model.Class,
        student_number=student_model.StudentNumber,
        name=student_model.Name,
        phone_number=student_model.PhoneNumber,
        profile_image_uri=student_model.ImageURI,
    )
