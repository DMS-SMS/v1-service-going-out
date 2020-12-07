from domain.usecase.approve_outing_teacher_usecase import ApproveOutingTeacherUseCase
from domain.usecase.certify_outing_usecase import CertifyOutingUseCase
from domain.usecase.get_outings_with_filter_usecase import GetOutingsWithFilterUseCase
from domain.usecase.reject_outing_teacher_usecase import RejectOutingTeacherUseCase
from proto.python.outing import outing_teacher_pb2 as proto
from service.mapper.teacher_outing_mapper import TeacherOutingMapper
from service.util.get_x_request_id import get_x_request_id


class TeacherOutingService:
    def __init__(
            self,
            approve_outing_teacher_usecase,
            reject_outing_teacher_usecase,
            certify_outing_usecase,
            get_outings_with_filter_usecase,
            teacher_outing_mapper
    ):
        self.approve_outing_teacher_usecase: ApproveOutingTeacherUseCase = approve_outing_teacher_usecase
        self.reject_outing_teacher_usecase: RejectOutingTeacherUseCase = reject_outing_teacher_usecase
        self.certify_outing_usecase: CertifyOutingUseCase = certify_outing_usecase
        self.get_outings_with_filter_usecase: GetOutingsWithFilterUseCase = get_outings_with_filter_usecase
        self.teacher_outing_mapper: TeacherOutingMapper = teacher_outing_mapper


    def approve_outing(self, request, context):
        self.approve_outing_teacher_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context)
        )
        return proto.ConfirmOutingResponse(status=200)

    def reject_outing(self, request, context):
        self.reject_outing_teacher_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context)
        )
        return proto.ConfirmOutingResponse(status=200)

    def certify_outing(self, request, context):
        self.certify_outing_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context)
        )
        return proto.ConfirmOutingResponse(status=200)

    def get_outings_with_filter(self, request, context):
        x_request_id = get_x_request_id(context)
        outings = self.get_outings_with_filter_usecase.run(
            request.uuid, x_request_id, request.status, request.grade, request.group, request.floor)

        response = proto.OutingResponse()
        response.status = 200
        response.outing.extend(
            self.teacher_outing_mapper.get_outings_for_teacher_mapper(outings, x_request_id, request.start, request.count))

        return response