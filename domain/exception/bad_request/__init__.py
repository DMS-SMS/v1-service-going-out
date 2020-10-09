from domain.exception.grpc_exception import gRPCException


class BadRequestException(gRPCException):
    def __init__(self):
        self.status = 400
        self.code = -1000
        self.msg = "Bad Request"
