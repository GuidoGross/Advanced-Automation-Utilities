from ._base_click import _BaseClick
from .._utilities import _apply_variation
from ..backend.windows._mouse import _mouse_down
from ..timing import Timing

class _HoldClick(_BaseClick):
    def execute(self):
        self._move_if_needed()
        _mouse_down(self.button)
        click_duration = self.physics.click_duration
        if self.physics.click_duration_variation > 0:
            click_duration = _apply_variation(click_duration, self.physics.click_duration_variation)
            click_duration = max(0, click_duration)
        Timing().wait(click_duration)