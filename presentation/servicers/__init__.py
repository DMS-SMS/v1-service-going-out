from proto.python.outing import outing_student_pb2_grpc, outing_teacher_pb2_grpc

from presentation.servicers.outing_student_servicer import StudentOutingServicer
from presentation.servicers.outing_teacher_servicer import TeacherOutingServicer


def register_outing_servicers(app):
    outing_student_pb2_grpc.add_OutingStudentServicer_to_server(StudentOutingServicer(), app)
    outing_teacher_pb2_grpc.add_OutingTeacherServicer_to_server(TeacherOutingServicer(), app)
