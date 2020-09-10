from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, ForeignKey, Enum

from infrastructure.extension import Base


class OutingModel(Base):
    __tablename__ = "outings"

    uuid = Column(String(20), primary_key=True)
    student_uuid = Column(String(18), nullable=False)
    status = Column(Enum("0", "1", "2", "3", "4", "5"), nullable=False)
    situation = Column(Enum("NORMAL", "EMERGENCY"), nullable=False)
    date = Column(DateTime, nullable=False)
    start_time = Column(String(4), nullable=False)
    end_time = Column(String(4), nullable=False)
    place = Column(String(50), nullable=False)
    reason = Column(String(150), nullable=False)

    arrival_date = Column(DateTime, nullable=True)
    arrival_time = Column(String(4), nullable=True)
    accepted_teacher = Column(Integer, nullable=True)


