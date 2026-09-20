from .mouse_physics import MousePhysics
from ._click import _Click
from typing import Optional

class _RightClick(_Click):
    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        physics: Optional[MousePhysics] = None
    ) -> None: super().__init__(x = x, y = y, button = "right", clicks = 1, physics = physics)