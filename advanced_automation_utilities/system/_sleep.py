from ._system_action import _SystemAction
from ..backend.windows._system import _sleep

class _Sleep(_SystemAction):
    def execute(self): _sleep()