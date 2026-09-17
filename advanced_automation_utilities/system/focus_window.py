from ._system_action import SystemAction
import pygetwindow

class FocusWindow(SystemAction):
    def __init__(self, window_title: str): self.window_title = window_title
    
    def execute(self):
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        if not windows: return False
        try:
            if windows[0].isMinimized: windows[0].restore()
            windows[0].activate()
            return True
        except Exception: return False