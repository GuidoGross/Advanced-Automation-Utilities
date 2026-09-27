from advanced_automation_utilities.screen import ScreenInfo
from ..backend.windows._mouse import _get_cursor_position
from .._typing import ColorFormat
import mss

class MouseInfo:
    """
    **Description:**

    Provides real-time information about the mouse state.
    """
    @property
    def coordinates(self) -> tuple[int, int]:
        """
        **MouseInfo().coordinates:** Gets the current (X, Y) coordinates of the pointer.

        **Description:**

        Reads the system's pointer position and returns it as a tuple. This is an instantaneous, non-blocking hardware read.

        **Returns:**

        **`tuple[int, int]`:** Format: (x, y).

        **Example:**

        ```python
        x, y = MouseInfo().coordinates
        ```
        """
        return _get_cursor_position()
    
    @property
    def x(self) -> int:
        """
        **MouseInfo().x:** Gets the current X coordinate of the pointer.

        **Description:**

        Reads the system's pointer position and extracts only the horizontal axis value.

        **Returns:**

        **`int`**

        **Example:**

        ```python
        x = MouseInfo().x
        ```
        """
        return self.coordinates[0]
    
    @property
    def y(self) -> int:
        """
        **MouseInfo().y:** Gets the current Y coordinate of the pointer.

        **Description:**

        Reads the system's pointer position and extracts only the vertical axis value.

        **Returns:**

        **`int`**

        **Example:**

        ```python
        y = MouseInfo().y
        ```
        """
        return self.coordinates[1]
    
    def pixel_color(self, format: ColorFormat = "rgb") -> tuple[int, int, int] | str:
        """
        **MouseInfo().pixel_color():** Gets the RGB or hexadecimal color of the pixel currently under the pointer.

        **Description:**

        Takes a micro-screenshot of the exact pixel the mouse is hovering over and extracts its color.

        **Arguments:**

        - **`format` (`str`):** Valid options: "rgb", "hexadecimal".

        **Returns:**

        **`None`**

        **Example:**

        ```python
        color = MouseInfo().pixel_color(format = "rgb")
        ```
        """
        return ScreenInfo().pixel_color(self.x, self.y, format = format)
    
    @property
    def on_screen(self) -> bool:
        """
        **MouseInfo().on_screen:** Checks if the pointer is currently within the bounds of any screen.

        **Description:**

        Verifies if the current mouse coordinates fall inside the desktop's virtual screen boundaries. Useful for multi-monitor setups.

        **Returns:**

        **`bool`**

        **Example:**

        ```python
        is_pointer_on_screen = MouseInfo().on_screen
        ```

        ### **Keyboard Utilities (keyboard)**

        **Low-level keyboard interaction and information retrieval:**
        """
        x, y = self.coordinates
        with mss.mss() as screen_capture_tool:
            virtual = screen_capture_tool.monitors[0]
            return (
                virtual["left"] <= x < virtual["left"] + virtual["width"] and virtual["top"] <= y < virtual["top"] + virtual["height"]
            )