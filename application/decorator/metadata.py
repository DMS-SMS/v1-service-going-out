from functools import wraps
from infrastructure.open_tracing import open_tracing
from infrastructure.open_tracing.open_tracing_handler import OpenTracing

from domain.exception.not_proxy_auth import NotProxyAuth
from domain.exception.not_proxy_auth.bad_span_context_exception import BadSpanContext
from domain.exception.not_proxy_auth.bad_x_request_id_exception import BadXRequestId



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
        else:
            if not x_request_id: raise BadXRequestId
            elif not parents_span: raise BadSpanContext

        open_tracing_service = OpenTracing(open_tracing.tracer, parents_span, x_request_id)
        return open_tracing_service.start_active_span(fn, *args, **kwargs)

    return wrapper
