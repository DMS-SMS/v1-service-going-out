from functools import wraps
from infrastructure.extension import open_tracing
from infrastructure.open_tracing import openTracing



def jagger_enable(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        flag = 0
        context = args[2]
        parents_span = str()
        x_request_id = str()
        for k, v in context.invocation_metadata():
            if flag == 2: break
            if k == "x-request-id":
                x_request_id = v
                flag += 1
            if k == "span-context":
                parents_span = v
                flag += 1
        else: raise Exception

        open_tracing_service = openTracing(open_tracing.tracer, parents_span, x_request_id)
        return open_tracing_service.start_active_span(fn, *args, **kwargs)

    return wrapper
