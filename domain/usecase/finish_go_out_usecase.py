import datetime

from domain.exception import Unauthorized, ConfirmFailed
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository


class FinishGoOutUseCase:
    def __init__(self, outing_repository, student_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository= student_repository

    def run(self, uuid, outing_id, x_request_id):
        if self.student_repository.find_by_uuid(uuid, x_request_id) is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing.student_uuid != uuid: raise Unauthorized()
        if outing.status != "3": raise ConfirmFailed()

        outing.status = "4"
        outing.arrival_time = datetime.datetime.now()
        self.outing_repository.save(outing)