from ..backend.windows._system import _get_clipboard_text, _get_active_window_title, _is_process_running

class SystemInfo:
    """
    **Description:**

    Provides real-time information about the operating system and hardware.
    """
    @property
    def clipboard_text(self) -> str:
        """
        **Description:**

        Gets the current text content of the Windows clipboard.

        **Returns:**

        **`str`**

        **Example:**

        ```python
        text = SystemInfo().clipboard_text
        ```
        """
        return _get_clipboard_text()
    
    @property
    def active_window_title(self) -> str:
        """
        **Description:**

        Gets the title of the currently focused/active window.

        **Returns:**

        **`str`**

        **Example:**

        ```python
        title = SystemInfo().active_window_title
        ```
        """
        return _get_active_window_title()
    
    def is_process_running(self, process: str) -> bool:
        """
        **Description:**

        Checks if a specific process is currently running.

        **Arguments:**

        - **`process` (`str`)**

        **Returns:**

        **`bool`**

        **Example:**

        ```python
        is_running = SystemInfo().is_process_running("notepad.exe")
        ```
        """
        return _is_process_running(process)