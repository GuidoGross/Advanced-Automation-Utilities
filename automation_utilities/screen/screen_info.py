import ctypes

class ScreenInfo:
    @property
    def resolution(self):
        width = ctypes.windll.user32.GetSystemMetrics(0)
        height = ctypes.windll.user32.GetSystemMetrics(1)
        return (width, height)

    @property
    def width(self): return ctypes.windll.user32.GetSystemMetrics(0)

    @property
    def height(self): return ctypes.windll.user32.GetSystemMetrics(1)

    def pixel_color(self, x: int, y: int, format: str = "rgb"):
        device_context = ctypes.windll.user32.GetDC(0)
        color = ctypes.windll.gdi32.GetPixel(device_context, x, y)
        ctypes.windll.user32.ReleaseDC(0, device_context)
        r = color & 0xFF
        g = (color >> 8) & 0xFF
        b = (color >> 16) & 0xFF
        rgb_color = (r, g, b)
        hexadecimal_color = "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])
        return rgb_color if format.lower() == "rgb" else hexadecimal_color