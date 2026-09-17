from abc import ABC, abstractmethod

class SoundAction(ABC):
    @abstractmethod
    def execute(self): pass