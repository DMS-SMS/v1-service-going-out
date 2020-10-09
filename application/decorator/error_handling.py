from functools import wraps

from domain.exception.not_proxy_auth import NotProxyAuth
from domain.exception.business_exception import BusinessException
from domain.exception.grpc_exception import gRPCException
from domain.exception.server_error import ServerErrorException


def error_handling(response):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                try:
                    return fn(*args, **kwargs)
                except BusinessException as e:
                    raise e
                except NotProxyAuth as e:
                    raise e
                except Exception:
                    raise ServerErrorException
            except gRPCException as e:
                return response(status=e.status, code=e.code, msg=e.msg)


        return wrapper

    return decorator
