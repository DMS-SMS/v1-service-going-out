from typing import Optional


class gRPCException(Exception):
    def __init__(self):
        self.status: Optional[int] = None
        self.code: Optional[int] = None
        self.msg: Optional[str] = None
