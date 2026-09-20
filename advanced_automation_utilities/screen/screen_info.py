from typing import Annotated, Union
import ctypes

class ScreenInfo:
    """
    Provides real-time information about the screen properties and state.
    """
    @property
    def resolution(self) -> Annotated[tuple[int, int], "Format: (width, height)"]:
        """
        Gets the (width, height) resolution of the primary screen.

        Example:
            ```python
            width, height = ScreenInfo().resolution
            ```
        """
        width = ctypes.windll.user32.GetSystemMetrics(0)
        height = ctypes.windll.user32.GetSystemMetrics(1)
        return (width, height)
    
    @property
    def width(self) -> int:
        """
        Gets the width of the primary screen.

        Example:
            ```python
            width = ScreenInfo().width
            ```
        """
        return ctypes.windll.user32.GetSystemMetrics(0)

    @property
    def height(self) -> int:
        """
        Gets the height of the primary screen.

        Example:
            ```python
            height = ScreenInfo().height
            ```
        """
        return ctypes.windll.user32.GetSystemMetrics(1)

    def pixel_color(
        self,
        x: int,
        y: int,
        format: Annotated[str, "Valid options: \"rgb\", \"hexadecimal\""] = "rgb"
    ) -> Annotated[
            Union[tuple[int, int, int], str],
            "Format: (R, G, B) for \"rgb\" or \"#RRGGBB\" for \"hexadecimal\""
        ]:
        """
        Gets the RGB color of a specific pixel coordinate.

        Example:
            ```python
            r, g, b = ScreenInfo().pixel_color(250, 500)
            ```
        """
        if format.lower() not in ["rgb", "hexadecimal"]:
            raise ValueError("Invalid color format. Valid options: \"rgb\", \"hexadecimal\".")
        device_context = ctypes.windll.user32.GetDC(0)
        color = ctypes.windll.gdi32.GetPixel(device_context, x, y)
        ctypes.windll.user32.ReleaseDC(0, device_context)
        r = color & 0xFF
        g = (color >> 8) & 0xFF
        b = (color >> 16) & 0xFF
        rgb_color = (r, g, b)
        hexadecimal_color = "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])
        match format.lower():
            case "rgb": return rgb_color
            case "hexadecimal": return hexadecimal_color