from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.extension import Base


class OutingModel(Base):
    __tablename__ = "outings"

    uuid = Column(String(20), primary_key=True)
    student_uuid = Column(
        String(18), ForeignKey("student_informs.student_uuid"), nullable=False
    )
    status = Column(Enum("-2", "-1", "0", "1", "2", "3", "4", "5"), nullable=False)
    # 0: 외출증 생성 , 1: 학부모 승인, -1: 학부모 거부, 2: 담임 확인, -2: 담임 거부, 3: 외출, 4: 외출 종료, 5: 사후제출
    situation = Column(Enum("NORMAL", "EMERGENCY"), nullable=False)
    date = Column(DateTime, nullable=False)
    start_time = Column(String(4), nullable=False)
    end_time = Column(String(4), nullable=False)
    place = Column(String(50), nullable=False)
    reason = Column(String(150), nullable=False)

    arrival_date = Column(DateTime, nullable=True)
    arrival_time = Column(String(4), nullable=True)
    accepted_teacher = Column(Integer, nullable=True)

    student = relationship("StudentInformsModel")
