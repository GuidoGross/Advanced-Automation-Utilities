from ._system_action import _SystemAction
import pygetwindow

class _CloseWindow(_SystemAction):
    def __init__(self, window_title: str) -> None: self.window_title = window_title
    
    def execute(self) -> None:
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        for window in windows:
            try: window.close()
            except Exception: pass