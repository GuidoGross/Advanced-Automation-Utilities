from typing import Union
from .._utilities import _validate_options
from ..backend.windows._screen import _get_screen_resolution, _get_pixel_color, _get_work_area
from .._typing import ColorFormat

class ScreenInfo:
    """
    **Description:**

    Provides real-time information about the screen properties and state.
    """
    @property
    def resolution(self) -> tuple[int, int]:
        """
        **`ScreenInfo().resolution`:** Gets the resolution of the primary screen.

        **Description:**

        Returns the resolution of the primary screen as a tuple.

        **Returns:**

        **`tuple[int, int]`:** Format: (width, height).

        **Example:**

        ```python
        width, height = ScreenInfo().resolution
        ```
        """
        return _get_screen_resolution()
    
    @property
    def width(self) -> int:
        """
        **`ScreenInfo().width`:** Gets the width of the primary screen.

        **Description:**

        Returns only the width of the primary screen as an integer.

        **Returns:**

        **`int`**

        **Example:**

        ```python
        width = ScreenInfo().width
        ```
        """
        return self.resolution[0]

    @property
    def height(self) -> int:
        """
        **`ScreenInfo().height`:** Gets the height of the primary screen.

        **Description:**

        Returns only the height of the primary screen as an integer.

        **Returns:**

        **`int`**

        **Example:**

        ```python
        height = ScreenInfo().height
        ```
        """
        return self.resolution[1]

    def pixel_color(
        self, x: int, y: int, format: ColorFormat = "rgb"
    ) -> Union[tuple[int, int, int], str]:
        """
        **`ScreenInfo().pixel_color()`:** Gets the RGB or hexadecimal color of a specific pixel coordinate.

        **Description:**

        Returns the color of the pixel at the specified coordinates on RGB or hexadecimal format.

        **Arguments:**

        - **`x` (`int`)**
        - **`y` (`int`)**
        - **`format` (`str`):** Valid options: "rgb", "hexadecimal".

        **Returns:**

        **`Union[tuple[int, int, int], str]`:** Format: (R, G, B) for "rgb" or "#RRGGBB" for "hexadecimal".

        **Example:**

        ```python
        pixel_color = ScreenInfo().pixel_color(x = 250, y = 500, format = "hexadecimal")
        ```

        ### **Timing Utilities (timing)**

        **Delays, chronometers, and condition-based execution flow:**
        """
        _validate_options(format.lower(), ["rgb", "hexadecimal"], "color format")
        rgb_color = _get_pixel_color(x, y)
        hexadecimal_color = "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])
        match format.lower():
            case "rgb": return rgb_color
            case "hexadecimal": return hexadecimal_color
    
    @property
    def work_area(self) -> tuple[int, int, int, int]:
        """
        **`ScreenInfo().work_area`:** Gets the primary screen's work area, excluding the taskbar.

        **Description:**

        Returns the boundaries of the primary screen's usable work area. This excludes the Windows taskbar and any other docked desktop toolbars, providing the exact coordinates of the space available for applications and windows.

        **Returns:**

        **`tuple[int, int, int, int]`:** Format: (left, top, right, bottom).

        **Example:**

        ```python
        left, top, right, bottom = ScreenInfo().work_area
        ```
        """
        return _get_work_area()