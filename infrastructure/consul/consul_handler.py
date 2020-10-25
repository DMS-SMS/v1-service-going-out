import json
import random

from typing import Optional
from consul import Consul, Check

from infrastructure.config.consul_config import ConsulConfig
from infrastructure.util.random_key import generate_random_key_only_hex


class ConsulHandler:
    def __init__(self):
        self.consul = Consul(host=ConsulConfig.host, port=ConsulConfig.port)
        self.consul_agent = self.consul.Agent(self.consul)
        self.consul_service = self.consul_agent.Service(self.consul)
        self.consul_check = self.consul_agent.Check(self.consul)
        ConsulConfig.service_host = "0.0.0.0"
        ConsulConfig.service_port = self.create_service_port()
        ConsulConfig.service_id = self.create_service_id()

    def register_consul(self):

        self.consul_service.register(
            name=ConsulConfig.service_name,
            service_id=ConsulConfig.service_id,
            address=ConsulConfig.service_host,
            port=ConsulConfig.service_port,
            token=ConsulConfig.token,
        )

        self.consul_check.register(
            name=f"service '{ConsulConfig.service_name}' check",
            check=Check.ttl("10000000s"),
            check_id=ConsulConfig.check_id,
            service_id=ConsulConfig.service_id,
            token=ConsulConfig.token,
        )

        self.consul_check.ttl_pass(ConsulConfig.check_id)


    def deregister_consul(self):
        self.consul_check.deregister(ConsulConfig.check_id)
        self.consul_service.deregister(ConsulConfig.service_id)

    def get_address(self, service: str) -> Optional[str]:
        services = self.consul_agent.services()
        checks = self.consul_agent.checks()
        for service_id in services:
            if services[service_id]["Service"] == service:
                if checks[f"service:{service_id}"]["Status"] == "passing":
                    return (
                        f"{services[service_id]['Address']}:{services[service_id]['Port']}"
                    )

        return None

    def get_db_info(self) -> dict:
        return json.loads(self.consul.kv.get("db/outing/local")[1]["Value"].decode())

    def get_redis_info(self) -> dict:
        return json.loads(self.consul.kv.get("redis/outing/local")[1]["Value"].decode())

    def create_service_port(self) -> int:
        port = self.generate_service_port()
        while self.check_service_port(port): port = self.generate_service_port()
        return port

    def check_service_port(self, port) -> bool:
        services = self.consul_agent.services()
        for service in services:
            if services[service]["Port"] == port: return True
        else: return False

    def generate_service_port(self) -> int:
        return random.randrange(10101, 10200)

    def create_service_id(self) -> str:
        service_id = self.generate_service_id()
        while self.check_service_id(service_id): service_id = self.generate_service_id()
        return service_id

    def check_service_id(self, service_id) -> bool:
        try: self.consul_agent.services()[service_id]
        except: return False
        return True

    def generate_service_id(self) -> str:
        return f"{ConsulConfig.service_name}" \
               f"-{generate_random_key_only_hex(8)}" \
               f"-{generate_random_key_only_hex(4)}" \
               f"-{generate_random_key_only_hex(4)}" \
               f"-{generate_random_key_only_hex(4)}" \
               f"-{generate_random_key_only_hex(12)}"