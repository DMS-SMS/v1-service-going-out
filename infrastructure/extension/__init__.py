from infrastructure.extension.consul_service import ConsulService
consul = ConsulService()

from infrastructure.extension.database import register_db
db_session, Base, engine = register_db()

from infrastructure.extension.redis_register import register_redis
redis = register_redis()