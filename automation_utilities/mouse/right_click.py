from ._mouse_physics import MousePhysics
from .click import Click
from typing import Optional

class RightClick(Click):
    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        physics: Optional[MousePhysics] = None
    ): super().__init__(x = x, y = y, button = "right", clicks = 1, physics = physics)