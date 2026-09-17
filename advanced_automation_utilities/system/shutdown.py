from ._system_action import SystemAction
import subprocess

class Shutdown(SystemAction):
    def __init__(self, delay: int = 0): self.delay = delay
    
    def execute(self):
        subprocess.run(["shutdown", "/s", "/t", str(self.delay)], creationflags = 0x08000000)