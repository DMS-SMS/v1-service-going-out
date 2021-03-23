import datetime

from const.code.python.outing import *

from domain.exception import Unauthorized, OutingFlowException
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository


class FinishGoOutUseCase:
    def __init__(self, outing_repository, student_repository, teacher_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository

    def run(self, uuid, outing_id, x_request_id):
        if self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id) is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing.status != "3":
            if outing.status == "0": raise OutingFlowException(code=not_approved_by_parents)
            if outing.status == "-1": raise OutingFlowException(code=rejected_by_parents)
            if outing.status == "1": raise OutingFlowException(code=not_approved_by_teacher)
            if outing.status == "-2": raise OutingFlowException(code=rejected_by_teacher)
            if outing.status == "2": raise OutingFlowException(code=not_out)
            else: raise OutingFlowException(code=already_finish_out)

        outing.status = "4"
        outing.arrival_time = datetime.datetime.now()
        self.outing_repository.save(outing)