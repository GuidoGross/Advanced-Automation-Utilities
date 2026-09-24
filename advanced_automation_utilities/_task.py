from typing import Any
import threading

class Task:
    """
    **Description:**

    Represents an asynchronous sequence of actions.
    """
    def __init__(self) -> None:
        self._actions: list[Any] = []
        self._done_event = threading.Event()
        self._exception: Exception | None = None
        self._cancelled = False
    
    def wait(self) -> None:
        """
        **Description:**

        Blocks the calling thread until the task is complete or cancelled.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        with mouse.asynchronous() as task: mouse.move(500, 500, speed = 100)
        task.wait() # Blocks the main thread until the mouse finishes moving
        ```
        """
        self._done_event.wait()
        if self._exception: raise self._exception
    
    def cancel(self) -> None:
        """
        **Description:**

        Cancels the task if it hasn't started or is currently running.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        with mouse.asynchronous() as task: mouse.move(500, 500, speed = 100)
        if screen.locate_image("error.png"): task.cancel() # Aborts the mouse movement instantly
        ```
        """
        self._cancelled = True