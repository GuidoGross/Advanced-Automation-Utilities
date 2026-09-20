from ._system_action import _SystemAction
import ctypes

class _Sleep(_SystemAction):
    def execute(self) -> None: ctypes.windll.powrprof.SetSuspendState(0, 1, 0)