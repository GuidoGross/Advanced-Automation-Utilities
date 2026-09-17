from ._mouse_action import MouseAction
from ._mouse_physics import MousePhysics
from ..timing import Timing
from typing import Optional
import ctypes
import random

class Scroll(MouseAction):
    def __init__(
        self,
        amount: int,
        physics: Optional[MousePhysics] = None
    ):
        super().__init__(physics = physics)
        self.amount = amount
    
    def execute(self):
        timing = Timing()
        if self.amount == 0: return
        if self.physics.scroll_speed == 0 and self.physics.scroll_duration == 0:
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, self.amount, 0)
            return
        step = self.physics.scroll_step
        if self.physics.scroll_duration > 0:
            current_duration = self.physics.scroll_duration
            if self.physics.scroll_duration_variation > 0:
                current_duration += random.uniform(-current_duration * self.physics.scroll_duration_variation, current_duration * self.physics.scroll_duration_variation)
            current_duration = max(1e-15, current_duration)
            base_pause = (current_duration * step) / abs(self.amount)
        else:
            current_speed = self.physics.scroll_speed
            if self.physics.scroll_speed_variation > 0:
                current_speed += random.uniform(-current_speed * self.physics.scroll_speed_variation, current_speed * self.physics.scroll_speed_variation)
            current_speed = max(1e-15, current_speed)
            base_pause = step / current_speed
        sign = 1 if self.amount > 0 else -1
        remaining = abs(self.amount)
        while remaining > 0:
            current_step = step if remaining >= step else remaining
            ctypes.windll.user32.mouse_event(0x0800, 0, 0, current_step * sign, 0)
            pause = base_pause
            if self.physics.scroll_pause_variation > 0:
                pause += random.uniform(-pause * self.physics.scroll_pause_variation, pause * self.physics.scroll_pause_variation)
                pause = max(0, pause)
            timing.wait(pause)
            remaining -= current_step