from typing import List

from domain.entity.outing import Outing
from domain.service.paging_service import PagingService

from infrastructure.util.list_util import paging_list


class PagingServiceImpl(PagingService):
    @classmethod
    def paging_outings(
        cls, outings: List["Outing"], start: int, count: int
    ) -> List["Outing"]:
        return paging_list(outings, start, count)