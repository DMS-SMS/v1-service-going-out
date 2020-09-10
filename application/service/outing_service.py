from proto.python.outing import outing_student_pb2

from application.mapper import create_outing_mapper

from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing

from infrastructure.repository.outing_repository_impl import OutingRepositoryImpl
from infrastructure.util.sms_service import send_to_parents
from infrastructure.exception import OutingExist


class OutingService:
    @classmethod
    def create_outing(cls, request):
        repository: OutingRepository = OutingRepositoryImpl()
        entity: Outing = create_outing_mapper(request)

        response = outing_student_pb2.CreateOutingResponse

        try:
            oid: str = repository.save_and_get_oid(entity)
            o_code: str = repository.set_and_get_parents_outing_code(oid)
            send_to_parents(oid, o_code)

        except OutingExist as e:
            return response(status=e.status, code=e.code, msg=e.msg)

        return response(status=201, msg="Created", oid=oid)