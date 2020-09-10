class OutingExist(Exception):
    def __init__(self):
        self.status = 409
        self.code = -1001
        self.msg = "Outing is exist"
