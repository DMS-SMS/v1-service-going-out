import time

from const.code.python.outing import *

from datetime import datetime
from domain.exception import Unauthorized, OutingNotFound, OutingFlowException
from domain.repository.outing_repository import OutingRepository
from domain.repository.parents_repository import ParentsRepository
from domain.repository.student_repository import StudentRepository
from domain.service.pick_service import PickService
from domain.service.sms_service import SMSService


class GoOutUseCase:
    def __init__(self, outing_repository, student_repository, parents_repository, sms_service, pick_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.parents_repository: ParentsRepository = parents_repository
        self.sms_service: SMSService = sms_service
        self.pick_service: PickService = pick_service

    def run(self, uuid, outing_id, x_request_id):
        student = self.student_repository.find_by_uuid(uuid, x_request_id)
        if student is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()

        if outing.student_uuid != uuid: raise Unauthorized()
        if outing.status != "2":
            if outing.status == "0": raise OutingFlowException(code=not_approved_by_parents)
            if outing.status == "-1": raise OutingFlowException(code=rejected_by_parents)
            if outing.status == "1": raise OutingFlowException(code=not_approved_by_teacher)
            if outing.status == "-2": raise OutingFlowException(code=rejected_by_teacher)
            if outing.status == "3": raise OutingFlowException(code=already_out)
            else: raise OutingFlowException()

        outing.status = "3"
        self.outing_repository.save(outing)

        parents = self.parents_repository.find_by_student_uuid(uuid, uuid, x_request_id)

        self.sms_service.send(
            parents._phone_number,
            f"[{student._name} 학생 외출 시작]\n"
            f"{student._name}학생이 외출을 시작하였습니다."
        )

        self.pick_service.absent(student._student_number, datetime.fromtimestamp(time.time()), outing.end_time)
