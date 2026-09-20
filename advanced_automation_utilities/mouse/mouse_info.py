from advanced_automation_utilities.screen import ScreenInfo
from typing import Annotated
import ctypes

class MouseInfo:
    """
    Provides real-time information about the mouse state.
    """
    @property
    def coordinates(self) -> Annotated[tuple[int, int], "Format: (x, y)"]:
        """
        Gets the current (X, Y) coordinates of the pointer.

        Example:
        ```python
        x, y = MouseInfo().coordinates
        ```
        """
        point = _Point()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
        return (int(point.x), int(point.y))
    
    @property
    def x(self) -> int:
        """
        Gets the current X coordinate of the pointer.

        Example:
        ```python
        x = MouseInfo().x
        ```
        """
        return self.coordinates[0]
    
    @property
    def y(self) -> int:
        """
        Gets the current Y coordinate of the pointer.

        Example:
        ```python
        y = MouseInfo().y
        ```
        """
        return self.coordinates[1]
    
    def pixel_color(
        self,
        format: Annotated[str, "Valid options: \"rgb\", \"hexadecimal\""] = "rgb"
    ) -> None:
        """
        Gets the RGB color of the pixel currently under the pointer.
        
        Example:
        ```python
        r, g, b = MouseInfo().pixel_color()
        ```
        """
        return ScreenInfo().pixel_color(self.x, self.y, format = format)
    
    @property
    def on_screen(self) -> bool:
        """
        Checks if the pointer is currently within the bounds of any screen.
        
        Example:
        ```python
        is_visible = MouseInfo().on_screen
        ```
        """
        x, y = self.coordinates
        width, height = ScreenInfo().resolution
        return 0 <= x < width and 0 <= y < height

class _Point(ctypes.Structure): _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]