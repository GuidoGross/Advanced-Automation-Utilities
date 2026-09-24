from ._screen_action import _ScreenAction
from ..utilities import _validate_region
from ..backend.windows._screen import _locate_image
import os

class _LocateImage(_ScreenAction):
    def __init__(self, image_path, confidence = 0.9, region = None, monitor_index = 0):
        self.image_path = image_path
        self.confidence = confidence
        self.region = region
        _validate_region(self.region)
        self.monitor_index = monitor_index
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(
                f"Image file \"{self.image_path}\" does not exist or could not be found."
            )
        if not (0 <= self.confidence <= 1): raise ValueError("Confidence must be between 0 and 1.")
        if self.monitor_index < 0: raise ValueError("Monitor index must be greater than or equal to 0.")
    
    def execute(self):
        return _locate_image(self.image_path, self.confidence, self.region, self.monitor_index)