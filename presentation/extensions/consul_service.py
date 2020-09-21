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

    consul_check.register(name="service 'DMS.SMS.v1.service.outing' check",
                          check=Check.ttl("10s"),
                          check_id = "TestCheckId",
                          service_id = consul_config.service_id,
                          token=consul_config.token
    )

def deregister_consul(consul_service, consul_check):
    consul_config = ConsulConfig()
    consul_service.deregister(consul_config.service_id)
    consul_check.deregister("TestCheckId")