from const.code.python.outing import *

from domain.exception import Unauthorized, OutingNotFound, OutingFlowException
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository
from domain.service.sms_service import SMSService


class RejectOutingTeacherUseCase:
    def __init__(self, outing_repository, student_repository, teacher_repository, sms_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository
        self.sms_service: SMSService = sms_service

    def run(self, uuid, outing_id, x_request_id):
        if self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id) is None: raise Unauthorized()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing is None: raise OutingNotFound()

        if outing.status != "1":
            if outing.status == "0": raise OutingFlowException(code=not_approved_by_parents)
            if outing.status == "-1":
                raise OutingFlowException(code=rejected_by_parents)
            else:
                raise OutingFlowException(code=already_confirm_by_teacher)

        outing.status = "-2"
        self.outing_repository.save(outing)

        student = self.student_repository.find_by_uuid(outing.student_uuid, x_request_id=x_request_id)

        self.sms_service.send(
            student._phone_number,
            f"[{student._name} 학생 외출 거절]\n\n"
            
            "선생님에 의해 거절 되었습니다.\n"
            "* 당일에는 추가 외출 신청 불가"
        )
