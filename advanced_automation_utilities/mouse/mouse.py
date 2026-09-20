from ._mouse_action import _MouseAction
from .mouse_physics import MousePhysics
from ._move import _Move
from ._hold_click import _HoldClick
from ._release_click import _ReleaseClick
from ._click import _Click
from ._double_click import _DoubleClick
from ._right_click import _RightClick
from ._middle_click import _MiddleClick
from ._drag_and_drop import _DragAndDrop
from ._scroll import _Scroll
from ._scroll_until import _ScrollUntil
from typing import Optional, Annotated, Callable
from contextlib import contextmanager
import threading

class Mouse:
    """
    Main controller for mouse automation.
    Allows moving the cursor, clicking, dragging, and scrolling.
    """
    def __init__(self, physics: Optional[MousePhysics] = None) -> None:
        """
        Initializes the Mouse controller.
        """
        self.physics = physics or MousePhysics()
        self._queue_mode = False
        self._queue = []
    
    @contextmanager
    def asynchronous(self) -> None:
        """
        Context manager to queue actions and execute them asynchronously.
        
        Example:
            ```python
            with mouse.asynchronous():
                mouse.move(100, 100)
                mouse.scroll(1000, "down")
            ```
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
    
    def _execute_or_queue(self, action: _MouseAction) -> None:
        self._queue.append(action) if self._queue_mode else action.execute()
        return self
    
    def move(
        self,
        x: int,
        y: int
    ) -> None:
        """
        Moves the pointer to the specified coordinates smoothly based on the configured physics.

        Example:
            ```python
            Mouse().move(x = 250, y = 500)
            ```
        """
        return self._execute_or_queue(_Move(x = x, y = y, physics = self.physics))
    
    def hold_click(
        self,
        x: Annotated[Optional[int], "Must be >= 0 and <= screen width"] = None,
        y: Annotated[Optional[int], "Must be >= 0 and <= screen height"] = None,
        button: Annotated[str, "Valid options: \"left\", \"right\", \"middle\""] = "left"
    ) -> None:
        """
        Holds down a mouse button.

        Example:
            ```python
            Mouse().hold_click()
            ```
        """
        return self._execute_or_queue(_HoldClick(x = x, y = y, button = button, physics = self.physics))
    
    def release_click(
        self,
        x: Annotated[Optional[int], "Must be >= 0 and <= screen width"] = None,
        y: Annotated[Optional[int], "Must be >= 0 and <= screen height"] = None,
        button: Annotated[str, "Valid options: \"left\", \"right\", \"middle\""] = "left"
    ) -> None:
        """
        Releases a previously held mouse button.

        Example:
            ```python
            Mouse().release_click()
            ```
        """
        return self._execute_or_queue(_ReleaseClick(x = x, y = y, button = button, physics = self.physics))

    def click(
        self, 
        x: Annotated[Optional[int], "Must be >= 0 and <= screen width"] = None, 
        y: Annotated[Optional[int], "Must be >= 0 and <= screen height"] = None, 
        button: Annotated[str, "Valid options: \"left\", \"right\", \"middle\""] = "left"
    ) -> None:
        """
        Clicks the mouse at its current position or at specified coordinates.

        Example:
            ```python
            Mouse().click()
            Mouse().click(x = 100, y = 200) # Moves before clicking
            ```
        """
        return self._execute_or_queue(
            _Click(x = x, y = y, button = button, clicks = 1, physics = self.physics)
        )
    
    def double_click(
        self,
        x: Annotated[Optional[int], "Must be >= 0 and <= screen width"] = None,
        y: Annotated[Optional[int], "Must be >= 0 and <= screen height"] = None,
        button: Annotated[str, "Valid options: \"left\", \"right\", \"middle\""] = "left"
    ) -> None:
        """
        Performs a double click.

        Example:
            ```python
            Mouse().double_click()
            ```
        """
        return self._execute_or_queue(_DoubleClick(x = x, y = y, button = button, physics = self.physics))
    
    def right_click(
        self,
        x: Annotated[Optional[int], "Must be >= 0 and <= screen width"] = None,
        y: Annotated[Optional[int], "Must be >= 0 and <= screen height"] = None
    ) -> None:
        """
        Performs a right click.

        Example:
            ```python
            Mouse().right_click()
            ```
        """
        return self._execute_or_queue(_RightClick(x = x, y = y, physics = self.physics))
    
    def middle_click(
        self,
        x: Annotated[Optional[int], "Must be >= 0 and <= screen width"] = None,
        y: Annotated[Optional[int], "Must be >= 0 and <= screen height"] = None
    ) -> None:
        """
        Performs a middle click.

        Example:
            ```python
            Mouse().middle_click()
            ```
        """
        return self._execute_or_queue(_MiddleClick(x = x, y = y, physics = self.physics))
    
    def drag_and_drop(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        button: Annotated[str, "Valid options: \"left\", \"right\", \"middle\""] = "left"
    ) -> None:
        """
        Drags an item from start to end coordinates smoothly.

        Example:
            ```python
            Mouse().drag_and_drop(start_x = 100, start_y = 100, end_x = 500, end_y = 500)
            ```
        """
        return self._execute_or_queue(
            _DragAndDrop(
                start_x = start_x, 
                start_y = start_y, 
                end_x = end_x, 
                end_y = end_y, 
                button = button, 
                physics = self.physics
            )
        )
    
    def scroll(
        self,
        amount: Annotated[int, "Must be >= 0"],
        direction: Annotated[str, "Valid options: \"up\", \"down\", \"left\", \"right\""] = "down"
    ) -> None:
        """
        Scrolls the mouse wheel by the specified amount in the specified direction.

        Example:
            ```python
            Mouse().scroll(amount = 1000, direction = "down")
            ```
        """
        return self._execute_or_queue(
            _Scroll(amount = amount, direction = direction, physics = self.physics)
        )
    
    def scroll_until(
        self,
        condition_function: Callable[[], bool],
        amount: int = 0,
        direction: Annotated[str, "Valid options: \"up\", \"down\", \"left\", \"right\""] = "down",
        timeout: float = 0,
        poll_interval: float = 0.1
    ) -> None:
        """
        Scrolls the mouse wheel continuously in the background until a given condition function evaluates to True, or an amount limit / timeout is reached.

        Example:
            ```python
            # Scrolls down infinitely until the image is found
            Mouse().scroll_until(
                condition_function = lambda: Screen().locate_image("logo.png")[0] is not None,
                direction = "down"
            )
            ```
        """
        return self._execute_or_queue(
            _ScrollUntil(
                condition_function = condition_function,
                amount = amount,
                direction = direction,
                timeout = timeout,
                poll_interval = poll_interval,
                physics = self.physics
            )
        )