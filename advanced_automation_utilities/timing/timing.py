from ._wait import _Wait
from ._wait_random import _WaitRandom
from ._wait_until import _WaitUntil
from typing import Callable

class Timing:
    """
    **Description:**

    Main controller for time-related operations.
    Allows pausing execution, waiting for conditions, and randomized delays.
    """
    def wait(self, duration: float) -> None:
        """
        **Description:**

        Pauses execution for an exact amount of seconds.

        **Arguments:**

        - **`duration` (`float`):** Seconds. Must be >= 0.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Timing().wait(2.5)
        ```
        """
        return _Wait(duration = duration).execute()
    
    def wait_random(self, minimum_duration: float, maximum_duration: float) -> None:
        """
        **Description:**

        Pauses execution for a random duration between two limits.

        **Arguments:**

        - **`minimum_duration` (`float`):** Seconds. Must be >= 0.
        - **`maximum_duration` (`float`):** Seconds. Must be >= 0.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Timing().wait_random(minimum_duration = 1.0, maximum_duration = 3.0)
        ```
        """
        return _WaitRandom(
            minimum_duration = minimum_duration, maximum_duration = maximum_duration
        ).execute()
    
    def wait_until(
        self,
        condition_function: Callable[[], bool],
        timeout: float = 0,
        poll_interval: float = 0.1
    ) -> bool:
        """
        **Description:**

        Halts execution until a given function or lambda condition evaluates to True.

        **Arguments:**

        - **`condition_function` (`Callable[[], bool]`)**
        - **`timeout` (`float`):** Seconds. Must be >= 0.
        - **`poll_interval` (`float`):** Seconds. Must be > 0.

        **Returns:**

        **`bool`**

        **Example:**

        ```python
        # Waits until the shift key is pressed
        Timing().wait_until(lambda: KeyboardInfo().is_pressed("shift"))
        ```
        """
        return _WaitUntil(
            condition_function = condition_function,
            timeout = timeout,
            poll_interval = poll_interval
        ).execute()