from datetime import datetime

from domain.entity.outing import Outing

from infrastructure.model import OutingModel


def create_outing_mapper(outing: Outing, uuid) -> OutingModel:
    return OutingModel(
        uuid = uuid,
        student_uuid = outing._student_uuid,
        status = "0",
        situation = outing._situation,
        date = datetime(year=int(outing._date[0:4]), month=int(outing._date[5:7]), day=int(outing._date[8:10])),
        start_time = outing._start_time,
        end_time = outing._end_time,
        place = outing._place,
        reason = outing._reason
    )