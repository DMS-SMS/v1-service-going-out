import logging

from application import gRPCApplication

from infrastructure.config.grpc_config import gRPCAppConfig
from infrastructure.consul.consul_handler import ConsulHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app = gRPCApplication(gRPCAppConfig(), ConsulHandler())
    app.serve()
