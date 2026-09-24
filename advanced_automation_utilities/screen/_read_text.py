from ._screen_action import _ScreenAction
from ..utilities import _validate_region
from ..backend.windows._screen import _run_ocr_on_region

class _ReadText(_ScreenAction):
    def __init__(self, region = None, monitor_index = 0):
        self.region = region
        _validate_region(self.region)
        self.monitor_index = monitor_index
        if self.monitor_index < 0: raise ValueError("Monitor index must be greater than or equal to 0.")
    
    def execute(self):
        result = _run_ocr_on_region(self.region, self.monitor_index)
        return result.text