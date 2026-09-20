from ._system_action import _SystemAction
from ..keyboard._native_keyboard import _disable_kill_switch

class _DisableKillSwitch(_SystemAction):
    def execute(self) -> None: _disable_kill_switch()