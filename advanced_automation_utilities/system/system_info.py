import pyperclip
import pygetwindow
import psutil

class SystemInfo:
    """
    Provides real-time information about the operating system and hardware.
    """
    @property
    def clipboard_text(self) -> str:
        """
        Gets the current text content of the Windows clipboard.

        Example:
            >>> text = SystemInfo().clipboard_text
        """
        return pyperclip.paste()
    
    @property
    def active_window_title(self) -> str:
        """
        Gets the title of the currently focused/active window.

        Example:
            >>> title = SystemInfo().active_window_title
        """
        active_window = pygetwindow.getActiveWindow()
        return active_window.title if active_window else ""
    
    def is_process_running(self, process: str) -> bool:
        """
        Checks if a specific process is currently running.
        
        Example:
            >>> is_running = SystemInfo().is_process_running("notepad.exe")
        """
        lower_case_process = process.lower()
        for process in psutil.process_iter(["name"]):
            try:
                if process.info["name"] and process.info["name"].lower() == lower_case_process: return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass
        return False