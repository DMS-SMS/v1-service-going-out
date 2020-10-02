import grpc
from concurrent import futures

from infrastructure.extension import Base, engine
from infrastructure.model import OutingModel
from infrastructure.config.grpc_config import gRPCAppConfig
from application.servicers import register_outing_servicers

def register_db():
    Base.metadata.create_all(engine)

def register_servicers(app):
    register_outing_servicers(app)


def create_app():
    config = gRPCAppConfig()
    app = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))
    app.add_insecure_port(config.address)

    register_db()
    register_servicers(app)

    return app
