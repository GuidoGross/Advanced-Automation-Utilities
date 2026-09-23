from ._locate_image import _LocateImage
from ._read_text import _ReadText
from ._locate_text import _LocateText
from typing import Optional

class Screen:
    """
    **Description:**

    Main controller for screen interaction.
    Allows locating images, reading text (OCR), and finding text coordinates on the screen.
    """
    def locate_image(
        self,
        image_path: str,
        confidence: float = 0.9,
        region: Optional[tuple[int, int, int, int]] = None,
        monitor_index: int = 0
    ) -> tuple[Optional[int], Optional[int]]:
        """
        **Description:**

        Searches for a template image on the screen and returns its central coordinates. Supports multi-monitor setups.

        **Arguments:**

        - **`image_path`** (`str`): Must be a valid file path.
        - **`confidence`** (`float`): Must be >= 0 and <= 1.
        - **`region`** (`Optional[tuple[int, int, int, int]]`): Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height.
        - **`monitor_index`** (`int`)

        **Returns:**

        **`tuple[Optional[int], Optional[int]]`:** Format: (x, y).

        **Example:**

        ```python
        x, y = Screen().locate_image("button.png", monitor_index = 0)
        ```
        """
        return _LocateImage(
            image_path = image_path,
            confidence = confidence,
            region = region,
            monitor_index = monitor_index
        ).execute()
    
    def read_text(self, region: Optional[tuple[int, int, int, int]] = None, monitor_index: int = 0) -> str:
        """
        **Description:**

        Uses OCR to extract all readable text from the screen or a specific region. Supports multi-monitor setups.

        **Arguments:**

        - **`region`** (`Optional[tuple[int, int, int, int]]`): Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height.
        - **`monitor_index`** (`int`)

        **Returns:**

        **`str`**

        **Example:**

        ```python
        text = Screen().read_text(monitor_index = 0)
        ```
        """
        return _ReadText(region = region, monitor_index = monitor_index).execute()
    
    def locate_text(
        self,
        text: str,
        region: Optional[tuple[int, int, int, int]] = None,
        exact_match: bool = False,
        monitor_index: int = 0
    ) -> tuple[Optional[int], Optional[int]]:
        """
        **Description:**

        Uses OCR to find specific text on the screen and returns its central coordinates. Supports multi-monitor setups.

        **Arguments:**

        - **`text`** (`str`)
        - **`region`** (`Optional[tuple[int, int, int, int]]`): Format: (left, top, right, bottom). Values must be >= 0 and <= screen width/height.
        - **`exact_match`** (`bool`)
        - **`monitor_index`** (`int`)

        **Returns:**

        **`tuple[Optional[int], Optional[int]]`**

        **Example:**

        ```python
        x, y = Screen().locate_text("Submit", monitor_index = 0)
        ```
        """
        return _LocateText(
            text = text,
            region = region,
            exact_match = exact_match,
            monitor_index = monitor_index
        ).execute()