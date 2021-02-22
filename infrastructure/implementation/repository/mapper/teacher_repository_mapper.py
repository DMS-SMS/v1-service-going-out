from typing import Optional

from domain.entity.teacher import Teacher
from proto.python.auth import auth_teacher_pb2


def get_teacher_mapper(
        teacher_uuid, teacher_proto: Optional["auth_teacher_pb2.GetTeacherInformWithUUIDResponse"]
) -> Optional["Teacher"]:
    if teacher_proto == None: return None

    return Teacher(
        teacher_uuid=teacher_uuid,
        grade=teacher_proto.Grade,
        group=teacher_proto.Group,
        name=teacher_proto.Name,
        phone_number=teacher_proto.PhoneNumber
    )