from ._keyboard_physics import KeyboardPhysics
from abc import ABC, abstractmethod
from typing import Optional

class KeyboardAction(ABC):
    def __init__(self, physics: Optional[KeyboardPhysics] = None):
        self.physics = physics or KeyboardPhysics()

    @abstractmethod
    def execute(self): pass