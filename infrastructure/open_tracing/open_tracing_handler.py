import os

from functools import wraps

from jaeger_client import Config
from jaeger_client.span_context import SpanContext


class OpenTracingHandler:
    def __init__(self):
        self._jaeger_address = os.getenv("JAEGER_ADDR").split(":")
        self._config = Config(
            config={
                'local_agent': {
                    'reporting_host': self._jaeger_address[0],
                    'reporting_port': int(self._jaeger_address[1]),
                },
                'logging': True,
            },

            service_name='DMS.SMS.v1.service.outing',
            validate=True,
        )
        self._tracer = self._config.initialize_tracer()

    @property
    def tracer(self):
        return self._tracer


class OpenTracing:
    def __init__(self, tracer, span_context, x_request_id):
        self._split_span_context = span_context.split(":")
        self._trace_id = int(self._split_span_context[0], 16)
        self._span_id =int(self._split_span_context[1], 16)
        self._span_parent_id = int(self._split_span_context[2], 16)
        self._span_flag = int(self._split_span_context[3], 16)
        self._span_context = SpanContext(
            self._trace_id,
            self._span_id,
            self._span_parent_id,
            self._span_flag
        )
        self._tracer = tracer
        self._x_request_id = x_request_id


    def start_active_span(self, fn, *args, **kwargs):
        with self._tracer.start_active_span("OutingService", child_of=self._span_context) as span:
            self._tracer.active_span.set_tag("X-Request-Id", self._x_request_id)
            return_value = fn(args[0], args[1], args[2])
            span.close()
            return return_value


def trace_service(service_name, tracer):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            with tracer.tracer.start_active_span(service_name, child_of=tracer.tracer.active_span) as span:
                return_value = fn(*args, **kwargs)
                span.close()
            return return_value
        return wrapper
    return decorator
