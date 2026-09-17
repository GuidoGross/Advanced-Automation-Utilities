from ._keyboard_action import KeyboardAction
from ._keyboard_physics import KeyboardPhysics
from ._native_keyboard import send_key
from ..timing import Timing
from typing import Optional
import random

class HoldKey(KeyboardAction):
    def __init__(self, key: str, physics: Optional[KeyboardPhysics] = None):
        super().__init__(physics = physics)
        self.key = key

    def execute(self):
        timing = Timing()
        delay = self.physics.press_delay
        if self.physics.press_delay_variation > 0:
            delay += random.uniform(-delay * self.physics.press_delay_variation, delay * self.physics.press_delay_variation)
            delay = max(0, delay)
        timing.wait(delay)
        send_key(self.key, key_released = False)
        duration = self.physics.press_duration
        if self.physics.press_duration_variation > 0:
            duration += random.uniform(-duration * self.physics.press_duration_variation, duration * self.physics.press_duration_variation)
            duration = max(0, duration)
        if self.physics.auto_repeat and duration > 0.5:
            timing.wait(0.5)
            remaining_duration = duration - 0.5
            repeat_interval = 0.033
            while remaining_duration > 0:
                if remaining_duration < repeat_interval:
                    timing.wait(remaining_duration)
                    break
                send_key(self.key, key_released = False)
                timing.wait(repeat_interval)
                remaining_duration -= repeat_interval
        else: timing.wait(duration)