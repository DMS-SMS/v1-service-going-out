from abc import ABCMeta, abstractmethod


class SMSService(metaclass=ABCMeta):
    @abstractmethod
    def send(self, target_number: str, message: str): pass