from .mouse_physics import MousePhysics
from abc import ABC, abstractmethod
from typing import Optional

class _MouseAction(ABC):
    def __init__(self, physics: Optional[MousePhysics] = None) -> None:
        self.physics = physics or MousePhysics()
    
    @abstractmethod
    def execute(self) -> None: pass