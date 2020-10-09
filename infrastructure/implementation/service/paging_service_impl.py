from typing import List

from domain.entity.outing import Outing
from domain.service.paging_service import pagingService

from infrastructure.util.list_util import paging_list


class pagingServiceImpl(pagingService):
    @classmethod
    def paging_outings(
        cls, outings: List["Outing"], start: int, count: int
    ) -> List["Outing"]:
        return paging_list(outings, start, count)