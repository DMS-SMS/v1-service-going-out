from typing import Optional

from domain.exception.grpc_exception import gRPCException


class BusinessException(gRPCException):
    def __init__(self):
        self.status: Optional[int] = None
        self.code: Optional[int] = None
        self.msg: Optional[str] = None
