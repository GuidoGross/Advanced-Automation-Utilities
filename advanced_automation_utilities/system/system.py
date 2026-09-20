from ._system_action import _SystemAction
from ._set_clipboard_text import _SetClipboardText
from ._open_process import _OpenProcess
from ._kill_process import _KillProcess
from ._focus_window import _FocusWindow
from ._resize_window import _ResizeWindow
from ._move_window import _MoveWindow
from ._close_window import _CloseWindow
from ._lock_screen import _LockScreen
from ._sign_out import _SignOut
from ._sleep import _Sleep
from ._hibernate import _Hibernate
from ._shutdown import _Shutdown
from ._restart import _Restart
from ._enable_kill_switch import _EnableKillSwitch
from ._disable_kill_switch import _DisableKillSwitch
from contextlib import contextmanager
import threading
from typing import Annotated

class System:
    """
    Main controller for system-level operations.
    Allows managing windows, processes, clipboard, and power states.
    """
    def __init__(self) -> None:
        """
        Initializes the System controller.
        """
        self._queue = []
        self._queue_mode = False
    
    def _execute_or_queue(self, action: _SystemAction) -> None:
        self._queue.append(action) if self._queue_mode else action.execute()
        return self
    
    @contextmanager
    def asynchronous(self) -> None:
        """
        Context manager to queue actions and execute them asynchronously.

        Example:
            >>> with system.asynchronous():
            ...     system.open_process("notepad.exe")
            ...     system.focus_window("Notepad")
        """
        self._queue_mode = True
        self._queue.clear()
        try: yield self
        finally:
            self._queue_mode = False
            if self._queue:
                actions_to_run = list(self._queue)
                
                def run_actions() -> None:
                    for action in actions_to_run: action.execute()
                
                threading.Thread(target = run_actions, daemon = True).start()
            self._queue.clear()
    
    def set_clipboard_text(self, text: str) -> None:
        """
        Sets the text content of the Windows clipboard.

        Example:
            >>> System().set_clipboard_text("Text to paste later")
        """
        return self._execute_or_queue(_SetClipboardText(text = text))
    
    def open_process(self, executable_path: str) -> None:
        """
        Opens a process or file with optional arguments.

        Example:
            >>> System().open_process("notepad.exe")
        """
        return self._execute_or_queue(_OpenProcess(executable_path = executable_path))
    
    def kill_process(self, process: str, force: bool = True) -> None:
        """
        Terminates an active process by its name.

        Example:
            >>> System().kill_process("notepad.exe", force = True)
        """
        return self._execute_or_queue(_KillProcess(process = process, force = force))
    
    def focus_window(self, window_title: str) -> None:
        """
        Brings a specific window to the foreground by its title.

        Example:
            >>> System().focus_window("Untitled - Notepad")
        """
        return self._execute_or_queue(_FocusWindow(window_title = window_title))
    
    def resize_window(
        self, 
        window_title: str, 
        width: Annotated[int, "Must be > 0"], 
        height: Annotated[int, "Must be > 0"]
    ) -> None:
        """
        Resizes a specific window to the specified dimensions by its title.

        Example:
            >>> System().resize_window("Untitled - Notepad", width = 800, height = 600)
        """
        return self._execute_or_queue(
            _ResizeWindow(window_title = window_title, width = width, height = height)
        )
    
    def move_window(self, window_title: str, x: int, y: int) -> None:
        """
        Moves a specific window to the specified coordinates by its title.

        Example:
            >>> System().move_window("Untitled - Notepad", x = 100, y = 100)
        """
        return self._execute_or_queue(_MoveWindow(window_title = window_title, x = x, y = y))
    
    def close_window(self, window_title: str) -> None:
        """
        Gently closes a specific window by its title.

        Example:
            >>> System().close_window("Untitled - Notepad")
        """
        return self._execute_or_queue(_CloseWindow(window_title = window_title))
    
    def lock_screen(self) -> None: 
        """
        Locks the Windows session (Win+L).

        Example:
            >>> System().lock_screen()
        """
        return self._execute_or_queue(_LockScreen())
    
    def sign_out(self) -> None: 
        """
        Signs out the current Windows user.

        Example:
            >>> System().sign_out()
        """
        return self._execute_or_queue(_SignOut())
    
    def sleep(self) -> None: 
        """
        Puts the computer into sleep mode.

        Example:
            >>> System().sleep()
        """
        return self._execute_or_queue(_Sleep())
    
    def hibernate(self) -> None: 
        """
        Puts the computer into hibernation mode.

        Example:
            >>> System().hibernate()
        """
        return self._execute_or_queue(_Hibernate())
    
    def shutdown(self, delay: Annotated[int, "Seconds. Must be >= 0"] = 0) -> None:
        """
        Turns off the computer.

        Example:
            >>> System().shutdown()
        """
        return self._execute_or_queue(_Shutdown(delay = delay))
    
    def restart(self, delay: Annotated[int, "Seconds. Must be >= 0"] = 0) -> None:
        """
        Restarts the computer.

        Example:
            >>> System().restart()
        """
        return self._execute_or_queue(_Restart(delay = delay))
    
    def enable_kill_switch(self, *keys: str) -> None:
        """
        Enables a global kill switch (Ctrl + Shift + Alt + K by default) to abort execution instantly.
        
        Example:
            >>> System().enable_kill_switch()
        """
        if not keys: keys = ("ctrl", "shift", "alt", "k")
        return self._execute_or_queue(_EnableKillSwitch(*keys))
    
    def disable_kill_switch(self) -> None: 
        """
        Disables the global kill switch.
        
        Example:
            >>> System().disable_kill_switch()
        """
        return self._execute_or_queue(_DisableKillSwitch())