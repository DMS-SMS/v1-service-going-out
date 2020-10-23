from domain.entity.outing import Outing
from domain.entity.student import Student
from domain.service.sms_service import SMSService

from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl
from infrastructure.implementation.repository.student_repository_impl import StudentRepositoryImpl
from infrastructure.redis.redis_handler import RedisHandler


class SMSServiceImpl(SMSService):
    def __init__(self):
        self.redis = RedisHandler()
        self.outing_repository = OutingRepositoryImpl()
        self.student_repository = StudentRepositoryImpl()

    def send_to_parents(self, outing_id: str, confirm_code: str, x_request_id: str):
        outing: Outing = self.outing_repository.find_by_id(outing_id)
        student: Student = self.student_repository.find_by_uuid(
            outing.student_uuid,
            x_request_id
        )

        student_name = student._name
        time = outing.start_time
        e_time = outing.end_time

        print("--------[문자서비스로 갈 내용]-------")

        print(
            f"{student_name} 학생이 외출을 신청하였습니다.\n 날짜 : {e_time}\n 시간 : {time}\n 장소 : {outing.place}\n 사유 : {outing.reason}\n"
        )
        if outing.situation == "EMERGENCY":
            print(f"위 외출은 긴급 상황으로 판단되어 학부모에게 외출 확인을 받지 않습니다.")
            self.redis.delete_by_key(confirm_code)
        else:
            print(f"외출 허가 : http://mallycrip/approve/{confirm_code}")
            print(f"외출 거부 : http://mallycrip/reject/{confirm_code}")
