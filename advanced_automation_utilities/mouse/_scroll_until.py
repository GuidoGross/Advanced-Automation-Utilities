from ._mouse_action import _MouseAction
from .mouse_physics import MousePhysics
from ._scroll import _Scroll
from ..timing import Timing, TimingInfo
from typing import Callable, Optional
import threading

class _ScrollUntil(_MouseAction):
    def __init__(
        self,
        condition_function: Callable[[], bool],
        amount: int = 0,
        direction: str = "down",
        timeout: float = 0,
        poll_interval: float = 0.1,
        physics: Optional[MousePhysics] = None
    ) -> None:
        super().__init__(physics = physics)
        self.condition_function = condition_function
        self.amount = amount
        self.direction = direction.lower()
        self.timeout = timeout
        self.poll_interval = poll_interval
        if self.amount < 0: raise ValueError("Scroll amount cannot be negative.")
        if self.direction not in ["up", "down", "left", "right"]:
            raise ValueError(
                "Invalid scroll direction. Valid options: \"up\", \"down\", \"left\", \"right\"."
            )
        if self.timeout < 0: raise ValueError("Wait time cannot be negative.")
        if self.poll_interval < 0: raise ValueError("Poll interval cannot be negative.")
    
    def execute(self) -> bool:
        stop_scroll = False
        timing = Timing()
        timing_info = TimingInfo()
        scrolled = 0
        limit = self.amount if self.amount > 0 else float("inf")
        step = self.physics.scroll_step

        def scroller() -> None:
            nonlocal scrolled
            while not stop_scroll and scrolled < limit:
                current_step = step if (limit - scrolled) >= step else int(limit - scrolled)
                _Scroll(
                    amount = current_step, direction = self.direction, physics = self.physics
                ).execute()
                scrolled += current_step
        
        scroll_thread = threading.Thread(target = scroller, daemon = True)
        scroll_thread.start()
        start_time = timing_info.time
        condition_met = False
        while self.timeout == 0 or timing_info.time - start_time < self.timeout:
            if self.condition_function():
                condition_met = True
                break
            if not scroll_thread.is_alive(): break
            timing.wait(self.poll_interval)
        stop_scroll = True
        scroll_thread.join()
        return condition_met