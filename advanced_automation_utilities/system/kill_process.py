from ._system_action import SystemAction
import psutil

class KillProcess(SystemAction):
    def __init__(self, process: str, force: bool = True):
        self.process = process
        self.force = force
    
    def execute(self):
        lower_case_process = self.process.lower()
        for process in psutil.process_iter(["name"]):
            try:
                if process.info["name"] and process.info["name"].lower() == lower_case_process:
                    process.kill() if self.force else process.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass