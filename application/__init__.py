import grpc
from concurrent import futures

from infrastructure.mysql import sql
from application.servicers import register_outing_servicers

class gRPCApplication:
    def __init__(self, config, consul):
        self._config = config
        self._app = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))
        self._consul = consul

        self._app.add_insecure_port(config.address)
        self.register_db()
        self.register_servicers()

    def register_db(self):
        sql.base.metadata.create_all(sql.engine)

    def register_servicers(self):
        register_outing_servicers(self._app)

    def serve(self):
        try:
            self._app.start()
            self._consul.register_consul()
            print("* gRPC Application is served")
            self._app.wait_for_termination()
        except:
            self._consul.deregister_consul()
            print("* gRPC Application is down")
