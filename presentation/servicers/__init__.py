from proto.python.outing import outing_student_pb2_grpc

from presentation.servicers.outing_student_servicer import StudentOutingServicer


def register_outing_servicers(app):
    outing_student_pb2_grpc.add_OutingStudentServicer_to_server(StudentOutingServicer(), app)
