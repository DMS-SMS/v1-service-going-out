import atexit
import grpc
from concurrent import futures

from infrastructure.mysql import sql
from application.servicers import register_outing_servicers

class gRPCApplication:
    def __init__(self, config, consul):
        self._consul = consul
        self._config = config
        self._app = grpc.server(futures.ThreadPoolExecutor(max_workers=self._config.max_workers))
        atexit.register(self.stop)

        self._app.add_insecure_port(self._config.address)
        self.register_db()
        self.register_servicers()

    def register_db(self):
        sql.base.metadata.create_all(sql.engine)

    def register_servicers(self):
        register_outing_servicers(self._app)

    def stop(self):
        self._consul.deregister_consul()
        print("* gRPC Application is down")

    def serve(self):
        try:
            self._app.start()
            self._consul.register_consul(self._config.port)
            print(f"* gRPC Application is served in {self._config.address}")
            self._app.wait_for_termination()
        except Exception as e:
            print(e)
            self.stop()
