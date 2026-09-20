from ._timing_action import _TimingAction
import time

class _Wait(_TimingAction):
    def __init__(self, duration: float) -> None:
        if duration < 0: raise ValueError("Duration cannot be negative.")
        self.duration = duration
    
    def execute(self) -> None:
        end_time = time.perf_counter() + self.duration
        while time.perf_counter() < end_time:
            remaining = end_time - time.perf_counter()
            if remaining <= 0: break
            time.sleep(min(0.01, remaining))