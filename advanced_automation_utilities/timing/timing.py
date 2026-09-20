from ._wait import _Wait
from ._wait_random import _WaitRandom
from ._wait_until import _WaitUntil
from typing import Annotated, Callable

class Timing:
    """
    Main controller for time-related operations.
    Allows pausing execution, waiting for conditions, and randomized delays.
    """
    def wait(self, duration: Annotated[float, "Seconds. Must be >= 0"]) -> None:
        """
        Pauses execution for an exact amount of seconds.
        
        Example:
            >>> Timing().wait(2.5)
        """
        return _Wait(duration = duration).execute()
    
    def wait_random(
        self,
        minimum_duration: Annotated[float, "Seconds. Must be >= 0"],
        maximum_duration: Annotated[float, "Seconds. Must be >= 0"]
    ) -> None:
        """
        Pauses execution for a random duration between two limits.

        Example:
            >>> Timing().wait_random(min_seconds = 1.0, max_seconds = 3.0)
        """
        return _WaitRandom(
            minimum_duration = minimum_duration, maximum_duration = maximum_duration
        ).execute()
    
    def wait_until(
        self,
        condition_function: Callable[[], bool],
        timeout: Annotated[float, "Seconds. Must be >= 0"] = 0,
        poll_interval: Annotated[float, "Seconds. Must be > 0"] = 0.1
    ) -> bool:
        """
        Halts execution until a given function or lambda condition evaluates to True.
        
        Example:
            >>> # Waits until the shift key is pressed
            >>> Timing().wait_until(lambda: KeyboardInfo().is_pressed("shift"))
        """
        return _WaitUntil(
            condition_function = condition_function,
            timeout = timeout,
            poll_interval = poll_interval
        ).execute()