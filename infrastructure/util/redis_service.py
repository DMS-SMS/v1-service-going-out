from typing import Optional

from infrastructure.extension import redis
from infrastructure.exception.not_found import NotFound


def save_parents_outing_code(oid: str, o_code: str):
    redis.set(o_code, oid)


def get_oid_by_parents_outing_code(o_code: str) -> Optional[str]:
    try:
        oid = redis.get(o_code).decode()
    except:
        oid = None
    return oid


def delete_outing_code(o_code: str):
    redis.delete(o_code)
