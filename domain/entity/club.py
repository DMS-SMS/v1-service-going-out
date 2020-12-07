from typing import List

class Club:
    def __init__(
        self,
        uuid=None,
        name=None,
        members=None,
    ):
        if members is None:
            members = list()
        self._uuid: str = uuid
        self._name: str = name
        self._members: List["str"] = members
