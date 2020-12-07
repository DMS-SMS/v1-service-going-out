from const.code.python.outing import *

from domain.exception import Unauthorized, OutingNotFound, OutingFlowException
from domain.repository.outing_repository import OutingRepository
from domain.repository.teacher_repository import TeacherRepository


class CertifyOutingUseCase:
    def __init__(self, outing_repository, teacher_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.teacher_repository: TeacherRepository = teacher_repository

    def run(self, uuid, outing_id, x_request_id):
        if self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id) is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()
        if outing.status != "4":
            if outing.status == "0": OutingFlowException(code=not_approved_by_parents)
            if outing.status == "-1": OutingFlowException(code=rejected_by_parents)
            if outing.status == "1": OutingFlowException(code=not_approved_by_teacher)
            if outing.status == "-2": OutingFlowException(code=rejected_by_teacher)
            if outing.status == "2": OutingFlowException(code=not_out)
            if outing.status == "3": OutingFlowException(code=not_finish_out)
            if outing.status == "5": OutingFlowException(code=already_confirm_out_by_teacher)
            else: OutingFlowException()

        outing.status = "5"
        outing.accepted_teacher = uuid
        self.outing_repository.save(outing)