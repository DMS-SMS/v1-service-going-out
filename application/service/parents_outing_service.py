from domain.usecase.reject_outing_usecase import RejectOutingUseCase
from proto.python.outing import outing_parents_pb2 as proto
from domain.usecase.approve_outing_usecase import ApproveOutingUseCase
from application.decorator.error_handling import error_handling


class ParentsOutingService:
    def __init__(self, approve_outing_usecase, reject_outing_usecase):
        self.approve_outing_usecase: ApproveOutingUseCase = approve_outing_usecase
        self.reject_outing_usecase: RejectOutingUseCase = reject_outing_usecase

    @error_handling(proto.ConfirmOutingByOCodeResponse)
    def approve_outing(self, request):
        self.approve_outing_usecase.run(request.o_code)
        return proto.ConfirmOutingByOCodeResponse(status=200)

    @error_handling(proto.ConfirmOutingByOCodeResponse)
    def reject_outing(self, request):
        self.reject_outing_usecase.run(request.o_code)
        return proto.ConfirmOutingByOCodeResponse(status=200)
