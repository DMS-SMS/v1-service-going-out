import time

from typing import List

from domain.entity import Outing
from domain.repository.student_repository import StudentRepository
from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from proto.python.outing.outing_teacher_pb2 import Outing as OutingProto


class TeacherOutingMapper:
    def get_outings_for_teacher_mapper(self, outings: List["Outing"], x_request_id, start, count):
        outings_proto = []
        student_repository: StudentRepository = StudentRepositoryImpl()

        for outing in outings[start:start+count]:
            outing_proto = OutingProto()
            student = student_repository.find_by_uuid(outing.student_uuid, x_request_id)

            outing_proto.outing_id = outing.outing_uuid
            outing_proto.name = student._name
            outing_proto.grade = student._grade
            outing_proto.group = student._group
            outing_proto.number = student._student_number

            outing_proto.place = outing.place
            outing_proto.reason = outing.reason
            outing_proto.start_time = int(time.mktime(outing.start_time.timetuple()))-32400
            outing_proto.end_time = int(time.mktime(outing.end_time.timetuple()))-32400
            outing_proto.situation = outing.situation
            outing_proto.status = outing.status
            outing_proto.arrival_time = outing.arrival_time

            if int(outing.status) >= 4:
                if outing.arrival_time > outing.end_time: outing_proto.is_late = True
                else: outing_proto.is_late = False

            outings_proto.append(outing_proto)

        return outings_proto