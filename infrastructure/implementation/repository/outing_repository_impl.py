import datetime

from typing import List

from sqlalchemy import func, and_

from domain.entity import Outing
from domain.repository.outing_repository import OutingRepository
from infrastructure.mysql import MySQLHandler
from infrastructure.open_tracing import open_tracing
from infrastructure.open_tracing.open_tracing_handler import trace_service


class OutingRepositoryImpl(OutingRepository):
    def __init__(self):
        self.sql = MySQLHandler()

    @trace_service("SQL (save)", open_tracing)
    def save(self, outing: Outing):
        self.sql._db_session.add(outing)
        self.sql._db_session.commit()
        self.sql._db_session.close()

    @trace_service("SQL (save)", open_tracing)
    def find_all_by_status(self, status: str) -> List["Outing"]:
        query = self.sql._db_session.query(Outing)
        if status: query = query.filter(Outing.status == status)
        model = query.all()
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model

    @trace_service("SQL (find)", open_tracing)
    def find_all_by_student_uuid(self, student_id):
        model = self.sql._db_session.query(Outing) \
            .filter(Outing.student_uuid == func.binary(student_id)) \
            .order_by(Outing.end_time.desc()).all()
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model

    @trace_service("SQL (find)", open_tracing)
    def find_all_by_student_uuid_and_status(self, student_uuid, status) -> List["Outing"]:
        query = self.sql._db_session.query(Outing).filter(Outing.student_uuid == func.binary(student_uuid))
        if status: query = query.filter(Outing.status == status)
        model = query.all()
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model

    @trace_service("SQL (find)", open_tracing)
    def find_by_id(self, id: str) -> Outing:
        model = (self.sql._db_session.query(Outing)
                 .filter(Outing.outing_uuid == func.binary(id)).first())
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model

    @trace_service("SQL (find)", open_tracing)
    def find_by_student_uuid_and_time(self, student_uuid: str, time: float) -> Outing:
        generated_time = datetime.datetime.fromtimestamp(time + 32400)
        current_day = datetime.datetime(generated_time.year, generated_time.month, generated_time.day)
        model = (self.sql._db_session.query(Outing)
                 .filter(Outing.student_uuid == func.binary(student_uuid))
                 .filter(and_(Outing.start_time >= current_day,
                              Outing.end_time < current_day + datetime.timedelta(days=1))).first())
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model

    @trace_service("SQL (find)", open_tracing)
    def find_all_by_status_and_term(self, status: str, start_time: str, end_time: int):
        generated_start_time = datetime.datetime.fromtimestamp(start_time + 32400)
        generated_end_time = datetime.datetime.fromtimestamp(end_time + 32400)

        model = (self.sql._db_session.query(Outing)
                 .filter(Outing.status == func.binary(status))
                 .filter(and_(Outing.start_time >= generated_start_time,
                              Outing.start_time <= generated_end_time)).all())
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model

    @trace_service("SQL (find)", open_tracing)
    def find_all_by_student_uuid_and_status_and_term(
            self, student_uuid: str, status: str, start_time: int, end_time: int):
        generated_start_time = datetime.datetime.fromtimestamp(start_time + 32400)
        generated_end_time = datetime.datetime.fromtimestamp(end_time + 32400)

        model = (self.sql._db_session.query(Outing)
                 .filter(Outing.status == func.binary(status))
                 .filter(Outing.student_uuid == func.binary(student_uuid))
                 .filter(and_(Outing.start_time >= generated_start_time,
                              Outing.start_time <= generated_end_time)).all())
        self.sql._db_session.commit()
        self.sql._db_session.close()
        return model
