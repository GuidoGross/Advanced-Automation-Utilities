from ._timing_action import TimingAction
from .wait import Wait
from ._timing_utilities import start_stop_timer
from typing import Callable

class WaitUntil(TimingAction):
    def __init__(
        self,
        condition_function: Callable[[], bool],
        timeout: float = 0,
        poll_interval: float = 0.1
    ):
        self.condition_function = condition_function
        self.timeout = timeout
        self.poll_interval = poll_interval

    def execute(self) -> bool:
        start_time = start_stop_timer()
        while self.timeout == 0 or start_stop_timer() - start_time < self.timeout:
            if self.condition_function(): return True
            Wait(self.poll_interval).execute()
        return False