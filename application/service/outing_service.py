from typing import List

from proto.python.outing import outing_student_pb2 as proto

from application.mapper import create_outing_mapper, get_outings_mapper
from application.decorator.error_handling import error_handling

from domain.repository import OutingRepository
from domain.entity.outing import Outing
from domain.service.outing_domain_service import OutingDomainService

from infrastructure.repository import OutingRepositoryImpl
from infrastructure.util.sms_service import send_to_parents
from infrastructure.service.OutingDomainServiceImpl import OutingDomainServiceImpl


class OutingService:
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
            repository.get_outings_by_student_id(request.sid), request.start, request.count)

        response.outing.extend(get_outings_mapper(outings_entity))
        response.status = 201
        response.msg = "OK"

        return response