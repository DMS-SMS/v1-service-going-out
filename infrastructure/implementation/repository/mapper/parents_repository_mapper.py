from typing import Optional

from domain.entity.parents import Parents
from proto.python.auth import auth_student_pb2


def get_parents_mapper(
        parents_proto: Optional["auth_student_pb2.GetParentWithStudentUUIDResponse"]
    ) -> Optional[Parents]:
    if Parents is None: return None
    return Parents(
        uuid=parents_proto.ParentUUID,
        name=parents_proto.Name,
        phone_number=parents_proto.PhoneNumber
    )
