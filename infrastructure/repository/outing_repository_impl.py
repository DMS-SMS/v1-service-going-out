import time

from datetime import datetime
from sqlalchemy import and_, func
from typing import List, Optional

from infrastructure.service.auth_service import AuthService
from infrastructure.model import OutingModel
from infrastructure.extension import db_session
from infrastructure.util.random_key import generate_outing_uuid, generate_random_key
from infrastructure.mapper.outing_repository_mapper import (
    create_outing_mapper,
    get_outing_mapper,
    get_outings_mapper,
)
from infrastructure.exception import (
    OutingExist,
    NotFound,
    NotApprovedByParents,
    AlreadyApprovedByParents,
    StillOut,
)
from infrastructure.service.redis_service import (
    get_oid_by_parents_outing_code,
    save_parents_outing_code,
    delete_outing_code,
)

from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing


class OutingRepositoryImpl(OutingRepository):
    @classmethod
    def save_and_get_oid(cls, outing: Outing) -> str:
        outing_uuid = generate_outing_uuid()

        while (
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == outing_uuid)
            .first()
        ):
            outing_uuid = generate_outing_uuid()

        if (
            db_session.query(OutingModel)
            .filter(
                and_(
                    OutingModel.student_uuid == func.binary(outing._student_uuid),
                    OutingModel.date == outing._date,
                )
            )
            .all()
        ):
            raise OutingExist

        db_session.add(create_outing_mapper(outing, outing_uuid))
        db_session.commit()
        return outing_uuid

    @classmethod
    def set_and_get_parents_outing_code(cls, oid: str) -> str:
        o_code = generate_random_key(20)

        while get_oid_by_parents_outing_code(o_code):
            o_code = generate_random_key(20)

        save_parents_outing_code(oid, o_code)

        return o_code

    @classmethod
    def get_outing_by_oid(cls, oid: str) -> Outing:
        outing = (
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing:
            raise NotFound

        return get_outing_mapper(outing)

    @classmethod
    def get_outings_by_student_id(cls, sid: str) -> List["Outing"]:
        outings = (
            db_session.query(OutingModel)
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
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )
        if not outing.status == "1":
            raise NotApprovedByParents

        outing.status = "2"
        db_session.commit()

    @classmethod
    def approve_by_outing_for_parents(cls, o_code: str) -> None:
        oid = get_oid_by_parents_outing_code(o_code)

        outing = (
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing:
            raise NotFound
        if not outing.status == "0":
            raise AlreadyApprovedByParents

        outing.status = "1"
        db_session.commit()

        delete_outing_code(o_code)

    @classmethod
    def reject_by_outing_for_teacher(cls, oid: str) -> None:
        outing = (
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "1":
            raise NotApprovedByParents

        outing.status = "-2"
        db_session.commit()

    @classmethod
    def reject_by_outing_for_parents(cls, o_code):
        oid = get_oid_by_parents_outing_code(o_code)

        outing = (
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing:
            raise NotFound
        if not outing.status == "0":
            raise AlreadyApprovedByParents

        outing.status = "-1"
        db_session.commit()

        delete_outing_code(o_code)

    @classmethod
    def certify_by_outing_for_teacher(cls, oid) -> None:
        outing = (
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "4":
            raise StillOut

        outing.status = "5"
        db_session.commit()

    @classmethod
    def get_outings_with_filter(cls, status, grade, group) -> List["Outing"]:
        auth_service = AuthService()
        query = db_session.query(OutingModel)
        if status:
            query = query.filter(OutingModel.status == func.binary(status))

        outings = query.order_by(OutingModel.date.desc()).all()

        if grade or group:
            for outing in outings[:]:
                student = auth_service.get_student_inform(outing.student_uuid, outing.student_uuid)
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
            db_session.query(OutingModel)
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
            db_session.query(OutingModel)
            .filter(OutingModel.uuid == func.binary(oid))
            .first()
        )

        if not outing.status == "2":
            raise StillOut

        outing.status = "3"
        db_session.commit()

    @classmethod
    def finish_go_out(cls, oid) -> None:
        outing = (
            db_session.query(OutingModel)
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

        db_session.commit()
