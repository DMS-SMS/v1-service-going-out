from domain.exception import Unauthorized
from domain.repository.club_repository import ClubRepository
from domain.repository.outing_repository import OutingRepository
from domain.repository.student_repository import StudentRepository
from domain.repository.teacher_repository import TeacherRepository


class GetOutingsWithFilterUseCase:
    def __init__(self, outing_repository, student_repository, teacher_repository, club_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.teacher_repository: TeacherRepository = teacher_repository
        self.club_repository: ClubRepository = club_repository

    def run(self, uuid, x_request_id, status, grade, group, floor):
        if self.teacher_repository.find_by_uuid(uuid, uuid, x_request_id) is None: raise Unauthorized()

        outings = []

        if not grade == 0:
            student_uuids = self.student_repository.find_all_by_inform(uuid, x_request_id, grade, group)
        else:
            student_uuids = []
            for club in self.club_repository.find_all_by_floor(uuid, floor):
                student_uuids.extend(club._members)

        for student_uuid in student_uuids:
            outings += self.outing_repository.find_all_by_student_uuid_and_status(student_uuid, status)

        outings = sorted(outings, key=lambda x: x.start_time, reverse=True)


        return outings