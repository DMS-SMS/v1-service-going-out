from typing import List

from domain.entity.outing import Outing

from domain.repository.student_repository import StudentRepository
from domain.repository.outing_repository import OutingRepository

from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl

from proto.python.outing.outing_student_pb2 import StudentOuting
from proto.python.outing.outing_teacher_pb2 import Outing as TeacherOuting


def create_outing_mapper(request):
    entity: Outing = Outing(
        student_uuid=request.uuid,
        situation=request.situation,
        date=request.date,
        start_time=request.start_time,
        end_time=request.end_time,
        place=request.place,
        reason=request.reason,
    )
    return entity


def get_outings_mapper(outing_entities: List["Outing"]) -> List["StudentOuting"]:
    outings = list()

    for outing_entity in outing_entities:
        outing = StudentOuting()

        outing.place = outing_entity._place
        outing.reason = outing_entity._reason
        outing.date = outing_entity._date
        outing.start_time = outing_entity._start_time
        outing.end_time = outing_entity._end_time
        outing.situation = outing_entity._situation
        outing.status = outing_entity._status

        outings.append(outing)

    return outings


def get_outings_for_teacher_mapper(
    outing_entities: List["Outing"],
) -> List["TeacherOuting"]:
    outings = list()
    student_repository: StudentRepository = StudentRepositoryImpl()
    outing_repository: OutingRepository = OutingRepositoryImpl()

    for outing_entity in outing_entities:
        outing = TeacherOuting()
        student = student_repository.get_student_by_uuid(outing_entity._student_uuid)
        is_late = outing_repository.get_is_late(outing_entity._outing_uuid)

        outing.name = student._name
        outing.grade = student._grade
        outing.group = student._group
        outing.number = student._student_number

        outing.place = outing_entity._place
        outing.reason = outing_entity._reason
        outing.date = outing_entity._date
        outing.start_time = outing_entity._start_time
        outing.end_time = outing_entity._end_time
        outing.situation = outing_entity._situation
        outing.status = outing_entity._status

        if is_late is not None:
            outing.is_late = is_late

        outings.append(outing)

    return outings
