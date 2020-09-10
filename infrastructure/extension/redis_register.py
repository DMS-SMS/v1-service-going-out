from redis import StrictRedis

from infrastructure.config import RedisConfig


def register_redis():
    redis_config = RedisConfig()
    return StrictRedis(
        host = redis_config.host,
        port = redis_config.port,
        password = redis_config.password,
        db = redis_config.db
    )