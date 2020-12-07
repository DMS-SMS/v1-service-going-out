from typing import Optional

from domain.entity.parents import Parents
from proto.python.auth import auth_student_pb2
from proto.python.auth import auth_parent_pb2


def get_parents_by_student_uuid_mapper(
        parents_proto: Optional["auth_student_pb2.GetParentWithStudentUUIDResponse"]
    ) -> Optional[Parents]:
    if parents_proto is None: return None
    return Parents(
        uuid=parents_proto.ParentUUID,
        name=parents_proto.Name,
        phone_number=parents_proto.PhoneNumber
    )

def get_parents_mapper(
        uuid, parents_proto: Optional["auth_parent_pb2.GetParentInformWithUUIDResponse"]
    ) -> Optional[Parents]:
    if parents_proto is None: return None
    return Parents(
        uuid=uuid,
        name=parents_proto.Name,
        phone_number=parents_proto.PhoneNumber
    )
