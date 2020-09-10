from domain.entity.outing import Outing


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