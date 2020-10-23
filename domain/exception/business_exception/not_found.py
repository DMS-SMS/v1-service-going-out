from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class OutingNotFound(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.NOT_FOUND)
        self.code: int = outing.not_found
        self.msg: str = "Outing Not Found"

class ConfirmCodeNotFound(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.NOT_FOUND)
        self.code: int = outing.not_found
        self.msg: str = "Confirm Code Not Found"