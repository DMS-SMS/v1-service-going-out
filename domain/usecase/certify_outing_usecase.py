from domain.repository import OutingRepository


class CertifyOutingUseCase:
    def __init__(self, outing_repository):
        self.outing_repository: OutingRepository = outing_repository

    def run(self, o_id):
        self.outing_repository.certify_by_outing_for_teacher(o_id)