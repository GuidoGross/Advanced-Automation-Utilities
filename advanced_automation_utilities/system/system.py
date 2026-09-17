from ._system_action import SystemAction
from .set_clipboard_text import SetClipboardText
from .open_process import OpenProcess
from .kill_process import KillProcess
from .focus_window import FocusWindow
from .close_window import CloseWindow
from .lock_screen import LockScreen
from .sign_out import SignOut
from .sleep import Sleep
from .hibernate import Hibernate
from .shutdown import Shutdown
from .restart import Restart
from .enable_kill_switch import EnableKillSwitch
from .disable_kill_switch import DisableKillSwitch
from .move_window import MoveWindow
from .resize_window import ResizeWindow
from contextlib import contextmanager
import threading

class System:
    def __init__(self):
        self._queue = []
        self._queue_mode = False
    
    def _execute_or_queue(self, action: SystemAction):
        self._queue.append(action) if self._queue_mode else action.execute()
        return self
    
    @contextmanager
    def asynchronous(self):
        self._queue_mode = True
        self._queue.clear()
        try: yield self
        finally:
            self._queue_mode = False
            if self._queue:
                actions_to_run = list(self._queue)
                def run_actions():
                    for action in actions_to_run: action.execute()
                threading.Thread(target = run_actions, daemon = True).start()
            self._queue.clear()
    
    def set_clipboard_text(self, text: str): return self._execute_or_queue(SetClipboardText(text = text))
    
    def open_process(self, executable_path: str):
        return self._execute_or_queue(OpenProcess(executable_path = executable_path))
    
    def kill_process(self, process: str, force: bool = True):
        return self._execute_or_queue(KillProcess(process = process, force = force))
        
    def focus_window(self, window_title: str):
        return self._execute_or_queue(FocusWindow(window_title = window_title))
    
    def resize_window(self, window_title: str, width: int, height: int):
        return self._execute_or_queue(
            ResizeWindow(window_title = window_title, width = width, height = height)
        )
    
    def move_window(self, window_title: str, x: int, y: int):
        return self._execute_or_queue(MoveWindow(window_title = window_title, x = x, y = y))
    
    def close_window(self, window_title: str):
        return self._execute_or_queue(CloseWindow(window_title = window_title))
    
    def lock_screen(self): return self._execute_or_queue(LockScreen())
    
    def sign_out(self): return self._execute_or_queue(SignOut())
    
    def sleep(self): return self._execute_or_queue(Sleep())
    
    def hibernate(self): return self._execute_or_queue(Hibernate())
    
    def shutdown(self, delay: int = 0): return self._execute_or_queue(Shutdown(delay = delay))
    
    def restart(self, delay: int = 0): return self._execute_or_queue(Restart(delay = delay))
    
    def enable_kill_switch(self, *keys: str):
        if not keys: keys = ("ctrl", "shift", "alt", "k")
        return self._execute_or_queue(EnableKillSwitch(*keys))
        
    def disable_kill_switch(self):
        return self._execute_or_queue(DisableKillSwitch())