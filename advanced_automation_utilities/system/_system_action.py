from abc import ABC, abstractmethod

class _SystemAction(ABC):
    @abstractmethod
    def execute(self) -> None: pass