from ._keyboard_action import KeyboardAction
from ._keyboard_physics import KeyboardPhysics
from ._native_keyboard import send_key
from ..timing import Timing
from typing import Optional
import random

class ReleaseKey(KeyboardAction):
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
        send_key(self.key, key_released = True)