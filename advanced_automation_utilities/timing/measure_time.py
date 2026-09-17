from ._timing_utilities import start_stop_timer
from tui_utilities import print, decimal_format
from functools import wraps

def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = start_stop_timer()
        result = function(*args, **kwargs)
        end_time = start_stop_timer()
        print([
            ("Ejecución de ", {}),
            (f"{function.__name__}()", {"color": "#00bfff"}),
            (" finalizada en ", {}),
            (f"{decimal_format((end_time - start_time) * 1000, decimals = 0)}ms", {"color": "#00bfff"})
        ], alignment = "center")
        return result
    return wrapper