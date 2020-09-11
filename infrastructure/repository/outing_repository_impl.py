from sqlalchemy import and_
from typing import List

from infrastructure.model import OutingModel
from infrastructure.extension import db_session
from infrastructure.util.random_key import random_key_generate
from infrastructure.mapper.outing_repository_mapper import create_outing_mapper, get_outing_mapper, get_outings_mapper
from infrastructure.exception import OutingExist, NotFound
from infrastructure.util.redis_service import get_oid_by_parents_outing_code, save_parents_outing_code

from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing


class OutingRepositoryImpl(OutingRepository):
    @classmethod
    def save_and_get_oid(cls, outing: Outing) -> str:
        outing_uuid = random_key_generate(20)

        while db_session.query(OutingModel).filter(OutingModel.uuid == outing_uuid).first():
            outing_uuid = random_key_generate(20)

        if db_session.query(OutingModel)\
            .filter(and_(OutingModel.student_uuid == outing._student_uuid,
                         OutingModel.date == outing._date)).all(): raise OutingExist


        db_session.add(create_outing_mapper(outing, outing_uuid))
        db_session.commit()
        return outing_uuid

    @classmethod
    def set_and_get_parents_outing_code(cls, oid: str) -> str:
        o_code = random_key_generate(20)

        while get_oid_by_parents_outing_code(o_code):
            o_code = random_key_generate(20)

        save_parents_outing_code(oid, o_code)

        return o_code

    @classmethod
    def get_outing_by_oid(cls, oid: str) -> Outing:
        return get_outing_mapper(db_session.query(OutingModel).filter(OutingModel.uuid == oid).first())

    @classmethod
    def get_outings_by_student_id(cls, sid: str) -> List["Outing"]:
        outings = get_outings_mapper(db_session.query(OutingModel).filter(OutingModel.student_uuid == sid)
                           .order_by(OutingModel.date.desc()).all())

        if not outings: raise NotFound

        return outings