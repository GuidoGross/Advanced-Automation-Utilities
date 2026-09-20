from ._timing_action import _TimingAction
from .timing_info import TimingInfo
from ._wait import _Wait
from typing import Callable

class _WaitUntil(_TimingAction):
    def __init__(
        self,
        condition_function: Callable[[], bool],
        timeout: float = 0,
        poll_interval: float = 0.1
    ) -> None:
        self.condition_function = condition_function
        self.timeout = timeout
        self.poll_interval = poll_interval
        if self.timeout < 0: raise ValueError("Timeout cannot be negative.")
        if self.poll_interval < 0: raise ValueError("Poll interval cannot be negative.")
    
    def execute(self) -> bool:
        timing_info = TimingInfo()
        start_time = timing_info.time
        while self.timeout == 0 or timing_info.time - start_time < self.timeout:
            if self.condition_function(): return True
            _Wait(self.poll_interval).execute()
        return False