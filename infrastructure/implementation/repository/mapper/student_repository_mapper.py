from typing import Optional

from proto.python.auth import auth_student_pb2

from domain.entity.student import Student


def get_student_mapper(
        student_uuid, student_proto: Optional["auth_student_pb2.GetStudentInformWithUUIDResponse"]
    ) -> Optional["Student"]:
    return Student(
        student_uuid=student_uuid,
        grade=student_proto.Grade,
        group=student_proto.Group,
        student_number=student_proto.StudentNumber,
        name=student_proto.Name,
        phone_number=student_proto.PhoneNumber,
        profile_image_uri=student_proto.ImageURI,
    )
