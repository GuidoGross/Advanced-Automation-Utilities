from .keyboard_physics import KeyboardPhysics
from typing import Optional
from abc import ABC, abstractmethod

class _KeyboardAction(ABC):
    def __init__(self, physics: Optional[KeyboardPhysics] = None) -> None:
        self.physics = physics or KeyboardPhysics()
    
    @abstractmethod
    def execute(self) -> None: pass