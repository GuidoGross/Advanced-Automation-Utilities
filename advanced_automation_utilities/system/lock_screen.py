from ._system_action import SystemAction
import ctypes

class LockScreen(SystemAction):
    def execute(self): ctypes.windll.user32.LockWorkStation()