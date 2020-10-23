from abc import ABCMeta, abstractmethod


class SMSService(metaclass=ABCMeta):
    @abstractmethod
    def send_to_parents(self, oid: str, o_code: str, x_request_id):
        pass