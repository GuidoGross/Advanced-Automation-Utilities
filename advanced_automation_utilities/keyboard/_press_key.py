from ._keyboard_action import _KeyboardAction
from ._hold_key import _HoldKey
from ._release_key import _ReleaseKey
from ..backend.windows._keyboard import _get_virtual_key_code

class _PressKey(_KeyboardAction):
    def __init__(self, key, physics = None):
        super().__init__(physics = physics)
        self.key = key
        if not _get_virtual_key_code(self.key):
            raise KeyError(f"The \"{self.key}\" key is not valid or supported.")
    
    def execute(self):
        _HoldKey(self.key, self.physics).execute()
        _ReleaseKey(self.key, self.physics).execute()