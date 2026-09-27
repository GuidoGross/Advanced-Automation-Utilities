class WindowNotFoundError(Exception):
    """
    **`WindowNotFoundError`:** Raised when a window cannot be found.

    **Description:**

    Raised when an operation attempts to interact with a window that cannot be found or is no longer available. This usually happens if a window is abruptly closed or changes its title during execution. You can catch this exception in dynamic scenarios to trigger a retry or to fail gracefully.

    **Inherits from:**

    **`Exception`**
    """

class KillSwitchTriggered(BaseException):
    """
    **`KillSwitchTriggered`:** Raised when the global kill switch is triggered.

    **Description:**

    Raised asynchronously across all automation threads when the global kill switch shortcut is triggered.

    **Inherits from:**

    **`BaseException`**

    **Important:**

    Because it inherits directly from `BaseException` (rather than standard `Exception`), generic `except Exception:` blocks in your code will not accidentally swallow it. This design guarantees that the kill switch will always instantly and safely abort the automation sequence, no matter what your script is doing.
    """