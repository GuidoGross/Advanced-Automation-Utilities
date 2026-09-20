from ._keyboard_action import _KeyboardAction
from .keyboard_physics import KeyboardPhysics
from ._native_keyboard import _get_virtual_key_code
from ._hold_key import _HoldKey
from ._release_key import _ReleaseKey
from typing import Optional

class _PressKey(_KeyboardAction):
    def __init__(self, key: str, physics: Optional[KeyboardPhysics] = None) -> None:
        super().__init__(physics = physics)
        self.key = key
        if not _get_virtual_key_code(self.key):
            raise KeyError(f"The \"{self.key}\" key is not valid or supported.")
    
    def execute(self) -> None:
        _HoldKey(self.key, self.physics).execute()
        _ReleaseKey(self.key, self.physics).execute()