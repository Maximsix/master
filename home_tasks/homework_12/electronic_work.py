from abc import ABC, abstractmethod


class ElectronicWork(ABC):

    @abstractmethod
    def wait(self):
        """start work system"""
        pass

    @abstractmethod
    def put_on_system(self):
        """stop work engine"""
        pass

    @abstractmethod
    def complete_trip(self):
        """object stop and parking"""
        pass
