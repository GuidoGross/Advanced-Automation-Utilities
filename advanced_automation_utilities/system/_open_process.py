from ._system_action import _SystemAction
from ..backend.windows._system import _open_process
import os
import shutil

class _OpenProcess(_SystemAction):
    def __init__(self, executable_path):
        self.executable_path = executable_path
        if not (os.path.exists(self.executable_path) or shutil.which(self.executable_path)):
            raise FileNotFoundError(
                f"The executable file \"{self.executable_path}\" does not exist or could not be found."
            )
    
    def execute(self): _open_process(self.executable_path)