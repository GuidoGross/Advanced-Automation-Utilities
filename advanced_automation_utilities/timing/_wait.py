from ._timing_action import _TimingAction
from ..utilities import _validate_between_range
import time

class _Wait(_TimingAction):
    def __init__(self, duration):
        _validate_between_range(duration = duration)
        self.duration = duration
    
    def execute(self):
        end_time = time.perf_counter() + self.duration
        while time.perf_counter() < end_time:
            remaining = end_time - time.perf_counter()
            if remaining <= 0: break
            time.sleep(min(0.01, remaining))