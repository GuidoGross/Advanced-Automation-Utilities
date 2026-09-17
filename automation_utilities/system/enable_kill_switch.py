from ._system_action import SystemAction
from ..keyboard._native_keyboard import enable_kill_switch

class EnableKillSwitch(SystemAction):
    def __init__(self, *keys: str): self.keys = list(keys)

    def execute(self): enable_kill_switch(self.keys)