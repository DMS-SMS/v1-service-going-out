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
    consul.register(name="Outing",
                    service_id="aaaa",
                    address="10.0.0.0",
                    port=20050,
                    token="aaaaa")

def deregister_consul(consul):
    consul.deregister("aaaa")