from domain.exception.grpc_exception import gRPCException


class NotProxyAuth(gRPCException):
    def __init__(self):
        self.status: int = 407