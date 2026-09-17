from ._system_action import SystemAction
import os

class OpenProcess(SystemAction):
    def __init__(self, executable_path: str): self.executable_path = executable_path

    def execute(self): os.startfile(self.executable_path)