from domain.repository import OutingRepository


class ApproveOutingTeacherUseCase:
    def __init__(self, outing_repository):
        self.outing_repository: OutingRepository = outing_repository

    def run(self, o_id):
        self.outing_repository.approve_by_outing_for_teacher(o_id)