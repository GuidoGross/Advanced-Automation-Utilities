from ._screen_action import ScreenAction
from ._screen_utilities import adjust_coordinates_for_region
from typing import Optional
import os
import cv2
import numpy

class LocateImage(ScreenAction):
    def __init__(
        self,
        image_path: str,
        confidence: float = 0.9,
        region: Optional[tuple[int, int, int, int]] = None,
        monitor_index: int = 0
    ):
        self.image_path = image_path
        self.confidence = confidence
        self.region = region
        self.monitor_index = monitor_index

    def execute(self) -> tuple[Optional[int], Optional[int]]:
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"No se ha encontrado la imagen \"{self.image_path}\".")
        try:
            template = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
            if template is None: return None, None
            from ._screen_utilities import take_screenshot
            screenshot = take_screenshot(self.region, self.monitor_index)
            image = numpy.array(screenshot)
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            _, max_value, _, max_location = cv2.minMaxLoc(result)
            if max_value >= self.confidence:
                height, width = template.shape[:2]
                x = max_location[0] + width / 2
                y = max_location[1] + height / 2
                return adjust_coordinates_for_region(x, y, self.region, self.monitor_index)
        except Exception: pass
        return None, None