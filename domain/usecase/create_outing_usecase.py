import datetime
import time
from domain.exception import OutingExist, Unauthorized
from domain.exception.bad_request import BadRequestException
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing
from domain.repository.parents_repository import ParentsRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository
from domain.service.pick_service import PickService
from domain.service.sms_service import SMSService
from domain.service.uuid_service import UuidService


class CreateOutingUseCase:
    def __init__(self, outing_repository, confirm_code_repository, student_repository, teacher_repository,
                 parents_repository, uuid_service, sms_service, pick_service):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository
        self.parents_repository: ParentsRepository = parents_repository
        self.uuid_service: UuidService = uuid_service
        self.sms_service: SMSService = sms_service
        self.pick_service: PickService = pick_service

    def run(self, uuid, situation, start_time, end_time, place, reason, x_request_id):
        student = self.student_repository.find_by_uuid(uuid, x_request_id)
        if student is None: raise Unauthorized()

        outing_uuid = self.uuid_service.generate_outing_uuid()

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

        self.outing_repository.save(
            Outing(
                outing_uuid=outing_uuid,
                student_uuid=uuid,
                status="1",
                situation=situation,
                start_time=start_datetime,
                end_time=end_datetime,
                place=place,
                reason=reason,
            )
        )

        self.pick_service.absent(student._student_number, start_datetime, end_datetime)

        return outing_uuid
