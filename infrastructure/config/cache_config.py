import os
from typing import Optional
from infrastructure.consul.consul_handler import ConsulHandler


class CacheConfig:
    def __init__(self):
        self._consul = ConsulHandler()
        self._redis_info = self._consul.get_redis_info()
        self._host: str = self._redis_info["host"]
        self._port: int = self._redis_info["port"]
        self._password: Optional[str] = os.getenv("REDIS_PASSWORD")
        self._db: int = self._redis_info["db"]

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def password(self) -> Optional[str]:
        return self._password

    @property
    def db(self) -> int:
        return self._db
