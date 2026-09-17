from ._system_action import SystemAction
import subprocess

class Restart(SystemAction):
    def __init__(self, delay: int = 0): self.delay = delay
    
    def execute(self):
        subprocess.run(["shutdown", "/r", "/t", str(self.delay)], creationflags = 0x08000000)