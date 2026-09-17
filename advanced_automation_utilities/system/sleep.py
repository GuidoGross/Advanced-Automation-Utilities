from ._system_action import SystemAction
import ctypes

class Sleep(SystemAction):
    def execute(self): ctypes.windll.powrprof.SetSuspendState(0, 1, 0)