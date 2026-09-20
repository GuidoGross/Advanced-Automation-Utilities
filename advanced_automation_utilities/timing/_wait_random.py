from ._timing_action import _TimingAction
from ._wait import _Wait
import random

class _WaitRandom(_TimingAction):
    def __init__(self, minimum_duration: float, maximum_duration: float) -> None:
        self.minimum_duration = minimum_duration
        self.maximum_duration = maximum_duration
        if self.minimum_duration < 0: raise ValueError("Minimum duration cannot be negative.")
        if self.maximum_duration < 0: raise ValueError("Maximum duration cannot be negative.")
        if self.minimum_duration > self.maximum_duration:
            raise ValueError("Minimum duration cannot be greater than maximum duration.")
    
    def execute(self) -> None:
        _Wait(random.uniform(self.minimum_duration, self.maximum_duration)).execute()