from redis import StrictRedis

from infrastructure.config.cache_config import CacheConfig


def register_redis():
    redis_config = CacheConfig()
    return StrictRedis(
        host=redis_config.host,
        port=redis_config.port,
        password=redis_config.password,
        db=redis_config.db,
    )
