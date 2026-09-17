from ._mouse_action import MouseAction
from ._mouse_physics import MousePhysics
from .move import Move
from .hold_click import HoldClick
from .release_click import ReleaseClick
from ..timing import Timing
from typing import Optional

class DragAndDrop(MouseAction):
    def __init__(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        button: str = "left",
        physics: Optional[MousePhysics] = None
    ):
        super().__init__(physics = physics)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.button = button

    def execute(self):
        timing = Timing()
        Move(x = self.start_x, y = self.start_y, physics = self.physics).execute()
        HoldClick(
            x = self.start_x, y = self.start_y, button = self.button, physics = self.physics
        ).execute()
        timing.wait(0.2)
        Move(x = self.end_x, y = self.end_y, physics = self.physics).execute()
        timing.wait(0.2)
        ReleaseClick(
            x = self.end_x, y = self.end_y, button = self.button, physics = self.physics
        ).execute()