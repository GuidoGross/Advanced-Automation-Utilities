from ._keyboard_action import KeyboardAction
from ._keyboard_physics import KeyboardPhysics
from .hold_key import HoldKey
from .release_key import ReleaseKey
from typing import Optional

class PressKey(KeyboardAction):
    def __init__(self, key: str, physics: Optional[KeyboardPhysics] = None):
        super().__init__(physics = physics)
        self.key = key

    def execute(self):
        HoldKey(self.key, self.physics).execute()
        ReleaseKey(self.key, self.physics).execute()