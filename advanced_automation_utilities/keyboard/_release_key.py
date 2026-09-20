from ._keyboard_action import _KeyboardAction
from .keyboard_physics import KeyboardPhysics
from ._native_keyboard import _get_virtual_key_code, _send_key
from ..timing import Timing
from typing import Optional
import random

class _ReleaseKey(_KeyboardAction):
    def __init__(self, key: str, physics: Optional[KeyboardPhysics] = None) -> None:
        super().__init__(physics = physics)
        self.key = key
        if not _get_virtual_key_code(self.key):
            raise KeyError(f"The \"{self.key}\" key is not valid or supported.")
    
    def execute(self) -> None:
        timing = Timing()
        delay = self.physics.press_delay
        if self.physics.press_delay_variation > 0:
            delay += random.uniform(-delay * self.physics.press_delay_variation, delay * self.physics.press_delay_variation)
            delay = max(0, delay)
        timing.wait(delay)
        _send_key(self.key, key_released = True)