from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.config.database_config import DatabaseConfig


class MySQLHandler:
    def __init__(self):
        self._config = DatabaseConfig()
        self._engine = create_engine(self._config.address, encoding="utf-8", pool_recycle=1800, pool_pre_ping=True)
        self._db_session = scoped_session(
            sessionmaker(
                autocommit=self._config.autocommit,
                autoflush=self._config.autoflush,
                bind=self.engine,
                expire_on_commit=False
            )
        )
        self._base = declarative_base()
        self._base.query = self.db_session.query_property()


    @property
    def db_session(self):
        return self._db_session

    @property
    def engine(self):
        return self._engine

    @property
    def base(self):
        return self._base