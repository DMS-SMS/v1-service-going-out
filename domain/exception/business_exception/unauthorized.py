from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class Unauthorized(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.FORBIDDEN)
        self.code: int = outing.unauthorized
        self.msg: str = "Unauthorized"
