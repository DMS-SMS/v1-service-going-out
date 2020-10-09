from http.server import HTTPStatus
from const.code.python import outing
from domain.exception.business_exception import BusinessException


class NotApprovedByParents(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.CONFLICT)
        self.code: int = outing.not_approved_by_parents
        self.msg: str = "It has not been approved by parents yet"


class AlreadyApprovedByTeacher(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.CONFLICT)
        self.code: int = outing.already_approved_by_teacher
        self.msg: str = "It has been approved by teacher"


class AlreadyApprovedByParents(BusinessException):
    def __init__(self):
        self.status: int = int(HTTPStatus.CONFLICT)
        self.code: int = outing.already_approved_by_parents
        self.msg: str = "It has been approved by parents"
