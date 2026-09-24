from ._system_action import _SystemAction
from ..backend.windows._keyboard import _disable_kill_switch

class _DisableKillSwitch(_SystemAction):
    def execute(self): _disable_kill_switch()