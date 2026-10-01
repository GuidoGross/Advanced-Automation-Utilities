from ._system_action import _SystemAction
from .._kill_switch_event import KILL_SWITCH_EVENT
from ..backend.windows._keyboard import _disable_kill_switch

class _DisableKillSwitch(_SystemAction):
    def execute(self):
        KILL_SWITCH_EVENT.clear()
        _disable_kill_switch()