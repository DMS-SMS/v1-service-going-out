from const.code.python.outing import *

from domain.exception import Unauthorized, OutingFlowException, OutingNotFound
from domain.repository.outing_repository import OutingRepository
from domain.repository.teacher_repository import TeacherRepository


class ApproveOutingTeacherUseCase:
    def __init__(self, outing_repository, teacher_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.teacher_repository: TeacherRepository = teacher_repository

    def run(self, uuid, outing_id, x_request_id):
        if self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id) is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()
        if outing.status != "1":
            if outing.status == "0": raise OutingFlowException(code=not_approved_by_parents)
            if outing.status == "-1": raise OutingFlowException(code=rejected_by_parents)
            if int(outing.status) > 1: raise OutingFlowException(code=already_confirm_by_teacher)

        outing.status = "2"

        self.outing_repository.save(outing)