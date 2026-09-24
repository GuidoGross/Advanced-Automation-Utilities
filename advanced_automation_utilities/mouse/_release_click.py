from ._mouse_action import _MouseAction
from ._move import _Move
from ..utilities import _validate_mouse_button, _apply_variation
from ..timing import Timing
from ..backend.windows._mouse import _mouse_up

class _ReleaseClick(_MouseAction):
    def __init__(self, x = None, y = None, button = "left", physics = None):
        super().__init__(physics = physics)
        self.x = x
        self.y = y
        self.button = button
        _validate_mouse_button(self.button)
    
    def execute(self):
        timing = Timing()
        if self.x is not None and self.y is not None:
            _Move(self.x, self.y, self.physics).execute()
            click_delay = self.physics.click_delay
            if self.physics.click_delay_variation > 0:
                click_delay = _apply_variation(click_delay, self.physics.click_delay_variation)
                click_delay = max(0, click_delay)
            timing.wait(click_delay)
        _mouse_up(self.button)