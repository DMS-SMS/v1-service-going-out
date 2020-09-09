from presentation import create_app


if __name__ == '__main__':
    app = create_app()
    app.start()
    app.wait_for_termination()