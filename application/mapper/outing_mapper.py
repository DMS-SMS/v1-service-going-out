from typing import List

from domain.entity.outing import Outing
from proto.python.outing.outing_student_pb2 import Outing as ProtoOuting



def create_outing_mapper(request):
    entity: Outing = Outing(
        student_uuid=request.uuid,
        situation=request.situation,
        date=request.date,
        start_time=request.start_time,
        end_time=request.end_time,
        place=request.place,
        reason=request.reason)
    return entity

def get_outings_mapper(outing_entities: List["Outing"]) -> List["ProtoOuting"]:
    outings = list()

    for outing_entity in outing_entities:
        print(outing_entity._date)

        outing = ProtoOuting()
        outing.place = outing_entity._place
        outing.reason = outing_entity._reason
        outing.date = outing_entity._date
        outing.start_time = outing_entity._start_time
        outing.end_time = outing_entity._end_time
        outing.situation = outing_entity._situation
        outing.status = outing_entity._status

        outings.append(outing)

    return outings
