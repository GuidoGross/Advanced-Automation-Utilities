from .timing_info import TimingInfo
from tui_utilities import print, decimal_format
from functools import wraps
from typing import Callable, Any

def measure_time(function: Callable) -> Callable:
    """
    A decorator to automatically measure and print the execution time of any function.
    
    Example:
        >>> @measure_time
        >>> def heavy_task(): pass
    """
    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        timing_info = TimingInfo()
        start_time = timing_info.time
        result = function(*args, **kwargs)
        end_time = timing_info.time
        print([
            ("Ejecución de ", {}),
            (f"{function.__name__}()", {"color": "#00bfff"}),
            (" finalizada en ", {}),
            (f"{decimal_format((end_time - start_time) * 1000, decimals = 0)}ms", {"color": "#00bfff"})
        ], alignment = "center")
        return result
    
    return wrapper