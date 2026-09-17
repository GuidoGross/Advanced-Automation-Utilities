from ._mouse_physics import MousePhysics
from .click import Click
from typing import Optional

class DoubleClick(Click):
    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left",
        physics: Optional[MousePhysics] = None
    ): super().__init__(x = x, y = y, button = button, clicks = 2, physics = physics)