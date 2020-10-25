import os

class ConsulConfig:
    address = os.getenv("CONSUL_ADDR").split(":")
    host = address[0]
    port = int(address[1])

    service_name = "DMS.SMS.v1.service.outing"
    service_id = None
    service_host = None
    service_port = None
    token = "temporary_token"

    check_id = f"service:{service_name}"