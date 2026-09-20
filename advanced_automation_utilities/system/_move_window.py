from ._system_action import _SystemAction
import pygetwindow

class _MoveWindow(_SystemAction):
    def __init__(self, window_title: str, x: int, y: int) -> None:
        self.window_title = window_title
        self.x = x
        self.y = y
    
    def execute(self) -> None:
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        if not windows: return
        try: windows[0].moveTo(self.x, self.y)
        except pygetwindow.PyGetWindowException: pass