from infrastructure.extension import consul


class DatabaseConfig:
    def __init__(self):
        self._db_info = consul.get_db_info()
        self._sql: str = self._db_info["dialect"]
        self._db: str = self._db_info["db"]
        self._host: str = self._db_info["host"]
        self._user: str = self._db_info["user"]
        self._password: str = "mingi0130"

        self._autocommit: bool = False
        self._autoflush: bool = False

    @property
    def address(self) -> str:
        return str(
            f"{self._sql}://{self._user}:{self._password}@{self._host}/{self._db}?charset=utf8"
        )

    @property
    def autocommit(self) -> bool:
        return self._autocommit

    @property
    def autoflush(self) -> bool:
        return self._autoflush
