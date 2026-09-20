from ._system_action import _SystemAction
import subprocess

class _Hibernate(_SystemAction):
    def execute(self) -> None: subprocess.run(["shutdown", "/h"], creationflags = 0x08000000)