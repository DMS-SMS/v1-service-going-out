class Student:
    def __init__(self,
                 student_uuid=None,
                 grade=None,
                 class_=None,
                 student_number=None,
                 name=None,
                 phone_number=None,
                 profile_uri=None
    ):
        self._stuent_uuid: str = student_uuid
        self._grade: int = grade
        self._class: int = class_
        self._student_number: int = student_number
        self._name: str = name
        self._phone_number: str = phone_number
        self._profile_uri: str = profile_uri
