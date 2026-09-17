from ._keyboard_action import KeyboardAction
from ._keyboard_physics import KeyboardPhysics
from .hold_key import HoldKey
from .release_key import ReleaseKey
from ..timing import Timing
from typing import Optional
import random

class Hotkey(KeyboardAction):
    def __init__(self, *keys: str, physics: Optional[KeyboardPhysics] = None):
        super().__init__(physics = physics)
        self.keys = keys

    def execute(self):
        timing = Timing()
        for i, key in enumerate(self.keys):
            HoldKey(key, self.physics).execute()
            if i < len(self.keys) - 1:
                delay = self.physics.hotkey_delay
                if self.physics.hotkey_delay_variation > 0:
                    delay += random.uniform(-delay * self.physics.hotkey_delay_variation, delay * self.physics.hotkey_delay_variation)
                delay = max(0, delay)
                timing.wait(delay)
        duration = self.physics.press_duration
        if self.physics.press_duration_variation > 0:
            duration += random.uniform(-duration * self.physics.press_duration_variation, duration * self.physics.press_duration_variation)
        duration = max(0, duration)
        timing.wait(duration)
        for key in reversed(self.keys): ReleaseKey(key, self.physics).execute()