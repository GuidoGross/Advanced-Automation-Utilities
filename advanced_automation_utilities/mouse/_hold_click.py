from ._mouse_action import _MouseAction
from .mouse_physics import MousePhysics
from ._move import _Move
from ..timing import Timing
from typing import Optional
import random
import ctypes

class _HoldClick(_MouseAction):
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
            case "left": flag = 0x0002
            case "right": flag = 0x0008
            case "middle": flag = 0x0020
        ctypes.windll.user32.mouse_event(flag, 0, 0, 0, 0)
        click_duration = self.physics.click_duration
        if self.physics.click_duration_variation > 0:
            click_duration += random.uniform(-click_duration * self.physics.click_duration_variation, click_duration * self.physics.click_duration_variation)
            click_duration = max(0, click_duration)
        timing.wait(click_duration)