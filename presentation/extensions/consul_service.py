from consul import Consul
from consul import Check

from presentation.config import ConsulConfig


def create_consul():
    consul_config = ConsulConfig()
    consul = Consul(
        host=consul_config.host,
        port=consul_config.port
    )

    return consul.Agent(consul).Service(consul), consul.Agent(consul).Check(consul)


def register_consul(consul_service, consul_check):
    consul_config = ConsulConfig()
    consul_service.register(name=consul_config.service_name,
                    service_id=consul_config.service_id,
                    address=consul_config.service_host,
                    port=consul_config.service_port,
                    token=consul_config.token)

    consul_check.register(name=f"service '{consul_config.service_name}' check",
                          check=Check.ttl("10000000s"),
                          check_id = consul_config.check_id,
                          service_id = consul_config.service_id,
                          token=consul_config.token
    )

    consul_check.ttl_pass(consul_config.check_id)

def deregister_consul(consul_service, consul_check):
    consul_config = ConsulConfig()

    consul_check.deregister(consul_config.check_id)
    consul_service.deregister(consul_config.service_id)