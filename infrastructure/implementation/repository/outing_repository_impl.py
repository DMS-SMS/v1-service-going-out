import time

from datetime import datetime
from sqlalchemy import and_, func
from typing import List, Optional

from infrastructure.auth.auth_handler import AuthHandler
from infrastructure.mysql.model.outing_model import OutingModel
from infrastructure.mysql.mysql_handler import MySQLHandler
from infrastructure.util.random_key import generate_outing_uuid, generate_random_key
from infrastructure.implementation.repository.mapper.student_repository_mapper import (
    get_student_mapper,

)
from infrastructure.implementation.repository.mapper.outing_repository_mapper import (
    get_outing_mapper,
    get_outings_mapper,
    create_outing_mapper
)
from domain.exception import (
    OutingExist,
    NotFound,
    NotApprovedByParents,
    AlreadyApprovedByParents,
    StillOut,
)
from infrastructure.redis.redis_handler import RedisHandler

from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing


class OutingRepositoryImpl(OutingRepository):
    sql = MySQLHandler()
    redis = RedisHandler()
    auth = AuthHandler()

    @classmethod
    def save_and_get_oid(cls, outing: Outing) -> str:
        outing_uuid = generate_outing_uuid()

        while (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == outing_uuid)
            .first()
        ):
            outing_uuid = generate_outing_uuid()

        if (
            cls.sql.db_session.query(OutingModel)
            .filter(
                and_(
                    OutingModel.student_uuid == func.binary(outing._student_uuid),
                    OutingModel.date == outing._date,
                )
            )
            .all()
        ):
            raise OutingExist

        cls.sql.db_session.add(create_outing_mapper(outing, outing_uuid))
        cls.sql.db_session.commit()
        return outing_uuid

    @classmethod
    def set_and_get_parents_outing_code(cls, oid: str) -> str:
        o_code = generate_random_key(20)

        while cls.redis.get_oid_by_parents_outing_code(o_code):
            o_code = generate_random_key(20)

        cls.redis.save_parents_outing_code(oid, o_code)

        return o_code

    @classmethod
    def get_outing_by_oid(cls, oid: str) -> Outing:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing:
            raise NotFound

        return get_outing_mapper(outing)

    @classmethod
    def get_outings_by_student_id(cls, sid: str) -> List["Outing"]:
        outings = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.student_uuid == func.binary(sid))
            .order_by(OutingModel.date.desc())
            .all()
        )

        if not outings:
            raise NotFound

        return get_outings_mapper(outings)

    @classmethod
    def approve_by_outing_for_teacher(cls, oid: str) -> None:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )
        if not outing.status == "1":
            raise NotApprovedByParents

        outing.status = "2"
        cls.sql.db_session.commit()

    @classmethod
    def approve_by_outing_for_parents(cls, o_code: str) -> None:
        oid = cls.redis.get_oid_by_parents_outing_code(o_code)

        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing:
            raise NotFound
        if not outing.status == "0":
            raise AlreadyApprovedByParents

        outing.status = "1"
        cls.sql.db_session.commit()

        cls.redis.delete_outing_code(o_code)

    @classmethod
    def reject_by_outing_for_teacher(cls, oid: str) -> None:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "1":
            raise NotApprovedByParents

        outing.status = "-2"
        cls.sql.db_session.commit()

    @classmethod
    def reject_by_outing_for_parents(cls, o_code):
        oid = cls.redis.get_oid_by_parents_outing_code(o_code)

        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing:
            raise NotFound
        if not outing.status == "0":
            raise AlreadyApprovedByParents

        outing.status = "-1"
        cls.sql.db_session.commit()

        cls.redis.delete_outing_code(o_code)

    @classmethod
    def certify_by_outing_for_teacher(cls, oid) -> None:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "4":
            raise StillOut

        outing.status = "5"
        cls.sql.db_session.commit()

    @classmethod
    def get_outings_with_filter(cls, status, grade, group) -> List["Outing"]:
        query = cls.sql.db_session.query(OutingModel)
        if status:
            query = query.filter(OutingModel.status == func.binary(status))

        outings = query.order_by(OutingModel.date.desc()).all()

        if grade or group:
            for outing in outings[:]:
                student = cls.auth.get_student_inform(outing.student_uuid, outing.student_uuid)
                if grade and group:
                    if student.Grade != grade: outings.remove(outing)
                    elif student.Group != group: outings.remove(outing)
                elif grade:
                    if student.Grade != grade: outings.remove(outing)
                else:
                    if student.Group != group: outings.remove(outing)


        return get_outings_mapper(outings)

    @classmethod
    def get_is_late(cls, oid) -> Optional[bool]:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if outing.arrival_time is None and outing.arrival_date is None:
            return None
        if outing.arrival_date == outing.date and int(outing.arrival_time) < int(
            outing.end_time
        ):
            return False
        return True

    @classmethod
    def go_out(cls, oid) -> None:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "2":
            raise StillOut

        outing.status = "3"
        cls.sql.db_session.commit()

    @classmethod
    def finish_go_out(cls, oid) -> None:
        outing = (
            cls.sql.db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "3":
            raise StillOut

        now = time.gmtime(time.time())

        outing.status = "4"

        outing.arrival_date = datetime(
            year=now.tm_year, month=now.tm_mon, day=now.tm_mday
        )
        outing.arrival_time = str(now.tm_hour).zfill(2) + str(now.tm_min).zfill(2)

        cls.sql.db_session.commit()
