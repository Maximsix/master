from abc import ABC, abstractmethod


class Move(ABC):

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

