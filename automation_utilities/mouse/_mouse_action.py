from ._mouse_physics import MousePhysics
from abc import ABC, abstractmethod
from typing import Optional

class MouseAction(ABC):
    def __init__(self, physics: Optional[MousePhysics] = None): self.physics = physics or MousePhysics()

    @abstractmethod
    def execute(self): pass