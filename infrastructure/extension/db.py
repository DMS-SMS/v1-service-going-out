from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.config import DatabaseConfig


def register_db():
    database_config = DatabaseConfig()

    engine = create_engine(database_config.address())
    db_session = scoped_session(sessionmaker(
        autocommit=database_config.autocommit, autoflush=database_config.autoflush, bind=engine))

    base = declarative_base()

    return db_session, base