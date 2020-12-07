from abc import ABCMeta, abstractmethod


class SMSService(metaclass=ABCMeta):
    @abstractmethod
    def send(self, target_number: str, message: str, x_request_id): pass