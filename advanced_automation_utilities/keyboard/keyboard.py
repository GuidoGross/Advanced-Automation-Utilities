from ._keyboard_action import _KeyboardAction
from .keyboard_physics import KeyboardPhysics
from ._hold_key import _HoldKey
from ._release_key import _ReleaseKey
from ._press_key import _PressKey
from ._hotkey import _Hotkey
from ._block_key import _BlockKey
from ._unblock_key import _UnblockKey
from ._write import _Write
from typing import Optional
from contextlib import contextmanager
import threading

class Keyboard:
    """
    Main controller for keyboard automation.
    Allows pressing keys, typing text, and managing key states.
    """
    def __init__(self, physics: Optional[KeyboardPhysics] = None) -> None:
        """
        Initializes the Keyboard controller.
        """
        self.physics = physics or KeyboardPhysics()
        self._queue_mode = False
        self._queue = []
    
    @contextmanager
    def asynchronous(self) -> None:
        """
        Context manager to queue actions and execute them asynchronously.

        Example:
            >>> with keyboard.asynchronous():
            ...     keyboard.write("Hello")
            ...     keyboard.press_key("enter")
        """
        self._queue_mode = True
        self._queue.clear()
        try: yield self
        finally:
            self._queue_mode = False
            if self._queue:
                queue_copy = list(self._queue)
                self._queue.clear()

                def worker(actions: list) -> None:
                    for action in actions: action.execute()
                
                thread = threading.Thread(target = worker, args = (queue_copy,), daemon = True)
                thread.start()
    
    def _execute_or_queue(self, action: _KeyboardAction) -> None:
        self._queue.append(action) if self._queue_mode else action.execute()
        return self
    
    def hold_key(self, key: str) -> None:
        """
        Presses a key and holds it down.

        Example:
            >>> Keyboard().hold_key("shift")
        """
        return self._execute_or_queue(_HoldKey(key = key, physics = self.physics))
    
    def release_key(self, key: str) -> None:
        """
        Releases a previously held key.

        Example:
            >>> Keyboard().release_key("shift")
        """
        return self._execute_or_queue(_ReleaseKey(key = key, physics = self.physics))
    
    def press_key(self, key: str) -> None:
        """
        Presses and immediately releases a single key.

        Example:
            >>> Keyboard().press_key("a")
        """
        return self._execute_or_queue(_PressKey(key = key, physics = self.physics))
    
    def hotkey(self, *keys: str) -> None:
        """
        Holds down a combination of keys and releases them in reverse order.

        Example:
            >>> Keyboard().hotkey("ctrl", "c")
        """
        return self._execute_or_queue(_Hotkey(*keys, physics = self.physics))
    
    def block_key(self, key: str) -> None:
        """
        Blocks all physical input from a specific key.

        Example:
            >>> Keyboard().block_key("esc")
        """
        return self._execute_or_queue(_BlockKey(key = key))
    
    def unblock_key(self, key: str) -> None:
        """
        Unblocks a previously blocked key.
        
        Example:
            >>> Keyboard().unblock_key("esc")
        """
        return self._execute_or_queue(_UnblockKey(key = key))
    
    def write(self, text: str) -> None:
        """
        Types a string character by character with advanced, human-like typing error simulations, delays, and physics.
        
        Example:
            >>> Keyboard().write("Hello, world!")
        """
        return self._execute_or_queue(_Write(text = text, physics = self.physics))