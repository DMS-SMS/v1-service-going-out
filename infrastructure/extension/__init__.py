from infrastructure.extension.database import register_db
from infrastructure.extension.redis_register import register_redis
from infrastructure.extension.consul_service import ConsulService


db_session, Base, engine = register_db()
redis = register_redis()
consul = ConsulService()