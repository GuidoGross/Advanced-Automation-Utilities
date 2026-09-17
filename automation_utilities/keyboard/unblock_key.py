from ._keyboard_action import KeyboardAction
from ._native_keyboard import unblock_key

class UnblockKey(KeyboardAction):
    def __init__(self, key: str, physics = None):
        super().__init__(physics = physics)
        self.key = key
        
    def execute(self): unblock_key(self.key)