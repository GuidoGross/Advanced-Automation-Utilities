from ._system_action import SystemAction
import pygetwindow

class MoveWindow(SystemAction):
    def __init__(self, window_title: str, x: int, y: int):
        self.window_title = window_title
        self.x = x
        self.y = y
    
    def execute(self):
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        if not windows: return False
        try:
            windows[0].moveTo(self.x, self.y)
            return True
        except Exception: return False