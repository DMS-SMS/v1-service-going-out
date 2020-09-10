from typing import Optional

from infrastructure.extension import redis


def save_parents_outing_code(oid: str, o_code: str):
    redis.set(o_code, oid)


def get_oid_by_parents_outing_code(o_code: str) -> Optional[str]:
    return redis.get(o_code)


def delete_outing_code(o_code: str):
    redis.delete(o_code)