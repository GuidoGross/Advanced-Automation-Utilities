from ._system_action import SystemAction
import pygetwindow

class ResizeWindow(SystemAction):
    def __init__(self, window_title: str, width: int, height: int):
        self.window_title = window_title
        self.width = width
        self.height = height
    
    def execute(self):
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        if not windows: return False
        try:
            windows[0].resizeTo(self.width, self.height)
            return True
        except Exception: return False