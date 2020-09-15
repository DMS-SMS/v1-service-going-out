import grpc
from concurrent import futures

from presentation.config import gRPCAppConfig
from presentation.servicers import register_outing_servicers


def register_hooks(app):
    pass


def register_servicers(app):
    register_outing_servicers(app)


def create_app():
    config = gRPCAppConfig()
    app = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))
    app.add_insecure_port(config.address)

    register_servicers(app)
    register_hooks(app)

    return app
