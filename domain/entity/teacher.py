class Teacher:
    def __init__(
        self,
        teacher_uuid=None,
        grade=None,
        group=None,
        name=None,
    ):
        self._teacher_uuid: str = teacher_uuid
        self._grade: int = grade
        self._group: int = group
        self._name: str = name