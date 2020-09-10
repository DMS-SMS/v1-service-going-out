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
        self._stuent_uuid = student_uuid
        self._grade = grade
        self._class = class_
        self._student_number = student_number
        self._name = name
        self._phone_number = phone_number
        self._profile_uri = profile_uri
