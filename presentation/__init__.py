import grpc


def register_hooks():
    pass


def register_servicers(app):
    pass


def create_app():
    app = grpc

    register_presentations(app)
    return app