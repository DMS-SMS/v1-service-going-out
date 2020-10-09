from domain.exception.not_proxy_auth import NotProxyAuth

class BadXRequestId(NotProxyAuth):
    def __init__(self):
        self.status: int = 407
        self.code: int = -402
        self.msg: str = "Bad x-request-id"