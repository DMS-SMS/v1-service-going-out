from presentation import create_app
from presentation.extensions import consul_service, consul_check
from presentation.extensions.consul_service import register_consul, deregister_consul


def serve():
    try:
        app = create_app()
        app.start()
        print("* Presentation is served")
        register_consul(consul_service, consul_check)
        app.wait_for_termination()
    except:
        deregister_consul(consul_service, consul_check)


if __name__ == "__main__":
    serve()
