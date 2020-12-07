from const.code.python.outing import *

from domain.exception import Unauthorized, OutingNotFound, OutingFlowException
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository


class GoOutUseCase:
    def __init__(self, outing_repository, student_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository

    def run(self, uuid, outing_id, x_request_id):
        if self.student_repository.find_by_uuid(uuid, x_request_id) is None: raise Unauthorized()

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