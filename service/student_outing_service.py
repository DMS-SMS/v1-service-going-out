from time import mktime

from domain.usecase.create_outing_usecase import CreateOutingUseCase
from domain.usecase.finish_go_out_usecase import FinishGoOutUseCase
from domain.usecase.get_card_usecase import GetCardUseCase
from domain.usecase.get_my_outings_usecase import GetMyOutingsUseCase
from domain.usecase.get_outing_inform_usecase import GetOutingInformUseCase
from domain.usecase.go_out_usecase import GoOutUseCase

from service.mapper.student_outing_mapper import StudentOutingMapper
from proto.python.outing import outing_student_pb2 as proto
from service.util.get_x_request_id import get_x_request_id


class StudentOutingService:
    def __init__(
            self,
            create_outing_usecase,
            get_my_outings_usecase,
            get_outing_inform_usecase,
            get_card_usecase,
            go_out_usecase,
            finish_go_out_usecase,
            student_outing_mapper
    ):
        self.create_outing_usecase: CreateOutingUseCase = create_outing_usecase
        self.get_my_outings_usecase: GetMyOutingsUseCase = get_my_outings_usecase
        self.get_outing_inform_usecase: GetOutingInformUseCase = get_outing_inform_usecase
        self.get_card_usecase: GetCardUseCase = get_card_usecase
        self.go_out_usecase: GoOutUseCase = go_out_usecase
        self.finish_go_out_usecase: FinishGoOutUseCase = finish_go_out_usecase
        self.student_outing_mapper: StudentOutingMapper = student_outing_mapper

    def create_outing(self, request: proto.CreateOutingRequest, context):
        outing_uuid, parents = self.create_outing_usecase.run(
            request.uuid,
            request.situation,
            request.start_time,
            request.end_time,
            request.place,
            request.reason,
            get_x_request_id(context))
        return proto.CreateOutingResponse(
            status=201, outing_id=outing_uuid, code=-1 if not parents else 0 if parents._phone_number else -2)

    def get_student_outings(self, request: proto.GetStudentOutingsRequest, context):
        outings = self.get_my_outings_usecase.run(
            request.uuid,
            request.student_id,
            get_x_request_id(context))

        response = proto.GetStudentOutingsResponse(status=200)
        response.outing.extend(
            self.student_outing_mapper.get_student_outings_mapper(outings, request.start, request.count))

        return response

    def get_outing_inform(self, request: proto.GetOutingInformRequest, context):
        outing = self.get_outing_inform_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context))

        return proto.GetOutingInformResponse(
            status=200,

            outing_id=outing.outing_uuid,
            place=outing.place,
            reason=outing.reason,
            start_time=int(mktime(outing.start_time.timetuple()))-32400,
            end_time=int(mktime(outing.end_time.timetuple()))-32400,
            outing_status=outing.status,
            outing_situation=outing.situation,
            student_uuid=outing.student_uuid
        )

    def get_card_about_outing(self, request: proto.GetCardAboutOutingRequest, context):
        outing, student = self.get_card_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context)
        )

        return proto.GetCardAboutOutingResponse(
            status=200,

            place=outing.place,
            start_time=int(mktime(outing.start_time.timetuple()))-32400,
            end_time=int(mktime(outing.end_time.timetuple()))-32400,
            outing_status=outing.status,
            reason=outing.reason,

            name=student._name,
            grade=student._grade,
            group=student._group,
            number=student._student_number,
            profile_image_uri=student._profile_image_uri,
        )

    def go_out(self, request, context):
        self.go_out_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context))
        return proto.GoOutResponse(status=200)

    def finish_go_out(self, request, context):
        self.finish_go_out_usecase.run(
            request.uuid,
            request.outing_id,
            get_x_request_id(context))
        return proto.GoOutResponse(status=200)
