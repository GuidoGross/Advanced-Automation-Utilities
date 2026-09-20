from ._system_action import _SystemAction
import pygetwindow

class _FocusWindow(_SystemAction):
    def __init__(self, window_title: str) -> None: self.window_title = window_title
    
    def execute(self) -> None:
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        if not windows: return False
        try:
            if windows[0].isMinimized: windows[0].restore()
            windows[0].activate()
            return True
        except pygetwindow.PyGetWindowException: return False