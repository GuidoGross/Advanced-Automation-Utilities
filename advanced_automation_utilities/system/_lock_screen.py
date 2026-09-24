from ._system_action import _SystemAction
from ..backend.windows._system import _lock_screen

class _LockScreen(_SystemAction):
    def execute(self): _lock_screen()