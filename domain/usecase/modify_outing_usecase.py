import datetime

from domain.exception import Unauthorized, OutingNotFound, OutingFlowException
from domain.repository.outing_repository import OutingRepository
from domain.repository.teacher_repository import TeacherRepository


class ModifyOutingUseCase:
    def __init__(self, outing_repository, teacher_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.teacher_repository: TeacherRepository = teacher_repository

    def execute(self, uuid, outing_id, end_time, x_request_id):
        teacher = self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id)
        if teacher is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()

        if outing.status != "1": raise OutingFlowException(code=-2400)

        outing.end_time = datetime.datetime.fromtimestamp(end_time + 32400)
        self.outing_repository.save(outing)
