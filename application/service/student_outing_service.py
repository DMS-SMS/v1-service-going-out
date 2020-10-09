from domain.usecase.create_outing_usecase import CreateOutingUseCase
from domain.usecase.finish_go_out_usecase import FinishGoOutUseCase
from domain.usecase.get_card_usecase import GetCardUseCase
from domain.usecase.get_my_outings_usecase import GetMyOutingsUseCase
from domain.usecase.get_outing_inform_usecase import GetOutingInformUseCase
from domain.usecase.go_out_usecase import GoOutUseCase
from proto.python.outing import outing_student_pb2 as proto

from application.mapper import create_outing_mapper, get_outings_mapper

from domain.entity import Outing


class StudentOutingService:
    def __init__(
            self,
            create_outing_usecase,
            get_my_outings_usecase,
            get_outing_inform_usecase,
            get_card_usecase,
            go_out_usecase,
            finish_go_out_usecase
    ):
        self.create_outing_usecase: CreateOutingUseCase = create_outing_usecase
        self.get_my_outings_usecase: GetMyOutingsUseCase = get_my_outings_usecase
        self.get_outing_inform_usecase: GetOutingInformUseCase = get_outing_inform_usecase
        self.get_card_usecase: GetCardUseCase = get_card_usecase
        self.go_out_usecase: GoOutUseCase = go_out_usecase
        self.finish_go_out_usecase: FinishGoOutUseCase = finish_go_out_usecase

    def create_outing(self, request):
        entity: Outing = create_outing_mapper(request)
        oid = self.create_outing_usecase.run(entity)
        return proto.CreateOutingResponse(status=201, oid=oid)

    def get_student_outings(self, request):
        outings = self.get_my_outings_usecase.run(request.uuid, request.sid, request.start, request.count)

        response = proto.GetStudentOutingsResponse(status=200)
        response.outing.extend(get_outings_mapper(outings))

        return response

    def get_outing_inform(self, request):
        outing = self.get_outing_inform_usecase.run(request.uuid, request.oid)

        return proto.GetOutingInformResponse(
            status=200,
            place=outing._place,
            reason=outing._reason,
            date=outing._date,
            start_time=outing._start_time,
            end_time=outing._end_time,
            o_status=outing._status,
            o_situation=outing._situation,
        )

    def get_card_about_outing(self, request):
        outing, student = self.get_card_usecase.run(request.uuid, request.oid)
        return proto.GetCardAboutOutingResponse(
            status=200,
            place=outing._place,
            date=outing._date,
            start_time=outing._start_time,
            end_time=outing._end_time,
            o_status=outing._status,
            name=student._name,
            grade=student._grade,
            group=student._group,
            number=student._student_number,
            profile_image_uri=student._profile_image_uri,
        )

    def go_out(self, request):
        self.go_out_usecase.run(request.oid)
        return proto.GoOutResponse(status=200)

    def finish_go_out(self, request):
        self.finish_go_out_usecase.run(request.oid)
        return proto.GoOutResponse(status=200)
