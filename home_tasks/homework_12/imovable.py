from abc import ABC, abstractmethod


class IMovable(ABC):

    @abstractmethod
    def move(self):
        """object move"""
        pass

    @abstractmethod
    def stop(self):
        """object stop"""
        pass

    @abstractmethod
    def charge(self):
        """charge object"""
        pass

