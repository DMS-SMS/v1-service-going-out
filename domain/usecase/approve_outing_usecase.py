from const.code.python.outing import *

from domain.exception import ConfirmCodeNotFound, OutingFlowException
from domain.repository.confirm_code_repository import ConfirmCodeRepository
from domain.repository.outing_repository import OutingRepository


class ApproveOutingUseCase:
    def __init__(self, outing_repository, confirm_code_repository):
        self.outing_repository: OutingRepository = outing_repository
        self.confirm_code_repository: ConfirmCodeRepository = confirm_code_repository

    def run(self, confirm_code):
        outing_id = self.confirm_code_repository.find_by_code(confirm_code)
        if outing_id == None: raise ConfirmCodeNotFound()

        outing = self.outing_repository.find_by_id(outing_id)
        if outing.status != "0": raise OutingFlowException(code=already_confirm_by_parents)

        outing.status = "1"
        self.outing_repository.save(outing)