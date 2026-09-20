from ._system_action import _SystemAction
import os
import shutil

class _OpenProcess(_SystemAction):
    def __init__(self, executable_path: str) -> None:
        self.executable_path = executable_path
        if not (os.path.exists(self.executable_path) or shutil.which(self.executable_path)):
            raise FileNotFoundError(
                f"The executable file \"{self.executable_path}\" does not exist or could not be found."
            )
    
    def execute(self) -> None: os.startfile(self.executable_path)