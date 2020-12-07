from domain.service.sms_service import SMSService
from infrastructure.open_tracing import open_tracing
from infrastructure.open_tracing.open_tracing_handler import trace_service


class SMSServiceImpl(SMSService):
    @trace_service("SMS (send)", open_tracing)
    def send(self, target_number: str, message: str, x_request_id):
        pass