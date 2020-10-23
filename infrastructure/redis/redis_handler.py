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

    def save(self, key: str, value: str):
        self._redis.set(key, value)

    def find_by_key(self, key: str) -> Optional[str]:
        try:
            value = self._redis.get(key).decode()
        except:
            value = None
        return value

    def delete_by_key(self, key: str):
        self._redis.delete(key)