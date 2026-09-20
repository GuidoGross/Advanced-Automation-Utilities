from ._system_action import _SystemAction
import pygetwindow

class _ResizeWindow(_SystemAction):
    def __init__(
        self,
        window_title: str,
        width: int,
        height: int
    ) -> None: 
        self.window_title = window_title
        self.width = width
        self.height = height
    
    def execute(self) -> None:
        windows = pygetwindow.getWindowsWithTitle(self.window_title)
        if not windows: return
        try: windows[0].resizeTo(self.width, self.height)
        except pygetwindow.PyGetWindowException: pass