from ._timing_action import _TimingAction
from .timing_info import TimingInfo
from ._wait import _Wait
from ..utilities import _validate_between_range

class _WaitUntil(_TimingAction):
    def __init__(self, condition_function, timeout = 0, poll_interval = 0.1):
        self.condition_function = condition_function
        self.timeout = timeout
        self.poll_interval = poll_interval
        _validate_between_range(timeout = self.timeout, poll_interval = self.poll_interval)
    
    def execute(self):
        timing_info = TimingInfo()
        start_time = timing_info.time
        while self.timeout == 0 or timing_info.time - start_time < self.timeout:
            if self.condition_function(): return True
            _Wait(self.poll_interval).execute()
        return False