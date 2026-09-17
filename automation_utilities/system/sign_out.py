from ._system_action import SystemAction
import subprocess

class SignOut(SystemAction):
    def execute(self): subprocess.run(["shutdown", "/l"], creationflags = 0x08000000)