from domain.repository import OutingRepository, StudentRepository
from domain.service.sms_service import SMSService


class CreateOutingUseCase:
    def __init__(self, outing_repository, student_repository, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.sms_service: SMSService = sms_service

    def run(self, entity):
        o_id: str = self.outing_repository.save_and_get_oid(entity)
        o_code: str = self.outing_repository.set_and_get_parents_outing_code(o_id)
        self.sms_service.send_to_parents(o_id, o_code)

        return o_id
