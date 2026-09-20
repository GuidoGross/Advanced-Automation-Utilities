from ._mouse_action import _MouseAction
from .mouse_physics import MousePhysics
from ._move import _Move
from ..timing import Timing
from typing import Optional
import random
import ctypes

class _ReleaseClick(_MouseAction):
    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left",
        physics: Optional[MousePhysics] = None
    ) -> None:
        super().__init__(physics = physics)
        self.x = x
        self.y = y
        self.button = button
        if self.button not in ["left", "right", "middle"]:
            raise ValueError("Invalid mouse button. Valid options: \"left\", \"right\", \"middle\".")
    
    def execute(self) -> None:
        timing = Timing()
        if self.x is not None and self.y is not None:
            _Move(self.x, self.y, self.physics).execute()
            click_delay = self.physics.click_delay
            if self.physics.click_delay_variation > 0:
                click_delay += random.uniform(-click_delay * self.physics.click_delay_variation, click_delay * self.physics.click_delay_variation)
                click_delay = max(0, click_delay)
            timing.wait(click_delay)
        match self.button:
            case "left": flag = 0x0004
            case "right": flag = 0x0010
            case "middle": flag = 0x0040
        ctypes.windll.user32.mouse_event(flag, 0, 0, 0, 0)