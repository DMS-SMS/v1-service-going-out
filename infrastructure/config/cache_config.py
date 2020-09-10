from typing import Optional


class CacheConfig:
    def __init__(self):
        self._host: str = "127.0.0.1"
        self._port: int = 6379
        self._password: Optional[str] = None
        self._db: int = 1

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
