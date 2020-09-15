from typing import List, Optional

from domain.entity.outing import Outing
from domain.repository.outing_repository import OutingRepository


class MockOutingRepository(OutingRepository):
    mock_outing = Outing(
            outing_uuid="outing-aaaabbbbcccc",
            student_uuid="student-aaaabbbbcccc",
            status="0",
            situation="NORMAL",
            accept_teacher=None,
            date="1999-02-03",
            start_time="1111",
            end_time="1111",
            place="홍대",
            reason="스윙스랑 돈까스 먹으러감",
            arrival_date=None,
            arrival_time=None,
        )

    @classmethod
    def save_and_get_oid(cls, outing: Outing) -> str:
        return "outing-aaaabbbbcccc"

    @classmethod
    def set_and_get_parents_outing_code(cls, oid: str) -> str:
        return "aaaabbbbccccddddeeeeffff"

    @classmethod
    def get_outing_by_oid(cls, oid: str) -> Outing:
        return cls.mock_outing

    @classmethod
    def get_outings_by_student_id(cls, sid: str) -> List["Outing"]:
        return [cls.mock_outing]

    @classmethod
    def approve_by_outing_for_teacher(cls, oid: str) -> None:
        pass

    @classmethod
    def approve_by_outing_for_parents(cls, o_code: str) -> None:
        pass

    @classmethod
    def reject_by_outing_for_teacher(cls, oid: str) -> None:
        pass

    @classmethod
    def reject_by_outing_for_parents(cls, o_code):
        pass

    @classmethod
    def certify_by_outing_for_teacher(cls, oid) -> None:
        pass

    @classmethod
    def get_outings_with_filter(cls, status, grade, class_) -> List["Outing"]:
        return [cls.mock_outing]

    @classmethod
    def get_is_late(cls, oid) -> Optional[bool]:
        return True

    @classmethod
    def go_out(cls, oid) -> None:
        pass

    @classmethod
    def finish_go_out(cls, oid) -> None:
        pass