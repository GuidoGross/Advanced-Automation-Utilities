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
from .._queueable_controller import _QueueableController

class System(_QueueableController):
    """
    **Description:**

    Main controller for system-level operations.
    Allows managing windows, processes, clipboard, and power states.
    """
    def __init__(self) -> None:
        """
        **Description:**

        Initializes the System controller.

        **Returns:**

        **`None`**
        """
        super().__init__()
    
    def set_clipboard_text(self, text: str) -> None:
        """
        **Description:**

        Sets the text content of the Windows clipboard.

        **Arguments:**

        - **`text`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().set_clipboard_text("Text to paste later")
        ```
        """
        return self._execute_or_queue(_SetClipboardText(text = text))
    
    def open_process(self, executable_path: str) -> None:
        """
        **Description:**

        Opens a process or file with optional arguments.

        **Arguments:**

        - **`executable_path`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().open_process("notepad.exe")
        ```
        """
        return self._execute_or_queue(_OpenProcess(executable_path = executable_path))
    
    def kill_process(self, process: str, force: bool = True) -> None:
        """
        **Description:**

        Terminates an active process by its name.

        **Arguments:**

        - **`process`** (`str`)
        - **`force`** (`bool`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().kill_process("notepad.exe", force = True)
        ```
        """
        return self._execute_or_queue(_KillProcess(process = process, force = force))
    
    def focus_window(self, window_title: str) -> None:
        """
        **Description:**

        Brings a specific window to the foreground by its title.

        **Arguments:**

        - **`window_title`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().focus_window("Untitled - Notepad")
        ```
        """
        return self._execute_or_queue(_FocusWindow(window_title = window_title))
    
    def resize_window(self, window_title: str, width: int, height: int) -> None:
        """
        **Description:**

        Resizes a specific window to the specified dimensions by its title.

        **Arguments:**

        - **`window_title`** (`str`)
        - **`width`** (`int`): Must be > 0.
        - **`height`** (`int`): Must be > 0.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().resize_window("Untitled - Notepad", width = 800, height = 600)
        ```
        """
        return self._execute_or_queue(
            _ResizeWindow(window_title = window_title, width = width, height = height)
        )
    
    def move_window(self, window_title: str, x: int, y: int) -> None:
        """
        **Description:**

        Moves a specific window to the specified coordinates by its title.

        **Arguments:**

        - **`window_title`** (`str`)
        - **`x`** (`int`)
        - **`y`** (`int`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().move_window("Untitled - Notepad", x = 100, y = 100)
        ```
        """
        return self._execute_or_queue(_MoveWindow(window_title = window_title, x = x, y = y))
    
    def close_window(self, window_title: str) -> None:
        """
        **Description:**

        Gently closes a specific window by its title.

        **Arguments:**

        - **`window_title`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().close_window("Untitled - Notepad")
        ```
        """
        return self._execute_or_queue(_CloseWindow(window_title = window_title))
    
    def lock_screen(self) -> None: 
        """
        **Description:**

        Locks the Windows session (Win+L).

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().lock_screen()
        ```
        """
        return self._execute_or_queue(_LockScreen())
    
    def sign_out(self) -> None: 
        """
        **Description:**

        Signs out the current Windows user.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().sign_out()
        ```
        """
        return self._execute_or_queue(_SignOut())
    
    def sleep(self) -> None: 
        """
        **Description:**

        Puts the computer into sleep mode.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().sleep()
        ```
        """
        return self._execute_or_queue(_Sleep())
    
    def hibernate(self) -> None: 
        """
        **Description:**

        Puts the computer into hibernation mode.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().hibernate()
        ```
        """
        return self._execute_or_queue(_Hibernate())
    
    def shutdown(self, delay: int = 0) -> None:
        """
        **Description:**

        Turns off the computer.

        **Arguments:**

        - **`delay`** (`int`): Seconds. Must be >= 0.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().shutdown()
        ```
        """
        return self._execute_or_queue(_Shutdown(delay = delay))
    
    def restart(self, delay: int = 0) -> None:
        """
        **Description:**

        Restarts the computer.

        **Arguments:**

        - **`delay`** (`int`): Seconds. Must be >= 0.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().restart()
        ```
        """
        return self._execute_or_queue(_Restart(delay = delay))
    
    def enable_kill_switch(self, *keys: str) -> None:
        """
        **Description:**

        Enables a global kill switch (Ctrl + Shift + Alt + K by default) to abort execution instantly.

        **Arguments:**

        - **`*keys`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().enable_kill_switch()
        ```
        """
        if not keys: keys = ("ctrl", "shift", "alt", "k")
        return self._execute_or_queue(_EnableKillSwitch(*keys))
    
    def disable_kill_switch(self) -> None: 
        """
        **Description:**

        Disables the global kill switch.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        System().disable_kill_switch()
        ```
        """
        return self._execute_or_queue(_DisableKillSwitch())