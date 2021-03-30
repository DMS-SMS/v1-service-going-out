from typing import Optional

from const.code.python.outing import *

from domain.exception import Unauthorized, OutingFlowException, OutingNotFound
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository
from domain.service.sms_service import SMSService


class ApproveOutingTeacherUseCase:
    def __init__(self, outing_repository, student_repository, teacher_repository, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository
        self.sms_service: SMSService = sms_service

    def run(self, uuid, outing_id, x_request_id):
        teacher = self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id)
        if teacher is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()
        if outing.status != "1":
            if outing.status == "0": raise OutingFlowException(code=not_approved_by_parents)
            if outing.status == "-1": raise OutingFlowException(code=rejected_by_parents)
            if int(outing.status) > 1:
                raise OutingFlowException(code=already_confirm_by_teacher)
            else:
                raise OutingFlowException()

        outing.status = "2"

        self.outing_repository.save(outing)

        student = self.student_repository.find_by_uuid(outing.student_uuid, x_request_id=x_request_id)

        self.sms_service.send(
            student._phone_number,
            f"[{student._name} 학생 외출증 승인]\n"
            "정문에서 '모바일 > 오늘의 외출증'을 보여드린 후 시작해주세요."
        )

        if teacher._group != student._group or teacher._grade != teacher._grade:
            teacher_uuids = self.teacher_repository.find_by_grade_and_group(
                uuid, student._grade, student._group, x_request_id=x_request_id
            )

            if teacher_uuids:
                homeroom_teacher: Optional["Teacher"] = self.teacher_repository.find_by_uuid(
                    uuid,
                    teacher_uuids[0],
                    x_request_id=x_request_id
                )

                self.sms_service.send(
                    homeroom_teacher._phone_number,
                    f"[{student._name} 학생 외출증 승인]\n"
                    f"{teacher._name}선생님에 의해 외출증이 승인 되었습니다."
                )