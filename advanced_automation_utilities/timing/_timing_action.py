from abc import ABC, abstractmethod

class _TimingAction(ABC):
    @abstractmethod
    def execute(self): pass