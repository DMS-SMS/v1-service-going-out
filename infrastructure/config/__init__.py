class DatabaseConfig:
    def __init__(self):
        self._sql: str = "mysql"
        self._db: str = "testdb"
        self._host: str = "0.0.0.0"
        self._user: str = "guest"
        self._password: str = "temporary_password"

        self._autocommit = False
        self._autoflush = False

    @property
    def address(self):
        return str(self._sql+"://"+self._user+"@"+self._password+"/"+self._db)

    @property
    def autocommit(self):
        return self._autocommit

    @property
    def autoflush(self):
        return self._autoflush

