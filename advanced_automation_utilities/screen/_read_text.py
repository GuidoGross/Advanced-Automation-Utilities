from ._screen_action import _ScreenAction
from ._ocr_utilities import _run_ocr_on_region
from typing import Optional

class _ReadText(_ScreenAction):
    def __init__(
        self,
        region: Optional[tuple[int, int, int, int]] = None,
        monitor_index: int = 0
    ) -> None:
        self.region = region
        self.monitor_index = monitor_index
        if self.monitor_index < 0: raise ValueError("Monitor index must be greater than or equal to 0.")
    
    def execute(self) -> str:
        result = _run_ocr_on_region(self.region, self.monitor_index)
        return result.text