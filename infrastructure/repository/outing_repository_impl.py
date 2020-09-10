from sqlalchemy import and_

from infrastructure.model import OutingModel
from infrastructure.extension import db_session
from infrastructure.util.random_key import random_key_generate
from infrastructure.mapper.outing_repository_mapper import create_outing_mapper
from infrastructure.exception import OutingExist

from domain.repository.outing_repository import OutingRepository
from domain.entity.outing import Outing


class OutingRepositoryImpl(OutingRepository):
    @classmethod
    def save_and_get_oid(cls, outing: Outing) -> int:
        outing_uuid = random_key_generate()

        while db_session.query(OutingModel).filter(OutingModel.uuid == outing_uuid).first():
            outing_uuid = random_key_generate()

        if db_session.query(OutingModel)\
            .filter(and_(OutingModel.student_uuid == outing._student_uuid,
                         OutingModel.date == outing._date)).all(): raise OutingExist


        db_session.add(create_outing_mapper(outing, outing_uuid))
        db_session.commit()

        return outing_uuid