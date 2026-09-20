import time

class TimingInfo:
    """
    Class that provides instantaneous timing information.
    """
    @property
    def time(self) -> float:
        """
        Returns the current time in seconds.
        
        Example:
        ```python
        current_time = TimingInfo().time
        ```
        """
        return time.time()