from typing import Optional

from infrastructure.extension import redis


def save_parents_outing_code(oid, o_code):
    redis.set(o_code, oid)


def get_oid_by_parents_outing_code(o_code) -> Optional[str]:
    return redis.get(o_code)


def delete_outing_code(o_code):
    redis.delete(o_code)