from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class OutingExist(BusinessException):
    def __init__(self):
        self.status: int = (HTTPStatus.CONFLICT)
        self.code: int = outing.outing_exist
        self.msg: str = "Outing is exist"
