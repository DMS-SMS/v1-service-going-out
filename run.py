from application import create_app
from infrastructure.extension import consul


def serve(app):
    try:
        app.start()
        print("* Presentation is served")
        consul.register_consul()
        app.wait_for_termination()
    except:
        consul.deregister_consul()


if __name__ == "__main__":
    app = create_app()
    serve(app)
