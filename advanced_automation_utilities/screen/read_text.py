from ._screen_action import ScreenAction
from ._ocr_utilities import _run_ocr_on_region
from typing import Optional

class ReadText(ScreenAction):
    def __init__(self, region: Optional[tuple[int, int, int, int]] = None, monitor_index: int = 0):
        self.region = region
        self.monitor_index = monitor_index

    def execute(self) -> str:
        result = _run_ocr_on_region(self.region, self.monitor_index)
        return result.text