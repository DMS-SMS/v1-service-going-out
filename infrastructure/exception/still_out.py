from infrastructure.exception.business_exception import BusinessException


class StillOut(BusinessException):
    def __init__(self):
        self.status: int = 407
        self.code: int = -1001
        self.msg: str = "Still out"
