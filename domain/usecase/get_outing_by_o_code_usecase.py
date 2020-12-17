from domain.exception import ConfirmCodeNotFound
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository


class GetOutingByOCodeUseCase:
    def __init__(self, outing_repository, confirm_code_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository

    def run(self, confirm_code):
        outing_id = self.confirm_code_repository.find_by_code(confirm_code)
        if outing_id == None: raise ConfirmCodeNotFound()

        return self.outing_repository.find_by_id(outing_id)