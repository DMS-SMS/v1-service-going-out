import logging

from infrastructure.consul.consul_handler import ConsulHandler
from proto.python.outing import outing_event_pb2_grpc


class EventServicer(outing_event_pb2_grpc.OutingEventServicer):
    def __init__(self, consul):
        self.consul: ConsulHandler = consul

    def ChangeAllServiceNodes(self, request, context):
        logging.info("* Service addresses is updated")
        self.consul.update_address()
