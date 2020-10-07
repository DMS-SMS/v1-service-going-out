from application import gRPCApplication

from infrastructure.config.grpc_config import gRPCAppConfig
from infrastructure.extension import consul

if __name__ == "__main__":
    app = gRPCApplication(gRPCAppConfig(), consul)
    app.serve()
