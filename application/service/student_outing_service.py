from typing import List

from proto.python.outing import outing_student_pb2 as proto

from application.mapper import create_outing_mapper, get_outings_mapper
from application.decorator.error_handling import error_handling

from domain.repository import OutingRepository, StudentRepository
from domain.entity import Outing, Student
from domain.service.outing_domain_service import OutingDomainService

from infrastructure.repository import OutingRepositoryImpl, StudentRepositoryImpl
from infrastructure.util.sms_service import send_to_parents
from infrastructure.service.OutingDomainServiceImpl import OutingDomainServiceImpl


class StudentOutingService:
    @classmethod
    @error_handling(proto.CreateOutingResponse)
    def create_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()
        entity: Outing = create_outing_mapper(request)

        oid: str = repository.save_and_get_oid(entity)
        o_code: str = repository.set_and_get_parents_outing_code(oid)
        send_to_parents(oid, o_code)

        return proto.CreateOutingResponse(status=201, msg="Created", oid=oid)

    @classmethod
    @error_handling(proto.GetStudentOutingsResponse)
    def get_student_outings(cls, request):
        response = proto.GetStudentOutingsResponse()

        repository: OutingRepository = OutingRepositoryImpl()
        domain_service: OutingDomainService = OutingDomainServiceImpl()

        domain_service.compare_uuid_and_sid(request.uuid, request.sid)

        outings_entity: List["Outing"] = domain_service.paging_outings(
            repository.get_outings_by_student_id(request.sid),
            request.start,
            request.count,
        )

        response.outing.extend(get_outings_mapper(outings_entity))
        response.status = 201
        response.msg = "OK"

        return response

    @classmethod
    @error_handling(proto.GetOutingInformResponse)
    def get_outing_inform(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()
        domain_service: OutingDomainService = OutingDomainServiceImpl()

        outing: Outing = repository.get_outing_by_oid(request.oid)

        domain_service.compare_uuid_and_sid(request.uuid, outing._student_uuid)

        return proto.GetOutingInformResponse(
            status=200,
            msg="OK",
            place=outing._place,
            reason=outing._reason,
            date=outing._date,
            start_time=outing._start_time,
            end_time=outing._end_time,
            o_status=outing._status,
            o_situation=outing._situation,
        )

    @classmethod
    @error_handling(proto.GetCardAboutOutingResponse)
    def get_card_about_outing(cls, request):
        outing_repository: OutingRepository = OutingRepositoryImpl()
        student_repository: StudentRepository = StudentRepositoryImpl()

        domain_service: OutingDomainService = OutingDomainServiceImpl()

        outing: Outing = outing_repository.get_outing_by_oid(request.oid)
        student: Student = student_repository.get_student_by_uuid(outing._student_uuid)

        domain_service.compare_uuid_and_sid(request.uuid, outing._student_uuid)

        return proto.GetCardAboutOutingResponse(
            status=200,
            msg="OK",
            place=outing._place,
            date=outing._date,
            start_time=outing._start_time,
            end_time=outing._end_time,
            o_status=outing._status,
            name=student._name,
            grade=student._grade,
            class_=student._class,
            number=student._student_number,
            image_url=student._profile_uri,
        )

    @classmethod
    @error_handling(proto.GoOutResponse)
    def go_out(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.go_out(request.oid)

        return proto.GoOutResponse(status=200)

    @classmethod
    @error_handling(proto.GoOutResponse)
    def finish_go_out(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()

        repository.finish_go_out(request.oid)

        return proto.GoOutResponse(status=200)
