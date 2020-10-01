from domain.repository import OutingRepository


class FinishGoOutUseCase:
    def __init__(self, outing_repository):
        self.outing_repository: OutingRepository = outing_repository

    def run(self, o_id):
        self.outing_repository.finish_go_out(o_id)