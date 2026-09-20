from ._system_action import _SystemAction
import ctypes

class _LockScreen(_SystemAction):
    def execute(self) -> None: ctypes.windll.user32.LockWorkStation()