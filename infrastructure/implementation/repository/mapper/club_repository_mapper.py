from domain.entity.club import Club

from proto.python.club import club_student_pb2

def get_club_list_mapper(clubs_proto: club_student_pb2.GetClubInformsWithUUIDsResponse):
    if clubs_proto == None: return []
    clubs = []
    for club in clubs_proto.Informs:
        clubs.append(
            Club(
                uuid=club.ClubUUID,
                name=club.Name,
                members=club.MemberUUIDs
        ))
    return clubs