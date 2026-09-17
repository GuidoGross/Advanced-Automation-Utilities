from abc import ABC, abstractmethod

class SystemAction(ABC):
    @abstractmethod
    def execute(self): pass