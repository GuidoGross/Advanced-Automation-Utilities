from ._mouse_action import _MouseAction
from .mouse_physics import MousePhysics
from ._move import _Move
from ._hold_click import _HoldClick
from ._release_click import _ReleaseClick
from ..timing import Timing
from typing import Optional

class _DragAndDrop(_MouseAction):
    def __init__(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        button: str = "left",
        physics: Optional[MousePhysics] = None
    ) -> None:
        super().__init__(physics = physics)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.button = button
        if self.button not in ["left", "right", "middle"]:
            raise ValueError("Invalid mouse button. Valid options: \"left\", \"right\", \"middle\".")
    
    def execute(self) -> None:
        timing = Timing()
        _Move(x = self.start_x, y = self.start_y, physics = self.physics).execute()
        _HoldClick(
            x = self.start_x, y = self.start_y, button = self.button, physics = self.physics
        ).execute()
        timing.wait(0.2)
        _Move(x = self.end_x, y = self.end_y, physics = self.physics).execute()
        timing.wait(0.2)
        _ReleaseClick(
            x = self.end_x, y = self.end_y, button = self.button, physics = self.physics
        ).execute()