from abc import ABC, abstractmethod

class _ScreenAction(ABC):
    @abstractmethod
    def execute(self): pass