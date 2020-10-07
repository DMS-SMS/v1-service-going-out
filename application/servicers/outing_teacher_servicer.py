from domain.usecase.approve_outing_teacher_usecase import ApproveOutingTeacherUseCase
from domain.usecase.certify_outing_usecase import CertifyOutingUseCase
from domain.usecase.get_outings_with_filter_usecase import GetOutingsWithFilterUseCase
from domain.usecase.reject_outing_teacher_usecase import RejectOutingTeacherUseCase
from proto.python.outing import outing_teacher_pb2_grpc

from application.service.teacher_outing_service import TeacherOutingService
from application.decorator.metadata import jagger_enable

from infrastructure.repository import OutingRepositoryImpl
from infrastructure.service.outing_domain_service_impl import OutingDomainServiceImpl


class TeacherOutingServicer(outing_teacher_pb2_grpc.OutingTeacherServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.outing_domain_service = OutingDomainServiceImpl()

        self.service = TeacherOutingService(
            approve_outing_teacher_usecase=ApproveOutingTeacherUseCase(
                self.outing_repository
            ),
            reject_outing_teacher_usecase=RejectOutingTeacherUseCase(
                self.outing_repository
            ),
            certify_outing_usecase=CertifyOutingUseCase(
                self.outing_repository
            ),
            get_outings_with_filter_usecase=GetOutingsWithFilterUseCase(
                self.outing_repository,
                self.outing_domain_service
            )
        )

    @jagger_enable
    def GetOutingWithFilter(self, request, context):
        return self.service.get_outings_with_filter(request)

    @jagger_enable
    def ApproveOuting(self, request, context):
        return self.service.approve_outing(request)

    @jagger_enable
    def RejectOuting(self, request, context):
        return self.service.reject_outing(request)

    @jagger_enable
    def CertifyOuting(self, request, context):
        return self.service.certify_outing(request)
