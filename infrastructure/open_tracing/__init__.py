from functools import wraps
from jaeger_client import Config
from jaeger_client.span_context import SpanContext


class reigsterOpenTracing:
    def __init__(self):
        self._config = Config(
            config={  # usually read from some yaml config
                'logging': True,
            },
            service_name='outing-service',
            validate=True,
        )
        self._tracer = self._config.initialize_tracer()

    @property
    def tracer(self):
        return self._tracer


class openTracing:
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
