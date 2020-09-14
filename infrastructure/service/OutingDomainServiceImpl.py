from typing import List

from domain.entity.outing import Outing
from domain.service.outing_domain_service import OutingDomainService

from infrastructure.util.list_util import paging_list
from infrastructure.util.string_util import compare_element

from infrastructure.exception import Unauthorized


class OutingDomainServiceImpl(OutingDomainService):
    @classmethod
    def paging_outings(
        cls, outings: List["Outing"], start: int, count: int
    ) -> List["Outing"]:
        return paging_list(outings, start, count)

    @classmethod
    def compare_uuid_and_sid(cls, uuid, sid):
        if not compare_element(uuid, sid):
            raise Unauthorized
