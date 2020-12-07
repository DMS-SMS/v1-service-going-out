import datetime

from domain.exception import OutingExist, Unauthorized
from domain.exception.bad_request import BadRequestException
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing
from domain.repository.student_repository import StudentRepository
from domain.service.sms_service import SMSService
from domain.service.uuid_service import UuidService


class CreateOutingUseCase:
    def __init__(self, outing_repository, confirm_code_repository, student_repository, uuid_service, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository
        self.student_repository: StudentRepository = student_repository
        self.uuid_service: UuidService = uuid_service
        self.sms_service: SMSService = sms_service

    def run(self, uuid, situation, start_time, end_time, place, reason, x_request_id):
        student = self.student_repository.find_by_uuid(uuid, x_request_id)
        if student is None: raise Unauthorized()

        outing_uuid = self.uuid_service.generate_outing_uuid()
        confirm_code = self.uuid_service.generate_confirm_code()

        if start_time >= end_time: raise BadRequestException()

        if self.outing_repository.find_by_student_uuid_and_end_time(uuid, end_time) is not None: raise OutingExist()

        self.outing_repository.save(
            Outing(
                outing_uuid=outing_uuid,
                student_uuid=uuid,
                status="1" if situation == "EMERGENCY" else "0",
                situation=situation,
                start_time=datetime.datetime.fromtimestamp(start_time),
                end_time=datetime.datetime.fromtimestamp(end_time),
                place=place,
                reason=reason,
            )
        )

        self.confirm_code_repository.save(outing_uuid, confirm_code)
        self.sms_service.send("number", self._generate_message(
            student._name,
            datetime.datetime.fromtimestamp(start_time),
            datetime.datetime.fromtimestamp(end_time),
            reason,
            place,
            "http://{BASEURL}",
            confirm_code
        ), x_request_id)

        return outing_uuid

    def _generate_message(self, name, start_time, end_time, reason, place, base_confirm_url,confirm_code) -> str:
        return f"{name}학생이 {start_time}~{end_time}까지의 외출을 신청하였습니다.\n" \
               f" 사유 : {reason} \n " \
               f" 장소 : {place} \n" \
               f" 허가 : {base_confirm_url}/confirm=?{confirm_code} \n" \
               f" 거부 : {base_confirm_url}/confirm=?{confirm_code}"