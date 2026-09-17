from ._system_action import SystemAction
import subprocess

class Hibernate(SystemAction):
    def execute(self): subprocess.run(["shutdown", "/h"], creationflags = 0x08000000)