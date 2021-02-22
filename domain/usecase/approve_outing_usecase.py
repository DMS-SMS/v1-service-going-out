from typing import List

from const.code.python.outing import *
from domain.entity import Outing, Student
from domain.entity.teacher import Teacher

from domain.exception import ConfirmCodeNotFound, OutingFlowException
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository
from domain.service.sms_service import SMSService


class ApproveOutingUseCase:
    def __init__(self, outing_repository, confirm_code_repository, student_repository, teacher_repository, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository
        self.sms_service: SMSService = sms_service

    def run(self, confirm_code, x_request_id):
        outing_id = self.confirm_code_repository.find_by_code(confirm_code)
        if outing_id == None: raise ConfirmCodeNotFound()

        outing: Outing = self.outing_repository.find_by_id(outing_id)
        if outing.status != "0": raise OutingFlowException(code=already_confirm_by_parents)

        outing.status = "1"
        self.outing_repository.save(outing)
        self.confirm_code_repository.delete_by_code(confirm_code)

        student: Student = self.student_repository.find_by_uuid(outing.student_uuid, x_request_id=x_request_id)
        teacher_uuids = self.teacher_repository.find_by_grade_and_group(
            outing.student_uuid, student._grade, student._group, x_request_id=x_request_id
        )

        if teacher_uuids:
            teacher: Teacher = self.teacher_repository.find_by_uuid(
                outing.student_uuid,
                teacher_uuids[0],
                x_request_id=x_request_id
            )

            self.sms_service.send(teacher._phone_number, f"{student._name}학생의 외출증이 허가 되었습니다.")
