from typing import Optional

from domain.repository.confirm_code_repository import ConfirmCodeRepository
from infrastructure.redis import RedisHandler


class ConfirmCodeRepositoryImpl(ConfirmCodeRepository):
    def __init__(self):
        self.redis = RedisHandler()

    def save(self, outing_uuid: str, confirm_code: str):
        self.redis.save(confirm_code, outing_uuid)

    def find_by_code(self, confirm_code: str) -> Optional["str"]:
        return self.redis.find_by_key(confirm_code)

    def delete_by_code(self, confirm_code: str):
        self.redis.delete_by_key(confirm_code)