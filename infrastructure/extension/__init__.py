from infrastructure.extension.db import register_db


db_session, Base, engine = register_db()