import os
import boto3

from threading import Thread

from infrastructure.consul.consul_handler import ConsulHandler


class AwsSqsService:
    def __init__(self, consul):
        self.consul: ConsulHandler = consul
        self.queue_url = os.getenv("SQS_ADDRESS")
        self.client = boto3.client(
            "sqs",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
            region_name="ap-northeast-2"
        )

    def listen(self):
        consul_checker = Thread(target=self.check_consul)
        consul_checker.start()

    def check_consul(self):
        while True:
            if self.get_messages():
                self.consul.update_address()

    def get_messages(self):
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            WaitTimeSeconds=3
        )

        try:
            for message in response["Messages"]:
                self.client.delete_message(
                    QueueUrl=self.queue_url,
                    ReceiptHandle=message["ReceiptHandle"]
                )
                return True
        except KeyError:
            return False

    def purge(self):
        self.client.purge_queue(QueueUrl=self.queue_url)
