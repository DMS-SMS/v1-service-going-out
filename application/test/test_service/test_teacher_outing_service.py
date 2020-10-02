from unittest import TestCase

from proto.python.outing import outing_teacher_pb2

from application.service.teacher_outing_service import TeacherOutingService
from application.test.test_service.mock import (
    MockOutingRepository,
    MockOutingDomainService,
)


class TestTeacherOutingService(TestCase):
    def setUp(self) -> None:
        self.service = TeacherOutingService(
            MockOutingRepository(), MockOutingDomainService()
        )
        self.proto = outing_teacher_pb2

    def test_approve_outing(self):
        request = self.proto.ConfirmOutingRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )
        response = self.proto.ConfirmOutingResponse(status=200)

        self.assertEqual(self.service.approve_outing(request), response)

    def test_reject_outing(self):
        request = self.proto.ConfirmOutingRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )
        response = self.proto.ConfirmOutingResponse(status=200)

        self.assertEqual(self.service.reject_outing(request), response)

    def test_certify_outing(self):
        request = self.proto.ConfirmOutingRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )
        response = self.proto.ConfirmOutingResponse(status=200)

        self.assertEqual(self.service.certify_outing(request), response)

    def get_outings_with_filter(self):
        request = self.proto.GetOutingWithFilterRequest(
            uuid="student-aaaabbbbcccc", status="0", grade=1, class_=1
        )

        outing = self.proto.Outing()

        outing.name = "스윙스"
        outing.grade = 1
        outing.class_ = 1
        outing.number = 11
        outing.place = "홍대"
        outing.reason = "스윙스랑 돈까스 먹으러감"
        outing.date = "1999-02-03"
        outing.start_time = "1111"
        outing.end_time = "1111"
        outing.situation = "NORMAL"
        outing.status = "0"

        response = self.proto.OutingResponse(status=200)
        response.outing.extend([outing])

        self.assertEqual(self.service.get_outings_with_filter(request), response)
