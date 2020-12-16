from domain.service.sms_service import SMSService
from infrastructure.open_tracing import open_tracing
from infrastructure.open_tracing.open_tracing_handler import trace_service


class SMSServiceImpl(SMSService):
    @trace_service("SMS (send)", open_tracing)
    def send(self, target_number: str, message: str, x_request_id):
        # Temporary
        import os
        import smtplib
        from email.mime.text import MIMEText

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login('frametemporary123@gmail.com', os.getenv("EMAIL_PASSWORD"))

        msg = MIMEText(message)
        msg['Subject'] = 'SMS 테스트'
        msg['To'] = 'dltjdqhr55@gmail.com'
        smtp.sendmail('frametemporary123@gmail.com', 'dltjdqhr55@gmail.com', msg.as_string())

        smtp.quit()