from ._base_click import _BaseClick
from ._hold_click import _HoldClick
from ._release_click import _ReleaseClick
from .._utilities import _validate_between_range, _apply_variation
from .._typing import MouseButton
from ..timing import Timing
from typing import Optional

class _Click(_BaseClick):
    def __init__(self, x: Optional[int] = None, y: Optional[int] = None, button: MouseButton = "left", clicks: int = 1, physics = None):
        super().__init__(x, y, button, physics)
        self.clicks = clicks
        _validate_between_range(self.clicks)
    
    def execute(self):
        self._move_if_needed()
        hold_click = _HoldClick(button = self.button, physics = self.physics)
        release_click = _ReleaseClick(button = self.button, physics = self.physics)
        for i in range(self.clicks):
            try:
                hold_click.execute()
                if i < self.clicks - 1:
                    click_duration = self.physics.click_duration
                    if self.physics.click_duration_variation > 0:
                        click_duration = _apply_variation(
                            click_duration, self.physics.click_duration_variation
                        )
                    click_duration = max(0, click_duration)
                    Timing().wait(click_duration)
            finally: release_click.execute()