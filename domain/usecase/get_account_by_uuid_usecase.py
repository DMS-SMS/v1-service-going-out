from domain.repository.student_repository import StudentRepository


class GetAccountByUuidUseCase:
    def __init__(self, student_repository):
        self.student_repository: StudentRepository = student_repository

    def run(self, account_uuid, x_request_id):
        return self.student_repository.find_by_uuid(account_uuid, x_request_id)