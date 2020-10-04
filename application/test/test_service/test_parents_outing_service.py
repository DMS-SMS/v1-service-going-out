from unittest import TestCase

from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from proto.python.outing import outing_parents_pb2

from application.service.parents_outing_service import ParentsOutingService
from application.test.test_service.mock import MockOutingRepository


class TestParentsOutingService(TestCase):
    def setUp(self) -> None:
        self.outing_repository = MockOutingRepository()
        self.service = ParentsOutingService(
            approve_outing_usecase=ApproveOutingUseCase(
                self.outing_repository
            ),
            reject_outing_usecase=RejectOutingUseCase(
                self.outing_repository
            )
        )
        self.proto = outing_parents_pb2

    def test_approve_outing(self):
        request = self.proto.ConfirmOutingByOCodeRequest(o_code="outing-aaaabbbbcccc")
        response = self.proto.ConfirmOutingByOCodeResponse(status=200)

        self.assertEqual(self.service.approve_outing(request), response)

    def test_reject_outing(self):
        request = self.proto.ConfirmOutingByOCodeRequest(o_code="outing-aaaabbbbcccc")
        response = self.proto.ConfirmOutingByOCodeResponse(status=200)

        self.assertEqual(self.service.reject_outing(request), response)
