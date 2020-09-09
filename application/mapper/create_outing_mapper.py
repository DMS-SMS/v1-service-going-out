from domain.entity.outing import Outing


def create_outing_mapper(request):
    entity: Outing = Outing(
        outing_uuid=None,
        student_uuid=request.uuid,
        status=None,
        situation=request.situation,
        accept_teacher=None,
        date=request.date,
        start_time=request.start_time,
        end_time=request.end_time,
        place=request.place,
        reason=request.reason,
        arrival_date=None,
        arrival_time=None)
    return entity