from ._timing_action import TimingAction
from .wait import Wait
import random

class WaitRandom(TimingAction):
    def __init__(self, minimum_seconds: float, maximum_seconds: float):
        self.minimum_seconds = minimum_seconds
        self.maximum_seconds = maximum_seconds

    def execute(self): Wait(random.uniform(self.minimum_seconds, self.maximum_seconds)).execute()