class gRPCAppConfig:
    def __init__(self):
        self._max_workers = 10
        self._host = "0.0.0.0"
        self._port = 50051

    @property
    def max_workers(self):
        return self._max_workers

    @property
    def address(self):
        return str(self._host + ":" + str(self._port))


class ConsulConfig:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 8500
        self._token = "12345"

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def token(self):
        return self._token