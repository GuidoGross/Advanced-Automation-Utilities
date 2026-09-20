from ._mouse_action import _MouseAction
from .mouse_physics import MousePhysics
from ..timing import Timing
from typing import Optional
import ctypes
import random

class _Scroll(_MouseAction):
    def __init__(
        self,
        amount: int,
        direction: str = "down",
        physics: Optional[MousePhysics] = None
    ) -> None:
        super().__init__(physics = physics)
        self.amount = amount
        self.direction = direction.lower()
        if self.amount < 0: raise ValueError("Scroll amount cannot be negative.")
        if self.direction not in ["up", "down", "left", "right"]:
            raise ValueError(
                "Invalid scroll direction. Valid options: \"up\", \"down\", \"left\", \"right\"."
            )
    
    def execute(self) -> None:
        timing = Timing()
        if self.amount == 0: return
        match self.direction:
            case "up":
                sign = 1
                scroll_flag = 0x0800
            case "down":
                sign = -1
                scroll_flag = 0x0800
            case "right":
                sign = 1
                scroll_flag = 0x1000
            case "left":
                sign = -1
                scroll_flag = 0x1000
        if self.physics.scroll_speed == 0 and self.physics.scroll_duration == 0:
            ctypes.windll.user32.mouse_event(scroll_flag, 0, 0, self.amount * sign, 0)
            return
        step = self.physics.scroll_step
        if self.physics.scroll_duration > 0:
            current_duration = self.physics.scroll_duration
            if self.physics.scroll_duration_variation > 0:
                current_duration += random.uniform(-current_duration * self.physics.scroll_duration_variation, current_duration * self.physics.scroll_duration_variation)
            current_duration = max(1e-15, current_duration)
            base_pause = (current_duration * step) / self.amount
        else:
            current_speed = self.physics.scroll_speed
            if self.physics.scroll_speed_variation > 0:
                current_speed += random.uniform(-current_speed * self.physics.scroll_speed_variation, current_speed * self.physics.scroll_speed_variation)
            current_speed = max(1e-15, current_speed)
            base_pause = step / current_speed
        remaining = self.amount
        while remaining > 0:
            current_step = step if remaining >= step else remaining
            ctypes.windll.user32.mouse_event(scroll_flag, 0, 0, current_step * sign, 0)
            pause = base_pause
            if self.physics.scroll_pause_variation > 0:
                pause += random.uniform(-pause * self.physics.scroll_pause_variation, pause * self.physics.scroll_pause_variation)
                pause = max(0, pause)
            timing.wait(pause)
            remaining -= current_step