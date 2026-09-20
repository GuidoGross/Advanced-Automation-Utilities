from ._system_action import _SystemAction
import psutil

class _KillProcess(_SystemAction):
    def __init__(self, process: str, force: bool = True) -> None:
        self.process = process
        self.force = force
    
    def execute(self) -> None:
        lower_case_process = self.process.lower()
        for process in psutil.process_iter(["name"]):
            try:
                if process.info["name"] and process.info["name"].lower() == lower_case_process:
                    process.kill() if self.force else process.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass