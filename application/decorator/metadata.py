from functools import wraps


def x_request_id(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        context = args[2]
        for k, v in context.invocation_metadata():
            if k == "x-request-id":
                context.set_trailing_metadata((
                    ('x-request-id', v.encode()),
                ))
                break

        return fn(*args, **kwargs)
    return wrapper

