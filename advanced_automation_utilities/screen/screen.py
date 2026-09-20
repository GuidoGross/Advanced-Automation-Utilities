from ._locate_image import _LocateImage
from ._read_text import _ReadText
from ._locate_text import _LocateText
from typing import Annotated, Optional

class Screen:
    """
    Main controller for screen interaction.
    Allows locating images, reading text (OCR), and finding text coordinates on the screen.
    """
    def locate_image(
        self,
        image_path: Annotated[str, "Must be a valid file path"],
        confidence: Annotated[float, "Must be >= 0 and <= 1"] = 0.9,
        region: Annotated[
            Optional[tuple[int, int, int, int]],
            "Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height"
        ] = None,
        monitor_index: int = 0
    ) -> Annotated[tuple[Optional[int], Optional[int]], "Format: (x, y)"]:
        """
        Searches for a template image on the screen and returns its central coordinates. Supports multi-monitor setups.

        Example:
            >>> x, y = Screen().locate_image("button.png", monitor_index = 0)
        """
        return _LocateImage(
            image_path = image_path,
            confidence = confidence,
            region = region,
            monitor_index = monitor_index
        ).execute()
    
    def read_text(
        self,
        region: Annotated[
            Optional[tuple[int, int, int, int]],
            "Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height"
        ] = None,
        monitor_index: int = 0
    ) -> str:
        """
        Uses OCR to extract all readable text from the screen or a specific region. Supports multi-monitor setups.
        
        Example:
            >>> text = Screen().read_text(monitor_index = 0)
        """
        return _ReadText(region = region, monitor_index = monitor_index).execute()
    
    def locate_text(
        self,
        text: str,
        region: Annotated[
            Optional[tuple[int, int, int, int]],
            "Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height"
        ] = None,
        exact_match: bool = False,
        monitor_index: int = 0
    ) -> tuple[Optional[int], Optional[int]]:
        """
        Uses OCR to find specific text on the screen and returns its central coordinates. Supports multi-monitor setups.
        
        Example:
            >>> x, y = Screen().locate_text("Submit", monitor_index = 0)
        """
        return _LocateText(
            text = text,
            region = region,
            exact_match = exact_match,
            monitor_index = monitor_index
        ).execute()