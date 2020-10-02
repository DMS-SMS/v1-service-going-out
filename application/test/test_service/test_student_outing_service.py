from unittest import TestCase

from domain.usecase.create_outing_usecase import CreateOutingUseCase
from domain.usecase.finish_go_out_usecase import FinishGoOutUseCase
from domain.usecase.get_card_usecase import GetCardUseCase
from domain.usecase.get_my_outings_usecase import GetMyOutingsUseCase
from domain.usecase.get_outing_inform_usecase import GetOutingInformUseCase
from domain.usecase.go_out_usecase import GoOutUseCase
from proto.python.outing import outing_student_pb2

from application.service.student_outing_service import StudentOutingService
from application.test.test_service.mock import (
    MockOutingRepository,
    MockStudentRepository,
    MockOutingDomainService,
    MockSMSService,
)


class TestStudentOutingService(TestCase):
    def setUp(self) -> None:
        self.outing_repository = MockOutingRepository()
        self.student_repository = MockStudentRepository()
        self.outing_domain_service = MockOutingDomainService()
        self.sms_service = MockSMSService()

        self.service = StudentOutingService(
            create_outing_usecase=CreateOutingUseCase(
                self.outing_repository,
                self.student_repository,
                self.sms_service,
            ),
            get_my_outings_usecase=GetMyOutingsUseCase(
                self.outing_repository,
                self.outing_domain_service
            ),
            get_outing_inform_usecase=GetOutingInformUseCase(
                self.outing_repository,
                self.outing_domain_service
            ),
            get_card_usecase=GetCardUseCase(
                self.outing_repository,
                self.student_repository,
                self.outing_domain_service
            ),
            go_out_usecase=GoOutUseCase(
                self.outing_repository
            ),
            finish_go_out_usecase=FinishGoOutUseCase(
                self.outing_repository
            )
        )
        self.proto = outing_student_pb2

    def test_create_outing(self):
        request = self.proto.CreateOutingRequest(
            uuid="student-aaaabbbbcccc",
            date="2020-09-20",
            start_time="1000",
            end_time="2400",
            place="홍대",
            reason="스윙스랑 돈까스 먹으러가요",
            situation="NORMAL",
        )
        response = self.proto.CreateOutingResponse(
            status=201, oid="outing-aaaabbbbcccc"
        )

        self.assertEqual(self.service.create_outing(request), response)

    def test_get_student_outings(self):
        request = self.proto.GetStudentOutingsRequest(
            uuid="student-aaaabbbbcccc", sid="student-aaaabbbbcccc", start=0, count=1
        )

        response = self.proto.GetStudentOutingsResponse(status=200)

        outing = self.proto.StudentOuting()

        outing.place = "홍대"
        outing.reason = "스윙스랑 돈까스 먹으러감"
        outing.date = "1999-02-03"
        outing.start_time = "1111"
        outing.end_time = "1111"
        outing.situation = "NORMAL"
        outing.status = "0"

        response.outing.extend([outing])

        self.assertEqual(self.service.get_student_outings(request), response)

    def test_get_outing_inform(self):
        request = self.proto.GetOutingInformRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )

        response = self.proto.GetOutingInformResponse(
            status=200,
            place="홍대",
            reason="스윙스랑 돈까스 먹으러감",
            date="1999-02-03",
            start_time="1111",
            end_time="1111",
            o_status="0",
            o_situation="NORMAL",
        )

        self.assertEqual(self.service.get_outing_inform(request), response)

    def test_get_card_about_outing(self):
        request = self.proto.GetCardAboutOutingRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )

        response = self.proto.GetCardAboutOutingResponse(
            status=200,
            place="홍대",
            date="1999-02-03",
            start_time="1111",
            end_time="1111",
            o_status="0",
            name="스윙스",
            grade=1,
            group=1,
            number=11,
            profile_image_uri="/swings-pork-cutlet",
        )

        self.assertEqual(self.service.get_card_about_outing(request), response)

    def test_go_out(self):
        request = self.proto.GoOutRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )
        response = self.proto.GoOutResponse(status=200)

        self.assertEqual(self.service.go_out(request), response)

    def test_finish_go_out(self):
        request = self.proto.GoOutRequest(
            uuid="student-aaaabbbbcccc", oid="outing-aaaabbbbcccc"
        )
        response = self.proto.GoOutResponse(status=200)

        self.assertEqual(self.service.finish_go_out(request), response)
