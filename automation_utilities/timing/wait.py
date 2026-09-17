from ._timing_action import TimingAction
import time

class Wait(TimingAction):
    def __init__(self, seconds: float): self.seconds = seconds

    def execute(self):
        end_time = time.perf_counter() + self.seconds
        while time.perf_counter() < end_time:
            remaining = end_time - time.perf_counter()
            if remaining <= 0: break
            time.sleep(min(0.01, remaining))