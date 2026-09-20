from ._keyboard_action import _KeyboardAction
from ._native_keyboard import _get_virtual_key_code, _block_key

class _BlockKey(_KeyboardAction):
    def __init__(self, key: str) -> None:
        if not _get_virtual_key_code(key): raise KeyError(f"The \"{key}\" key is not valid or supported.")
        super().__init__()
        self.key = key
    
    def execute(self) -> None: _block_key(self.key)