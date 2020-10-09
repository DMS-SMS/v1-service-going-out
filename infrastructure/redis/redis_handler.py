from typing import Optional

from redis import StrictRedis

from infrastructure.config.cache_config import CacheConfig


class RedisHandler:
    def __init__(self):
        self._config = CacheConfig()
        self._redis = StrictRedis(
            host=self._config.host,
            port=self._config.port,
            password=self._config.password,
            db=self._config.db,
        )

    @property
    def redis(self):
        return self._redis

    def save_parents_outing_code(self, oid: str, o_code: str):
        self._redis.set(o_code, oid)

    def get_oid_by_parents_outing_code(self, o_code: str) -> Optional[str]:
        try:
            oid = self._redis.get(o_code).decode()
        except:
            oid = None
        return oid

    def delete_outing_code(self, o_code: str):
        self._redis.delete(o_code)