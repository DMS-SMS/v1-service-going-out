from abc import ABCMeta, abstractmethod

class uuidService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def compare_uuid_and_sid(cls, uuid, sid):
        pass