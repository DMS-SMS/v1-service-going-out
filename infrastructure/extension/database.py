from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.config.database_config import DatabaseConfig


def register_db():
    database_config = DatabaseConfig()

    engine = create_engine(database_config.address, encoding="utf-8")
    db_session = scoped_session(
        sessionmaker(
            autocommit=database_config.autocommit,
            autoflush=database_config.autoflush,
            bind=engine,
        )
    )

    Base = declarative_base()
    Base.query = db_session.query_property()

    return db_session, Base, engine
