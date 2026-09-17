from ._mouse_physics import MousePhysics
from .move import Move
from .hold_click import HoldClick
from .release_click import ReleaseClick
from .click import Click
from .double_click import DoubleClick
from .right_click import RightClick
from .middle_click import MiddleClick
from .drag_and_drop import DragAndDrop
from .scroll import Scroll
from typing import Optional
from contextlib import contextmanager
import threading

class Mouse:
    def __init__(self, physics: Optional[MousePhysics] = None):
        self.physics = physics or MousePhysics()
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

    def move(self, x: int, y: int):
        return self._execute_or_queue(Move(x = x, y = y, physics = self.physics))
    
    def hold_click(self, x: Optional[int] = None, y: Optional[int] = None, button: str = "left"):
        return self._execute_or_queue(HoldClick(x = x, y = y, button = button, physics = self.physics))
        
    def release_click(self, x: Optional[int] = None, y: Optional[int] = None, button: str = "left"):
        return self._execute_or_queue(ReleaseClick(x = x, y = y, button = button, physics = self.physics))

    def click(self, x: Optional[int] = None, y: Optional[int] = None, button: str = "left"):
        return self._execute_or_queue(
            Click(x = x, y = y, button = button, clicks = 1, physics = self.physics)
        )
        
    def double_click(self, x: Optional[int] = None, y: Optional[int] = None, button: str = "left"):
        return self._execute_or_queue(DoubleClick(x = x, y = y, button = button, physics = self.physics))
        
    def right_click(self, x: Optional[int] = None, y: Optional[int] = None):
        return self._execute_or_queue(RightClick(x = x, y = y, physics = self.physics))
        
    def middle_click(self, x: Optional[int] = None, y: Optional[int] = None):
        return self._execute_or_queue(MiddleClick(x = x, y = y, physics = self.physics))
    
    def drag_and_drop(self, start_x: int, start_y: int, end_x: int, end_y: int, button: str = "left"):
        return self._execute_or_queue(
            DragAndDrop(
                start_x = start_x, 
                start_y = start_y, 
                end_x = end_x, 
                end_y = end_y, 
                button = button, 
                physics = self.physics
            )
        )

    def scroll(self, amount: int):
        return self._execute_or_queue(Scroll(amount = amount, physics = self.physics))