from domain.service.uuid_service import uuidService

from infrastructure.util.string_util import compare_element

from domain.exception import Unauthorized


class uuidServiceImpl(uuidService):
    @classmethod
    def compare_uuid_and_sid(cls, uuid, sid):
        if not compare_element(uuid, sid):
            raise Unauthorized
