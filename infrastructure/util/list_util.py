from typing import List


def paging_list(list: List, start: int, count: int) -> List:
    return list[start : start + count]
