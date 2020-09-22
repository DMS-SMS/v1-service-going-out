from typing import List

from domain.entity.outing import Outing
from domain.service.outing_domain_service import OutingDomainService


class MockOutingDomainService(OutingDomainService):
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
    def paging_outings(
        cls, outings: List["Outing"], start: int, count: int
    ) -> List["Outing"]:
        return [cls.mock_outing]

    @classmethod
    def compare_uuid_and_sid(cls, uuid, sid):
        pass
