from typing import Optional


class DatabaseConfig:
    def __init__(self):
        self._sql: str = "mysql"
        self._db: str = "test"
        self._host: str = "127.0.0.1"
        self._user: str = "root"
        self._password: str = "mingi0130"

        self._autocommit = False
        self._autoflush = False

    @property
    def address(self):
        return str(f"{self._sql}://{self._user}:{self._password}@{self._host}/{self._db}?charset=utf8")

    @property
    def autocommit(self):
        return self._autocommit

    @property
    def autoflush(self):
        return self._autoflush


class RedisConfig:
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
