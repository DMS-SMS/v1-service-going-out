class ConsulConfig:
    def __init__(self):
        self._host = "127.0.0.1"
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
