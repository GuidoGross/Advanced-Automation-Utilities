from ._keyboard_action import _KeyboardAction
from .keyboard_physics import KeyboardPhysics
from ._native_keyboard import _get_virtual_key_code
from ._hold_key import _HoldKey
from ._release_key import _ReleaseKey
from ..timing import Timing
from typing import Optional
import random

class _Hotkey(_KeyboardAction):
    def __init__(self, *keys: str, physics: Optional[KeyboardPhysics] = None) -> None:
        super().__init__(physics = physics)
        self.keys = keys
        for key in self.keys:
            if not _get_virtual_key_code(key):
                raise KeyError(f"The \"{key}\" key is not valid or supported.")
    
    def execute(self) -> None:
        timing = Timing()
        for i, key in enumerate(self.keys):
            _HoldKey(key, self.physics).execute()
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
        for key in reversed(self.keys): _ReleaseKey(key, self.physics).execute()