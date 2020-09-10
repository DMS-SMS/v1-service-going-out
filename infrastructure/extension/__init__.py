from infrastructure.extension.database import register_db
from infrastructure.extension.redis_register import register_redis


db_session, Base, engine = register_db()
redis = register_redis()