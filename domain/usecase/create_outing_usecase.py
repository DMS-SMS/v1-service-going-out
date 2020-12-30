import datetime
import time

from domain.exception import OutingExist, Unauthorized
from domain.exception.bad_request import BadRequestException
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing
from domain.repository.parents_repository import ParentsRepository
from domain.repository.student_repository import StudentRepository
from domain.service.sms_service import SMSService
from domain.service.uuid_service import UuidService


class CreateOutingUseCase:
    def __init__(self, outing_repository, confirm_code_repository, student_repository, parents_repository, uuid_service, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository
        self.student_repository: StudentRepository = student_repository
        self.parents_repository: ParentsRepository = parents_repository
        self.uuid_service: UuidService = uuid_service
        self.sms_service: SMSService = sms_service

    def run(self, uuid, situation, start_time, end_time, place, reason, x_request_id):
        student = self.student_repository.find_by_uuid(uuid, x_request_id)
        if student is None: raise Unauthorized()

        outing_uuid = self.uuid_service.generate_outing_uuid()
        confirm_code = self.uuid_service.generate_confirm_code()

        start_datetime = datetime.datetime.fromtimestamp(start_time+32400)
        start_date_one_day_later = datetime.datetime(start_datetime.year, start_datetime.month, start_datetime.day) \
                     + datetime.timedelta(days=1)


        if datetime.datetime.fromtimestamp(end_time+32400) > start_date_one_day_later: raise BadRequestException()
        if time.time() > start_time: raise BadRequestException()
        if time.time() + 604800 <= start_time: raise BadRequestException()
        if start_time >= end_time: raise BadRequestException()
        if self.outing_repository.find_by_student_uuid_and_time(uuid, start_time) is not None: raise OutingExist()

        self.outing_repository.save(
            Outing(
                outing_uuid=outing_uuid,
                student_uuid=uuid,
                status="1" if situation == "EMERGENCY" else "0",
                situation=situation,
                start_time=datetime.datetime.fromtimestamp(start_time+32400),
                end_time=datetime.datetime.fromtimestamp(end_time+32400),
                place=place,
                reason=reason,
            )
        )


        self.confirm_code_repository.save(outing_uuid, confirm_code)
        self.sms_service.send(
            self.parents_repository.find_by_student_uuid(uuid, uuid, x_request_id)._phone_number,
            self._generate_message(
                student._name,
                "54.180.165.105/check",
                confirm_code,
                True if situation == "EMERGENCY" else False
            ),
            x_request_id)

        return outing_uuid

    def _generate_message(self, name, base_confirm_url, confirm_code, emergency=False) -> str:
        if emergency: return f"{name}학생 긴급 외출 신청\n" \
               f" 확인 : {base_confirm_url}?c={confirm_code}"

        return f"{name}학생 외출 신청\n" \
               f" 확인 : {base_confirm_url}?c={confirm_code}"