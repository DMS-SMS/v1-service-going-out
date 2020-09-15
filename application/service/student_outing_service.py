from typing import List

from proto.python.outing import outing_student_pb2 as proto

from application.mapper import create_outing_mapper, get_outings_mapper
from application.decorator.error_handling import error_handling

from domain.repository import OutingRepository, StudentRepository
from domain.entity import Outing, Student
from domain.service.outing_domain_service import OutingDomainService


class StudentOutingService:
    def __init__(self, outing_repository, student_repository, outing_domain_service, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository

        self.outing_domain_service: OutingDomainService = outing_domain_service

        self.sms_service = sms_service

    @error_handling(proto.CreateOutingResponse)
    def create_outing(self, request):
        entity: Outing = create_outing_mapper(request)

        oid: str = self.outing_repository.save_and_get_oid(entity)
        o_code: str = self.outing_repository.set_and_get_parents_outing_code(oid)
        self.sms_service.send_to_parents(oid, o_code)

        return proto.CreateOutingResponse(status=201, oid=oid)

    @error_handling(proto.GetStudentOutingsResponse)
    def get_student_outings(self, request):
        response = proto.GetStudentOutingsResponse(status=200)

        self.outing_domain_service.compare_uuid_and_sid(request.uuid, request.sid)

        outings_entity: List["Outing"] = self.outing_domain_service.paging_outings(
            self.outing_repository.get_outings_by_student_id(request.sid),
            request.start,
            request.count,
        )

        response.outing.extend(get_outings_mapper(outings_entity))

        return response

    @error_handling(proto.GetOutingInformResponse)
    def get_outing_inform(self, request):
        outing: Outing = self.outing_repository.get_outing_by_oid(request.oid)

        self.outing_domain_service.compare_uuid_and_sid(
            request.uuid, outing._student_uuid
        )

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

    @error_handling(proto.GetCardAboutOutingResponse)
    def get_card_about_outing(self, request):
        outing: Outing = self.outing_repository.get_outing_by_oid(request.oid)
        student: Student = self.student_repository.get_student_by_uuid(
            outing._student_uuid
        )

        self.outing_domain_service.compare_uuid_and_sid(
            request.uuid, outing._student_uuid
        )

        return proto.GetCardAboutOutingResponse(
            status=200,
            place=outing._place,
            date=outing._date,
            start_time=outing._start_time,
            end_time=outing._end_time,
            o_status=outing._status,
            name=student._name,
            grade=student._grade,
            class_=student._class,
            number=student._student_number,
            profile_image_uri=student._profile_image_uri,
        )

    @error_handling(proto.GoOutResponse)
    def go_out(self, request):
        self.outing_repository.go_out(request.oid)
        return proto.GoOutResponse(status=200)

    @error_handling(proto.GoOutResponse)
    def finish_go_out(self, request):
        self.outing_repository.finish_go_out(request.oid)
        return proto.GoOutResponse(status=200)
