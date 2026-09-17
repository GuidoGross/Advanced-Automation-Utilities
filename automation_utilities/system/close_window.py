from ._system_action import SystemAction
import pygetwindow

class CloseWindow(SystemAction):
    def __init__(self, window_title: str): self.window_title = window_title
    
    def execute(self):
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        for window in windows:
            try: window.close()
            except Exception: pass