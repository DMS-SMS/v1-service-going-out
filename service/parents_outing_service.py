import time

from domain.entity import Outing, Student
from domain.usecase.get_account_by_uuid_usecase import GetAccountByUuidUseCase
from domain.usecase.get_outing_by_o_code_usecase import GetOutingByOCodeUseCase
from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from proto.python.outing import outing_parents_pb2 as proto
from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from service.util.get_x_request_id import get_x_request_id


class ParentsOutingService:
    def __init__(self, approve_outing_usecase, reject_outing_usecase, get_outing_by_o_code_usecase, get_account_by_uuid_usecase):
        self.approve_outing_usecase: ApproveOutingUseCase = approve_outing_usecase
        self.reject_outing_usecase: RejectOutingUseCase = reject_outing_usecase
        self.get_outing_by_o_code_usecase : GetOutingByOCodeUseCase = get_outing_by_o_code_usecase
        self.get_account_by_uuid_usecase: GetAccountByUuidUseCase = get_account_by_uuid_usecase

    def approve_outing(self, request, context):
        self.approve_outing_usecase.run(request.confirm_code)
        return proto.ConfirmOutingByOCodeResponse(status=200)

    def reject_outing(self, request, context):
        self.reject_outing_usecase.run(request.confirm_code)
        return proto.ConfirmOutingByOCodeResponse(status=200)

    def get_outing(self, request, context):
        outing: Outing = self.get_outing_by_o_code_usecase.run(request.confirm_code)
        student: Student = self.get_account_by_uuid_usecase.run(outing.student_uuid, get_x_request_id(context))

        return proto.GetOutingByOCodeResponse(
            status = 200,
            name=student._name,
            outing_id=outing.outing_uuid,
            start_time=int(time.mktime(outing.start_time.timetuple())),
            end_time=int(time.mktime(outing.end_time.timetuple())),
            place=outing.place,
            reason=outing.reason,
            situation=outing.situation
        )
