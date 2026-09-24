from .keyboard_physics import KeyboardPhysics
from ._hold_key import _HoldKey
from ._release_key import _ReleaseKey
from ._press_key import _PressKey
from ._hotkey import _Hotkey
from ._block_key import _BlockKey
from ._unblock_key import _UnblockKey
from ._write import _Write
from .._queueable_controller import _QueueableController
from typing import Optional, Self

class Keyboard(_QueueableController):
    """
    **Description:**

    Main controller for keyboard automation.
    Allows pressing keys, typing text, and managing key states.
    """
    def __init__(self, physics: Optional[KeyboardPhysics] = None) -> None:
        """
        **Description:**

        Initializes the Keyboard controller.

        **Arguments:**

        - **`physics` (`Optional[KeyboardPhysics]`)**

        **Returns:**

        **`None`**
        """
        super().__init__()
        self.physics = physics or KeyboardPhysics()
    
    def hold_key(self, key: str) -> Self:
        """
        **Description:**

        Presses a key and holds it down.

        **Arguments:**

        - **`key` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().hold_key("shift")
        ```
        """
        return self._execute_or_queue(_HoldKey(key = key, physics = self.physics))
    
    def release_key(self, key: str) -> Self:
        """
        **Description:**

        Releases a previously held key.

        **Arguments:**

        - **`key` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().release_key("shift")
        ```
        """
        return self._execute_or_queue(_ReleaseKey(key = key, physics = self.physics))
    
    def press_key(self, key: str) -> Self:
        """
        **Description:**

        Presses and immediately releases a single key.

        **Arguments:**

        - **`key` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().press_key("a")
        ```
        """
        return self._execute_or_queue(_PressKey(key = key, physics = self.physics))
    
    def hotkey(self, *keys: str) -> Self:
        """
        **Description:**

        Holds down a combination of keys and releases them in reverse order.

        **Arguments:**

        - **`*keys` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().hotkey("ctrl", "c")
        ```
        """
        return self._execute_or_queue(_Hotkey(*keys, physics = self.physics))
    
    def block_key(self, key: str) -> Self:
        """
        **Description:**

        Blocks all physical input from a specific key.

        **Arguments:**

        - **`key` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().block_key("esc")
        ```
        """
        return self._execute_or_queue(_BlockKey(key = key))
    
    def unblock_key(self, key: str) -> Self:
        """
        **Description:**

        Unblocks a previously blocked key.

        **Arguments:**

        - **`key` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().unblock_key("esc")
        ```
        """
        return self._execute_or_queue(_UnblockKey(key = key))
    
    def write(self, text: str) -> Self:
        """
        **Description:**

        Types a string character by character with advanced, human-like typing error simulations, delays, and physics.

        **Arguments:**

        - **`text` (`str`)**

        **Returns:**

        **`Self`**

        **Example:**

        ```python
        Keyboard().write("Hello, world!")
        ```
        """
        return self._execute_or_queue(_Write(text = text, physics = self.physics))