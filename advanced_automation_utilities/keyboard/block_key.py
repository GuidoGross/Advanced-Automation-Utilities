from ._keyboard_action import KeyboardAction
from ._native_keyboard import block_key

class BlockKey(KeyboardAction):
    def __init__(self, key: str, physics = None):
        super().__init__(physics = physics)
        self.key = key
        
    def execute(self): block_key(self.key)