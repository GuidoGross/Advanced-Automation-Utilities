from .locate_image import LocateImage
from .read_text import ReadText
from .locate_text import LocateText
from typing import Optional

class Screen:
    def locate_image(
        self,
        image_path: str,
        confidence: float = 0.9,
        region: Optional[tuple[int, int, int, int]] = None,
        monitor_index: int = 0
    ) -> tuple[Optional[int], Optional[int]]:
        return LocateImage(
            image_path = image_path,
            confidence = confidence,
            region = region,
            monitor_index = monitor_index
        ).execute()

    def read_text(
        self,
        region: Optional[tuple[int, int, int, int]] = None,
        monitor_index: int = 0
    ) -> str:
        return ReadText(region = region, monitor_index = monitor_index).execute()
        
    def locate_text(
        self, 
        text: str,
        region: Optional[tuple[int, int, int, int]] = None,
        exact_match: bool = False,
        monitor_index: int = 0
    ) -> tuple[Optional[int], Optional[int]]:
        return LocateText(
            text = text,
            region = region,
            exact_match = exact_match,
            monitor_index = monitor_index
        ).execute()