from ._system_action import _SystemAction
import subprocess

class _SignOut(_SystemAction):
    def execute(self) -> None: subprocess.run(["shutdown", "/l"], creationflags = 0x08000000)