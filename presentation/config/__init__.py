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
        self._host = "10.156.145.137"
        self._port = 8500

        self._service_host = None
        self._service_port = None
        self._service_id = "DMS.SMS.v1.service.outing"
        self._service_name = "DMS.SMS.v1.service.outing"
        self._token = "temporary_token"

        self._check_id = "DMS.SMS.v1.service.outing"

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def service_host(self):
        return self._service_host

    @property
    def service_port(self):
        return self._service_port

    @property
    def service_id(self):
        return self._service_id

    @property
    def service_name(self):
        return self._service_name

    @property
    def token(self):
        return self._token

    @property
    def check_id(self):
        return self._check_id
