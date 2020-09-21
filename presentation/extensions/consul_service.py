from consul import Consul

from presentation.config import ConsulConfig


def create_consul():
    consul_config = ConsulConfig()
    consul = Consul(
        host=consul_config.host,
        port=consul_config.port
    )

    return consul.Agent(consul).Service(consul)


def register_consul(consul):
    consul_config = ConsulConfig()
    consul.register(name=consul_config.service_name,
                    service_id=consul_config.service_id,
                    address=consul_config.service_host,
                    port=consul_config.service_port,
                    token=consul_config.token)

def deregister_consul(consul):
    consul_config = ConsulConfig()
    consul.deregister(consul_config.service_id)