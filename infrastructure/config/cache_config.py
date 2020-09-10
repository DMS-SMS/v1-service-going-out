from typing import Optional


class CacheConfig:
    def __init__(self):
        self._host: str = "127.0.0.1"
        self._port: int = 6379
        self._password: Optional[str] = None
        self._db: int = 1

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def password(self):
        return self._password

    @property
    def db(self):
        return self._db
