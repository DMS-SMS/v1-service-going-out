from typing import Optional


class Outing:
    def __init__(self,
                 outing_uuid=None,
                 student_uuid=None,
                 status=None,
                 situation=None,
                 accept_teacher=None,
                 date=None,
                 start_time=None,
                 end_time=None,
                 place=None,
                 reason=None,
                 arrival_date=None,
                 arrival_time=None):
        self._outing_uuid : str = outing_uuid
        self._student_uuid : str = student_uuid
        self._status : str = status
        self._situation : str = situation
        self._accept_teacher : Optional[int] = accept_teacher
        self._date : str = date
        self._start_time : str = start_time
        self._end_time : str = end_time
        self._place : str = place
        self._reason : str = reason
        self._arrival_date : Optional[str] = arrival_date
        self._arrival_time : Optional[int] = arrival_time