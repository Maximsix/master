from abc import ABC, abstractmethod


class ElectronicWork(ABC):

    @abstractmethod
    def wait(self):
        """wait system"""
        pass

    @abstractmethod
    def put_on_system(self):
        """put on system"""
        pass

    @abstractmethod
    def complete_trip(self):
        """complete trip"""
        pass
