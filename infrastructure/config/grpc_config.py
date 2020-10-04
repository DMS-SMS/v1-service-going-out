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