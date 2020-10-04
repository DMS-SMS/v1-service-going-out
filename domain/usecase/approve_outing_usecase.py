from domain.repository import OutingRepository


class ApproveOutingUseCase:
    def __init__(self, outing_repository):
        self.outing_repository: OutingRepository = outing_repository

    def run(self, o_code):
        self.outing_repository.approve_by_outing_for_parents(o_code)