from domain.exception.business_exception import BusinessException


class Unauthorized(BusinessException):
    def __init__(self):
        self.status: int = 403
        self.code: int = -1001
        self.msg: str = "Unauthorized"
