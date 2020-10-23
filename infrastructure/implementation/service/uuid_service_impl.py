from domain.service.uuid_service import UuidService
from infrastructure.implementation.repository.confirm_code_repository_impl import ConfirmCodeRepositoryImpl
from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl

from infrastructure.util.random_key import generate_confirm_code, generate_outing_uuid


class UuidServiceImpl(UuidService):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.confirm_code_repository = ConfirmCodeRepositoryImpl()

    def generate_outing_uuid(self) -> str:
        uuid = generate_outing_uuid()
        while self.outing_repository.find_by_id(uuid): uuid = generate_outing_uuid()
        return uuid

    def generate_confirm_code(self) -> str:
        code = generate_confirm_code()
        while self.confirm_code_repository.find_by_code(code): code = generate_confirm_code()
        return code

