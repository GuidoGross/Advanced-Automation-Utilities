from advanced_automation_utilities.screen import ScreenInfo
from ..backend.windows._mouse import _get_cursor_position
import mss

class MouseInfo:
    """
    **Description:**

    Provides real-time information about the mouse state.
    """
    @property
    def coordinates(self) -> tuple[int, int]:
        """
        **Description:**

        Gets the current (X, Y) coordinates of the pointer.

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
        **Description:**

        Gets the current X coordinate of the pointer.

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
        **Description:**

        Gets the current Y coordinate of the pointer.

        **Returns:**

        **`int`**

        **Example:**

        ```python
        y = MouseInfo().y
        ```
        """
        return self.coordinates[1]
    
    def pixel_color(self, format: str = "rgb") -> None:
        """
        **Description:**

        Gets the RGB color of the pixel currently under the pointer.

        **Arguments:**

        - **`format` (`str`):** Valid options: "rgb", "hexadecimal".

        **Returns:**

        **`None`**

        **Example:**

        ```python
        r, g, b = MouseInfo().pixel_color()
        ```
        """
        return ScreenInfo().pixel_color(self.x, self.y, format = format)
    
    @property
    def on_screen(self) -> bool:
        """
        **Description:**

        Checks if the pointer is currently within the bounds of any screen.

        **Returns:**

        **`bool`**

        **Example:**

        ```python
        is_visible = MouseInfo().on_screen
        ```
        """
        x, y = self.coordinates
        with mss.mss() as screen_capture_tool:
            virtual = screen_capture_tool.monitors[0]
            return (
                virtual["left"] <= x < virtual["left"] + virtual["width"] and virtual["top"] <= y < virtual["top"] + virtual["height"]
            )