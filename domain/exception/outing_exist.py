from domain.exception.business_exception import BusinessException


class OutingExist(BusinessException):
    def __init__(self):
        self.status: int = 409
        self.code: int = -1001
        self.msg: str = "Outing is exist"
