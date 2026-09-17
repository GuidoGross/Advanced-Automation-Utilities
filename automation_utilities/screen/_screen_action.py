from abc import ABC, abstractmethod

class ScreenAction(ABC):
    @abstractmethod
    def execute(self): pass