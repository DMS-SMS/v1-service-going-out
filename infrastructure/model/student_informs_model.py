from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, ForeignKey, Enum

from infrastructure.extension import Base


class StudentInformsModel(Base):
    __tablename__ = "student_informs"

    student_uuid = Column(String(18), primary_key=True)
    grade = Column(Integer)
    class_ = Column(Integer)
    student_number = Column(Integer)
    name = Column(String(4))
    phone_number = Column(String(11))
    profile_uri = Column(String(150))

