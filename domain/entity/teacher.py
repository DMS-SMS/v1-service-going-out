class Teacher:
    def __init__(
            self,
            teacher_uuid=None,
            grade=None,
            group=None,
            name=None,
            phone_number=None
    ):
        self._teacher_uuid: str = teacher_uuid
        self._grade: int = grade
        self._group: int = group
        self._name: str = name
        self._phone_number: str = phone_number
