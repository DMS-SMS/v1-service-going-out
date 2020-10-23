from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class ConfirmFailed(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.CONFLICT)
        self.code: int = outing.already_approved_by_parents
        self.msg: str = "The request cannot be executed"
