from infrastructure.exception.business_exception import BusinessException


class NotApprovedByParents(BusinessException):
    def __init__(self):
        self.status: int = 407
        self.code: int = -1201
        self.msg: str = "It has not been approved by parents yet"


class AlreadyApprovedByTeacher(BusinessException):
    def __init__(self):
        self.status: int = 407
        self.code: int = -1202
        self.msg: str = "It has been approved by teacher"


class AlreadyApprovedByParents(BusinessException):
    def __init__(self):
        self.status: int = 407
        self.code: int = -1203
        self.msg: str = "It has been approved by parents"
