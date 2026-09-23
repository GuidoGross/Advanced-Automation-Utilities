from contextlib import contextmanager
from typing import Generator, Any
import threading

class _QueueableController:
    def __init__(self) -> None:
        self._queue_mode = False
        self._queue = []
    
    @contextmanager
    def asynchronous(self) -> Generator["_QueueableController", None, None]:
        """
        **Description:**

        Context manager to queue actions and execute them asynchronously.

        **Returns:**

        **`Generator["_QueueableController", None, None]`**

        **Example:**

        ```python
        with controller.asynchronous():
            controller.action_1()
            controller.action_2()
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
    
    def _execute_or_queue(self, action: Any) -> Any:
        self._queue.append(action) if self._queue_mode else action.execute()
        return self