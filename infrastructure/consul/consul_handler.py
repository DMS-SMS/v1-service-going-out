import json

from typing import Optional
from consul import Consul, Check

from infrastructure.config.consul_config import ConsulConfig


class ConsulHandler:
    def __init__(self):
        self.consul_config = ConsulConfig()
        self.consul = Consul(host=self.consul_config.host, port=self.consul_config.port)
        self.consul_agent = self.consul.Agent(self.consul)
        self.consul_service = self.consul_agent.Service(self.consul)
        self.consul_check = self.consul_agent.Check(self.consul)

    def register_consul(self):
        self.consul_service.register(
            name=self.consul_config.service_name,
            service_id=self.consul_config.service_id,
            address=self.consul_config.service_host,
            port=self.consul_config.service_port,
            token=self.consul_config.token,
        )

        self.consul_check.register(
            name=f"service '{self.consul_config.service_name}' check",
            check=Check.ttl("10000000s"),
            check_id=self.consul_config.check_id,
            service_id=self.consul_config.service_id,
            token=self.consul_config.token,
        )

        self.consul_check.ttl_pass(self.consul_config.check_id)

    def deregister_consul(self):
        self.consul_check.deregister(self.consul_config.check_id)
        self.consul_service.deregister(self.consul_config.service_id)

    def get_address(self, service: str) -> Optional[str]:
        services = self.consul_agent.services()
        for service_id in services:
            if services[service_id]["Service"] == service:
                return (
                    f"{services[service_id]['Address']}:{services[service_id]['Port']}"
                )

        return None

    def get_db_info(self) -> dict:
        return json.loads(self.consul.kv.get("db/outing/local")[1]["Value"].decode())
