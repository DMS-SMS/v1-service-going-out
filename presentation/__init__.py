import grpc
from concurrent import futures

from presentation.config import gRPCAppConfig


def register_hooks(app):
    pass


def register_servicers(app):
    pass


def create_app():
    config = gRPCAppConfig()
    app = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))

    register_servicers(app)
    register_hooks(app)

    return app