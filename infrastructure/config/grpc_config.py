from infrastructure.config.consul_config import ConsulConfig


class gRPCAppConfig:
    def __init__(self):
        self._max_workers = 10
        # self._host = ConsulConfig.service_host
        self._host = "0.0.0.0"
        self._port = ConsulConfig.service_port

    @property
    def max_workers(self):
        return self._max_workers

    @property
    def address(self):
        return str(self._host + ":" + str(self._port))