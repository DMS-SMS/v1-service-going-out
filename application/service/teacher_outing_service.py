from domain.usecase.approve_outing_teacher_usecase import ApproveOutingTeacherUseCase
from domain.usecase.certify_outing_usecase import CertifyOutingUseCase
from domain.usecase.get_outings_with_filter_usecase import GetOutingsWithFilterUseCase
from domain.usecase.reject_outing_teacher_usecase import RejectOutingTeacherUseCase
from proto.python.outing import outing_teacher_pb2 as proto

from application.mapper.outing_mapper import get_outings_for_teacher_mapper

class TeacherOutingService:
    def __init__(
            self,
            approve_outing_teacher_usecase,
            reject_outing_teacher_usecase,
            certify_outing_usecase,
            get_outings_with_filter_usecase
    ):
        self.approve_outing_teacher_usecase: ApproveOutingTeacherUseCase = approve_outing_teacher_usecase
        self.reject_outing_teacher_usecase: RejectOutingTeacherUseCase = reject_outing_teacher_usecase
        self.certify_outing_usecase: CertifyOutingUseCase = certify_outing_usecase
        self.get_outings_with_filter_usecase: GetOutingsWithFilterUseCase = get_outings_with_filter_usecase


    def approve_outing(self, request):
        self.approve_outing_teacher_usecase.run(request.oid)
        return proto.ConfirmOutingResponse(status=200)

    def reject_outing(self, request):
        self.reject_outing_teacher_usecase.run(request.oid)
        return proto.ConfirmOutingResponse(status=200)

    def certify_outing(self, request):
        self.certify_outing_usecase.run(request.oid)
        return proto.ConfirmOutingResponse(status=200)

    def get_outings_with_filter(self, request):
        outings = self.get_outings_with_filter_usecase.run(
            request.status, request.grade, request.group, request.start, request.count)

        response = proto.OutingResponse()
        response.status = 200
        response.outing.extend(get_outings_for_teacher_mapper(outings))

        return response
