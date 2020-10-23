from domain.exception import Unauthorized, ConfirmFailed, OutingNotFound
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
        if outing.status != "4": raise ConfirmFailed()

        outing.status = "5"
        outing.accepted_teacher = uuid
        self.outing_repository.save(outing)