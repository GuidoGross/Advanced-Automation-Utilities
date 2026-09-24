from typing import Union
from ..backend.windows._screen import _get_screen_resolution, _get_pixel_color, _get_work_area

class ScreenInfo:
    """
    **Description:**

    Provides real-time information about the screen properties and state.
    """
    @property
    def resolution(self) -> tuple[int, int]:
        """
        **Description:**

        Gets the (width, height) resolution of the primary screen.

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
        **Description:**

        Gets the width of the primary screen.

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
        **Description:**

        Gets the height of the primary screen.

        **Returns:**

        **`int`**

        **Example:**

        ```python
        height = ScreenInfo().height
        ```
        """
        return self.resolution[1]

    def pixel_color(self, x: int, y: int, format: str = "rgb") -> Union[tuple[int, int, int], str]:
        """
        **Description:**

        Gets the RGB color of a specific pixel coordinate.

        **Arguments:**

        - **`x` (`int`)**
        - **`y` (`int`)**
        - **`format` (`str`):** Valid options: "rgb", "hexadecimal".

        **Returns:**

        **`Union[tuple[int, int, int], str]`:** Format: (R, G, B) for "rgb" or "#RRGGBB" for "hexadecimal".

        **Example:**

        ```python
        r, g, b = ScreenInfo().pixel_color(250, 500)
        ```
        """
        if format.lower() not in ["rgb", "hexadecimal"]:
            raise ValueError("Invalid color format. Valid options: \"rgb\", \"hexadecimal\".")
        rgb_color = _get_pixel_color(x, y)
        hexadecimal_color = "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])
        match format.lower():
            case "rgb": return rgb_color
            case "hexadecimal": return hexadecimal_color
    
    @property
    def work_area(self) -> tuple[int, int, int, int]:
        """
        **Description:**

        Gets the primary screen's work area, excluding the taskbar.

        **Returns:**

        **`tuple[int, int, int, int]`:** Format: (left, top, right, bottom).

        **Example:**

        ```python
        left, top, right, bottom = ScreenInfo().work_area
        ```
        """
        return _get_work_area()