import pyperclip
import pygetwindow
import psutil

class SystemInfo:
    @property
    def clipboard_text(self) -> str: return pyperclip.paste()
        
    @property
    def active_window_title(self) -> str:
        active_window = pygetwindow.getActiveWindow()
        return active_window.title if active_window else ""
        
    def is_process_running(self, process: str) -> bool:
        lower_case_process = process.lower()
        for process in psutil.process_iter(["name"]):
            try:
                if process.info["name"] and process.info["name"].lower() == lower_case_process:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass
        return False