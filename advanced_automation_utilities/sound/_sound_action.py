from abc import ABC, abstractmethod

class _SoundAction(ABC):
    @abstractmethod
    def execute(self) -> None: pass