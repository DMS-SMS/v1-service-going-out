from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class StillOut(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.CONFLICT)
        self.code: int = outing.still_out
        self.msg: str = "Still out"
