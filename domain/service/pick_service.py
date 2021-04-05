from abc import ABCMeta, abstractmethod


class PickService(metaclass=ABCMeta):
    @abstractmethod
    def absent(self, student_number, start_time, end_time): pass