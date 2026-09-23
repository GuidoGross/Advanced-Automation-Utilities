import time

class TimingInfo:
    """
    **Description:**

    Class that provides instantaneous timing information.
    """
    @property
    def time(self) -> float:
        """
        **Description:**

        Returns the current time in seconds.

        **Returns:**

        **`float`**

        **Example:**

        ```python
        current_time = TimingInfo().time
        ```
        """
        return time.time()