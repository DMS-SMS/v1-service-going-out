import datetime
import time
from typing import Optional

from domain.entity.teacher import Teacher
from domain.exception import OutingExist, Unauthorized
from domain.exception.bad_request import BadRequestException
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing
from domain.repository.parents_repository import ParentsRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository
from domain.service.sms_service import SMSService
from domain.service.uuid_service import UuidService


class CreateOutingUseCase:
    def __init__(self, outing_repository, confirm_code_repository, student_repository, teacher_repository,
                 parents_repository, uuid_service, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository
        self.parents_repository: ParentsRepository = parents_repository
        self.uuid_service: UuidService = uuid_service
        self.sms_service: SMSService = sms_service

    def run(self, uuid, situation, start_time, end_time, place, reason, x_request_id):
        student = self.student_repository.find_by_uuid(uuid, x_request_id)
        if student is None: raise Unauthorized()

        outing_uuid = self.uuid_service.generate_outing_uuid()
        confirm_code = self.uuid_service.generate_confirm_code()

        time_now = time.time()

        start_datetime = datetime.datetime.fromtimestamp(start_time + 32400)
        start_date_one_day_later = datetime.datetime(start_datetime.year, start_datetime.month, start_datetime.day) \
                                   + datetime.timedelta(days=1)

        end_datetime = datetime.datetime.fromtimestamp(end_time + 32400)

        if end_datetime > start_date_one_day_later:
            raise BadRequestException(message="The end time cannot be the day after the start time.")
        if time_now > start_time:
            raise BadRequestException(message="The start time must be earlier than the current time.")
        if not datetime.datetime.fromtimestamp(time_now + 32400).date() == start_datetime.date():
            raise BadRequestException(message="Start time should be today.")
        if start_time >= end_time:
            raise BadRequestException(message="The start time cannot be bigger than the end time.")
        if self.outing_repository.find_by_student_uuid_and_time(uuid, start_time) is not None:
            raise OutingExist()

        parents = self.parents_repository.find_by_student_uuid(uuid, uuid, x_request_id)

        teacher_uuids = self.teacher_repository.find_by_grade_and_group(
            uuid, student._grade, student._group, x_request_id=x_request_id
        )

        teacher = None
        if teacher_uuids:
            teacher: Optional["Teacher"] = self.teacher_repository.find_by_uuid(
                uuid,
                teacher_uuids[0],
                x_request_id=x_request_id
            )

        self.outing_repository.save(
            Outing(
                outing_uuid=outing_uuid,
                student_uuid=uuid,
                status="1" if situation == "emergency" or not parents else "0",
                situation=situation,
                start_time=start_datetime,
                end_time=end_datetime,
                place=place,
                reason=reason,
            )
        )

        if parents and parents._phone_number:
            self.confirm_code_repository.save(outing_uuid, confirm_code)
            self.sms_service.send(
                parents._phone_number,
                self._generate_message(
                    student._name,
                    "parent.dsm-sms.com/",
                    confirm_code[8:],
                    True if situation == "emergency" else False
                ))

        elif teacher:
            self.sms_service.send(
                teacher._phone_number,
                f'''[{student._name} 학생 외출 신청]
                PC를 통해 아래 링크에 접속해 확인해주세요.
                
                teacher.dsm-sms.com'''
            )

        if situation == "emergency" and teacher:
            self.sms_service.send(
                teacher._phone_number,
                f'''[{student._name} 학생 긴급 외출 신청]
                PC를 통해 아래 링크에 접속해 확인해주세요.

                teacher.dsm-sms.com'''
            )


        return outing_uuid, parents

    def _generate_message(self, name, base_confirm_url, confirm_code, emergency=False) -> str:
        if emergency:
            return f'''[{name} 학생 긴급 외출]
            아래 링크를 통해 확인해주세요.
            
            {base_confirm_url}{confirm_code}'''

        return f'''[{name} 학생 외출 신청]
        아래 링크를 통해 확인해주세요.
        
        {base_confirm_url}{confirm_code}'''
