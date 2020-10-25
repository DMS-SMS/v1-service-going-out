from typing import Optional

from redis import StrictRedis

from infrastructure.config.cache_config import CacheConfig
from infrastructure.open_tracing import open_tracing
from infrastructure.open_tracing.open_tracing_handler import trace_service


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

    @trace_service("Redis (save)", open_tracing)
    def save(self, key: str, value: str):
        self._redis.set(key, value)

    @trace_service("Redis (find)", open_tracing)
    def find_by_key(self, key: str) -> Optional[str]:
        try:
            value = self._redis.get(key).decode()
        except:
            value = None
        return value

    @trace_service("Redis (delete)", open_tracing)
    def delete_by_key(self, key: str):
        self._redis.delete(key)