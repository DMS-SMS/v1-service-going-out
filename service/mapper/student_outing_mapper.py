import time

from typing import List

from domain.entity import Outing
from proto.python.outing.outing_student_pb2 import StudentOuting


class StudentOutingMapper:
    def get_student_outings_mapper(self, outings: List["Outing"], start: int, end: int):
        outings_proto = []

        for outing in outings[start:end]:
            outing_proto = StudentOuting()

            outing_proto.place = outing.place
            outing_proto.reason = outing.reason
            outing_proto.start_time = int(time.mktime(outing.start_time.timetuple()))
            outing_proto.end_time = int(time.mktime(outing.end_time.timetuple()))
            outing_proto.situation = outing.situation
            outing_proto.status = outing.status

            outings_proto.append(outing_proto)

        return outings_proto
