from domain.entity.outing import Outing
from domain.entity.student import Student

from infrastructure.repository import OutingRepositoryImpl, StudentRepositoryImpl
from infrastructure.util.redis_service import delete_outing_code


class SMSService:
    def send_to_parents(self, oid: str, o_code: str):
        outing: Outing = OutingRepositoryImpl().get_outing_by_oid(oid)
        student: Student = StudentRepositoryImpl().get_student_by_uuid(
            outing._student_uuid
        )

        student_name = student._name
        date = str(outing._date)[0:10]
        time = str(
            f"{outing._start_time[0:2]}:{outing._start_time[2:4]} ~ {outing._end_time[0:2]}:{outing._end_time[2:4]}"
        )

        print("--------[문자서비스로 갈 내용]-------")

        print(
            f"{student_name} 학생이 외출을 신청하였습니다.\n 날짜 : {date}\n 시간 : {time}\n 장소 : {outing._place}\n 사유 : {outing._reason}\n"
        )
        if outing._situation == "EMERGENCY":
            print(f"위 외출은 긴급 상황으로 판단되어 학부모에게 외출 확인을 받지 않습니다.")
            delete_outing_code(o_code)
        else:
            print(f"외출 허가 : http://mallycrip/approve/{o_code}")
            print(f"외출 거부 : http://mallycrip/reject/{o_code}")
