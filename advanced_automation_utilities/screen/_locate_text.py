from ._screen_action import _ScreenAction
from ._ocr_utilities import _run_ocr_on_region
from ._screen_utilities import _adjust_coordinates_for_region
from typing import Optional

class _LocateText(_ScreenAction):
    def __init__(
        self,
        text: str,
        region: Optional[tuple[int, int, int, int]] = None,
        exact_match: bool = False,
        monitor_index: int = 0
    ) -> None:
        self.text = text
        self.region = region
        self.exact_match = exact_match
        self.monitor_index = monitor_index
        if self.monitor_index < 0: raise ValueError("Monitor index must be greater than or equal to 0.")
    
    def execute(self) -> tuple[Optional[int], Optional[int]]:
        result = _run_ocr_on_region(self.region, self.monitor_index)
        search_text = self.text if self.exact_match else self.text.lower()
        search_words = search_text.split()
        first_word = search_words[0]
        for line in result.lines:
            line_text = line.text if self.exact_match else line.text.lower()
            if search_text in line_text:
                for word in line.words:
                    word_text = word.text if self.exact_match else word.text.lower()
                    if first_word in word_text:
                        rectangle = word.bounding_rect
                        x = rectangle.x + rectangle.width / 2
                        y = rectangle.y + rectangle.height / 2
                        return _adjust_coordinates_for_region(x, y, self.region, self.monitor_index)
                if line.words:
                    rectangle = line.words[0].bounding_rect
                    x = rectangle.x + rectangle.width / 2
                    y = rectangle.y + rectangle.height / 2
                    return _adjust_coordinates_for_region(x, y, self.region, self.monitor_index)
        return None, None