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
from .._queueable_controller import _QueueableController
from typing import Optional, Callable

class Mouse(_QueueableController):
    """
    **Description:**

    Main controller for mouse automation.
    Allows moving the cursor, clicking, dragging, and scrolling.
    """
    def __init__(self, physics: Optional[MousePhysics] = None) -> None:
        """
        **Description:**

        Initializes the Mouse controller.

        **Arguments:**

        - **`physics`** (`Optional[MousePhysics]`)

        **Returns:**

        **`None`**
        """
        super().__init__()
        self.physics = physics or MousePhysics()
    
    def move(self, x: int, y: int) -> None:
        """
        **Description:**

        Moves the pointer to the specified coordinates smoothly based on the configured physics.

        **Arguments:**

        - **`x`** (`int`)
        - **`y`** (`int`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Mouse().move(x = 250, y = 500)
        ```
        """
        return self._execute_or_queue(_Move(x = x, y = y, physics = self.physics))
    
    def hold_click(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left"
    ) -> None:
        """
        **Description:**

        Holds down a mouse button.

        **Arguments:**

        - **`x`** (`Optional[int]`): Must be >= 0 and <= screen width.
        - **`y`** (`Optional[int]`): Must be >= 0 and <= screen height.
        - **`button`** (`str`): Valid options: "left", "right", "middle".

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Mouse().hold_click()
        ```
        """
        return self._execute_or_queue(_HoldClick(x = x, y = y, button = button, physics = self.physics))
    
    def release_click(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left"
    ) -> None:
        """
        **Description:**

        Releases a previously held mouse button.

        **Arguments:**

        - **`x`** (`Optional[int]`): Must be >= 0 and <= screen width.
        - **`y`** (`Optional[int]`): Must be >= 0 and <= screen height.
        - **`button`** (`str`): Valid options: "left", "right", "middle".

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Mouse().release_click()
        ```
        """
        return self._execute_or_queue(_ReleaseClick(x = x, y = y, button = button, physics = self.physics))

    def click(
        self, 
        x: Optional[int] = None, 
        y: Optional[int] = None, 
        button: str = "left"
    ) -> None:
        """
        **Description:**

        Clicks the mouse at its current position or at specified coordinates.

        **Arguments:**

        - **`x`** (`Optional[int]`): Must be >= 0 and <= screen width.
        - **`y`** (`Optional[int]`): Must be >= 0 and <= screen height.
        - **`button`** (`str`): Valid options: "left", "right", "middle".

        **Returns:**

        **`None`**

        **Example:**

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
        x: Optional[int] = None,
        y: Optional[int] = None,
        button: str = "left"
    ) -> None:
        """
        **Description:**

        Performs a double click.

        **Arguments:**

        - **`x`** (`Optional[int]`): Must be >= 0 and <= screen width.
        - **`y`** (`Optional[int]`): Must be >= 0 and <= screen height.
        - **`button`** (`str`): Valid options: "left", "right", "middle".

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Mouse().double_click()
        ```
        """
        return self._execute_or_queue(_DoubleClick(x = x, y = y, button = button, physics = self.physics))
    
    def right_click(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """
        **Description:**

        Performs a right click.

        **Arguments:**

        - **`x`** (`Optional[int]`): Must be >= 0 and <= screen width.
        - **`y`** (`Optional[int]`): Must be >= 0 and <= screen height.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Mouse().right_click()
        ```
        """
        return self._execute_or_queue(_RightClick(x = x, y = y, physics = self.physics))
    
    def middle_click(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """
        **Description:**

        Performs a middle click.

        **Arguments:**

        - **`x`** (`Optional[int]`): Must be >= 0 and <= screen width.
        - **`y`** (`Optional[int]`): Must be >= 0 and <= screen height.

        **Returns:**

        **`None`**

        **Example:**

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
        button: str = "left"
    ) -> None:
        """
        **Description:**

        Drags an item from start to end coordinates smoothly.

        **Arguments:**

        - **`start_x`** (`int`)
        - **`start_y`** (`int`)
        - **`end_x`** (`int`)
        - **`end_y`** (`int`)
        - **`button`** (`str`): Valid options: "left", "right", "middle".

        **Returns:**

        **`None`**

        **Example:**

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
    
    def scroll(self, amount: int, direction: str = "down") -> None:
        """
        **Description:**

        Scrolls the mouse wheel by the specified amount in the specified direction.

        **Arguments:**

        - **`amount`** (`int`): Must be >= 0.
        - **`direction`** (`str`): Valid options: "up", "down", "left", "right".

        **Returns:**

        **`None`**

        **Example:**

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
        direction: str = "down",
        timeout: float = 0,
        poll_interval: float = 0.1
    ) -> None:
        """
        **Description:**

        Scrolls the mouse wheel continuously in the background until a given condition function evaluates to True, or an amount limit / timeout is reached.

        **Arguments:**

        - **`condition_function`** (`Callable[[], bool]`)
        - **`amount`** (`int`)
        - **`direction`** (`str`): Valid options: "up", "down", "left", "right".
        - **`timeout`** (`float`)
        - **`poll_interval`** (`float`)

        **Returns:**

        **`None`**

        **Example:**

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