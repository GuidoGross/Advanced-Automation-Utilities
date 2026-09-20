from ._system_action import _SystemAction
import subprocess

class _Shutdown(_SystemAction):
    def __init__(self, delay: int = 0) -> None:
        self.delay = delay
        if delay < 0: raise ValueError("Delay cannot be negative.")
    
    def execute(self) -> None:
        subprocess.run(["shutdown", "/s", "/t", str(self.delay)], creationflags = 0x08000000)