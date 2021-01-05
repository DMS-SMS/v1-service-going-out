import os

from domain.service.sms_service import SMSService
from infrastructure.open_tracing import open_tracing
from infrastructure.open_tracing.open_tracing_handler import trace_service


class SMSServiceImpl(SMSService):
    @trace_service("SMS (send)", open_tracing)
    def send(self, target_number: str, message: str, x_request_id):
        import boto3
        client = boto3.client(
            "sns",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
            region_name="ap-northeast-1"  # 도쿄
        )

        client.publish(
            PhoneNumber="+82" + target_number,
            Message=message,
            MessageAttributes={
                'AWS.SNS.SMS.SMSType': {
                    'DataType': 'String',
                    'StringValue': 'Transactional'
                }
            }
        )
