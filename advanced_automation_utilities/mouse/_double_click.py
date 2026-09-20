from .mouse_physics import MousePhysics
from ._click import _Click
from typing import Optional

class _DoubleClick(_Click):
    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left",
        physics: Optional[MousePhysics] = None
    ) -> None: super().__init__(x = x, y = y, button = button, clicks = 2, physics = physics)