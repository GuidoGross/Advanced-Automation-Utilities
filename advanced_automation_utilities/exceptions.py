class WindowNotFoundError(Exception):
    """
    **Description:**

    Raised when a specified window cannot be found.
    """

class KillSwitchTriggered(BaseException):
    """
    **Description:**

    Raised asynchronously when the Kill Switch is triggered.
    """