class Student:
    def __init__(
        self,
        student_uuid=None,
        grade=None,
        group=None,
        student_number=None,
        name=None,
        phone_number=None,
        profile_image_uri=None,
    ):
        self._student_uuid: str = student_uuid
        self._grade: int = grade
        self._group: int = group
        self._student_number: int = student_number
        self._name: str = name
        self._phone_number: str = phone_number
        self._profile_image_uri: str = profile_image_uri