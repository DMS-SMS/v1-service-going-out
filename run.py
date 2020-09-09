from presentation import create_app


def serve():
    app = create_app()
    app.start()
    app.wait_for_termination()


if __name__ == '__main__':
    serve()