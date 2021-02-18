from domain.exception.grpc_exception import gRPCException


class BadRequestException(gRPCException):
    def __init__(self, code=0, message="Bad Request"):
        self.status = 400
        self.code = code
        self.msg = message
