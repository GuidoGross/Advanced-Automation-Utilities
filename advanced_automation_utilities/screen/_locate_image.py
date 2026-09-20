from ._screen_action import _ScreenAction
from ._screen_utilities import _adjust_coordinates_for_region
from typing import Optional
import os
import cv2
import numpy

class _LocateImage(_ScreenAction):
    def __init__(
        self,
        image_path: str,
        confidence: float = 0.9,
        region: Optional[tuple[int, int, int, int]] = None,
        monitor_index: int = 0
    ) -> None:
        self.image_path = image_path
        self.confidence = confidence
        self.region = region
        self.monitor_index = monitor_index
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(
                f"Image file \"{self.image_path}\" does not exist or could not be found."
            )
        if not (0 <= self.confidence <= 1): raise ValueError("Confidence must be between 0 and 1.")
        if self.monitor_index < 0: raise ValueError("Monitor index must be greater than or equal to 0.")
    
    def execute(self) -> tuple[Optional[int], Optional[int]]:
        try:
            template = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
            if template is None: return None, None
            from ._screen_utilities import _take_screenshot
            screenshot = _take_screenshot(self.region, self.monitor_index)
            image = numpy.array(screenshot)
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            _, max_value, _, max_location = cv2.minMaxLoc(result)
            if max_value >= self.confidence:
                height, width = template.shape[:2]
                x = max_location[0] + width / 2
                y = max_location[1] + height / 2
                return _adjust_coordinates_for_region(x, y, self.region, self.monitor_index)
        except Exception: pass
        return None, None