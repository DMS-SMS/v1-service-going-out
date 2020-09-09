class Outing:
    def __init__(self,
                 outing_uuid,
                 student_uuid,
                 status,
                 situation,
                 accept_teacher,
                 date,
                 start_time,
                 end_time,
                 place,
                 reason,
                 arrival_date,
                 arrival_time):
        self._outing_uuid = outing_uuid
        self._student_uuid = student_uuid
        self._status = status
        self._situation = situation
        self._accept_teacher = accept_teacher
        self._date = date
        self._start_time = start_time
        self._end_time = end_time
        self._place = place
        self._reason = reason
        self._arrival_date = arrival_date
        self._arrival_time = arrival_time