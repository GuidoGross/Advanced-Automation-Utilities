from ._system_action import _SystemAction
from ..keyboard._native_keyboard import _enable_kill_switch

class _EnableKillSwitch(_SystemAction):
    def __init__(self, *keys: str) -> None: self.keys = list(keys)
    
    def execute(self) -> None: _enable_kill_switch(self.keys)