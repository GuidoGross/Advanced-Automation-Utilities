from ._mouse_action import MouseAction
from ._mouse_physics import MousePhysics
from .move import Move
from ..timing import Timing
from typing import Optional
import random
import ctypes

class Click(MouseAction):
    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left",
        clicks: int = 1,
        physics: Optional[MousePhysics] = None
    ):
        super().__init__(physics = physics)
        self.x = x
        self.y = y
        self.button = button
        self.clicks = clicks

    def execute(self):
        timing = Timing()
        if self.x is not None and self.y is not None:
            Move(self.x, self.y, self.physics).execute()
            click_delay = self.physics.click_delay
            if self.physics.click_delay_variation > 0:
                click_delay += random.uniform(-click_delay * self.physics.click_delay_variation, click_delay * self.physics.click_delay_variation)
                click_delay = max(0, click_delay)
            timing.wait(click_delay)
        for i in range(self.clicks):
            flag = 0x0002
            if self.button == "right": flag = 0x0008
            elif self.button == "middle": flag = 0x0020
            ctypes.windll.user32.mouse_event(flag, 0, 0, 0, 0)
            click_duration = self.physics.click_duration
            if self.physics.click_duration_variation > 0:
                click_duration += random.uniform(-click_duration * self.physics.click_duration_variation, click_duration * self.physics.click_duration_variation)
                click_duration = max(0, click_duration)
            timing.wait(click_duration)
            flag = 0x0004
            if self.button == "right": flag = 0x0010
            elif self.button == "middle": flag = 0x0040
            ctypes.windll.user32.mouse_event(flag, 0, 0, 0, 0)
            if i < self.clicks - 1:
                click_duration = self.physics.click_duration
                if self.physics.click_duration_variation > 0:
                    click_duration += random.uniform(-click_duration * self.physics.click_duration_variation, click_duration * self.physics.click_duration_variation)
                    click_duration = max(0, click_duration)
                timing.wait(click_duration)