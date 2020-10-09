from domain.exception.business_exception import BusinessException


class NotFound(BusinessException):
    def __init__(self):
        self.status: int = 404
        self.code: int = -1001
        self.msg: str = "NotFound"
