from .wait import Wait
from .wait_random import WaitRandom
from .wait_until import WaitUntil
from typing import Callable

class Timing:
    def wait(self, seconds: float): return Wait(seconds = seconds).execute()

    def wait_random(self, minimum_seconds: float, maximum_seconds: float):
        return WaitRandom(minimum_seconds = minimum_seconds, maximum_seconds = maximum_seconds).execute()

    def wait_until(
        self,
        condition_function: Callable[[], bool],
        timeout: float = 0,
        poll_interval: float = 0.1
    ) -> bool:
        return WaitUntil(
            condition_function = condition_function,
            timeout = timeout,
            poll_interval = poll_interval
        ).execute()