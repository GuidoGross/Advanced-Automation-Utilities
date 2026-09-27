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
        self.results: list[Any] = []
        self.last_result: Any = None
    
    def wait(self) -> None:
        """
        **Description:**

        Blocks the calling thread until the task is complete or cancelled.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        with mouse.asynchronous() as mouse_task: mouse.move(x = 500, y = 500)
        mouse_task.wait()
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
        with mouse.asynchronous() as mouse_task: mouse.move(x = 250, y = 500)
        image_found = screen.locate_image(
            image_path = "error.png",
            confidence = 0.9,
            region = [250, 250, 500, 500],
            monitor_index = 0
        )
        if image_found: mouse_task.cancel()
        ```
        """
        self._cancelled = True