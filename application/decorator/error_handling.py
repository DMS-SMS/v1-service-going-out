from functools import wraps

from domain.exception.business_exception import BusinessException


def error_handling(response):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except BusinessException as e:
                return response(status=e.status, code=e.code, msg=e.msg)

        return wrapper

    return decorator
