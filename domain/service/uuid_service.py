from abc import ABCMeta, abstractmethod

class UuidService(metaclass=ABCMeta):
    @abstractmethod
    def generate_outing_uuid(self) -> str: pass

    @abstractmethod
    def generate_confirm_code(self) -> str: pass