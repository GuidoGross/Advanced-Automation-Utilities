from automation_utilities.screen import ScreenInfo
import ctypes

class MouseInfo:
    @property
    def coordinates(self) -> tuple[int, int]:
        point = _Point()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
        return (int(point.x), int(point.y))
        
    @property
    def x(self) -> int: return self.coordinates[0]
        
    @property
    def y(self) -> int: return self.coordinates[1]
        
    def pixel_color(self, format: str = "rgb"):
        return ScreenInfo().pixel_color(self.x, self.y, format = format)
        
    @property
    def on_screen(self) -> bool:
        x, y = self.coordinates
        width, height = ScreenInfo().resolution
        return 0 <= x < width and 0 <= y < height

class _Point(ctypes.Structure): _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]