from ._native_keyboard import _get_virtual_key_code, _is_pressed

class KeyboardInfo:
    """
    Provides real-time information about the keyboard state.
    """
    def is_pressed(self, key: str) -> bool: 
        """
        Returns True if the specified key is currently physically pressed down.
        
        Example:
        ```python
        is_shift_down = KeyboardInfo().is_pressed("shift")
        ```
        """
        if not _get_virtual_key_code(key): raise KeyError(f"The \"{key}\" key is not valid or supported.")
        return _is_pressed(key)