from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class OutingFlowException(BusinessException):
    def __init__(self, code=-1000):
        self.status: int = int(HTTPStatus.CONFLICT)
        self.code: int = code
        self.msg: str = "The request cannot be executed"
