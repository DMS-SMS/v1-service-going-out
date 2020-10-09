from domain.exception.not_proxy_auth import NotProxyAuth

class BadSpanContext(NotProxyAuth):
    def __init__(self):
        self.status: int = 407
        self.code: int = -401
        self.msg: str = "Bad span-context"