from ._system_action import SystemAction
from ..keyboard._native_keyboard import disable_kill_switch

class DisableKillSwitch(SystemAction):
    def execute(self): disable_kill_switch()