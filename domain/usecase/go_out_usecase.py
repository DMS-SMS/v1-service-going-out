from domain.repository import OutingRepository


class GoOutUseCase:
    def __init__(self, outing_repository):
        self.outing_repository: OutingRepository = outing_repository

    def run(self, o_id):
        self.outing_repository.go_out(o_id)