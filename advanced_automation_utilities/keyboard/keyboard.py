from ._keyboard_physics import KeyboardPhysics
from .hold_key import HoldKey
from .release_key import ReleaseKey
from .press_key import PressKey
from .hotkey import Hotkey
from .block_key import BlockKey
from .unblock_key import UnblockKey
from .write import Write
from typing import Optional
from contextlib import contextmanager
import threading

class Keyboard:
    def __init__(self, physics: Optional[KeyboardPhysics] = None):
        self.physics = physics or KeyboardPhysics()
        self._queue_mode = False
        self._queue = []

    @contextmanager
    def asynchronous(self):
        self._queue_mode = True
        self._queue.clear()
        try: yield self
        finally:
            self._queue_mode = False
            if self._queue:
                queue_copy = list(self._queue)
                self._queue.clear()
                def worker(actions):
                    for action in actions: action.execute()
                thread = threading.Thread(target = worker, args = (queue_copy,), daemon = True)
                thread.start()

    def _execute_or_queue(self, action):
        self._queue.append(action) if self._queue_mode else action.execute()
        return self

    def hold_key(self, key: str):
        return self._execute_or_queue(HoldKey(key = key, physics = self.physics))

    def release_key(self, key: str):
        return self._execute_or_queue(ReleaseKey(key = key, physics = self.physics))

    def press_key(self, key: str):
        return self._execute_or_queue(PressKey(key = key, physics = self.physics))
    
    def hotkey(self, *keys: str): return self._execute_or_queue(Hotkey(*keys, physics = self.physics))
    
    def block_key(self, key: str):
        return self._execute_or_queue(BlockKey(key = key, physics = self.physics))

    def unblock_key(self, key: str):
        return self._execute_or_queue(UnblockKey(key = key, physics = self.physics))

    def write(self, text: str): return self._execute_or_queue(Write(text = text, physics = self.physics))