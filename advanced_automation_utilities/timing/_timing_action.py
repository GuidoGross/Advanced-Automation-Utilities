from abc import ABC, abstractmethod

class TimingAction(ABC):
    @abstractmethod
    def execute(self): pass