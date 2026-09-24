from ._mouse_action import _MouseAction
from ._move import _Move
from ._hold_click import _HoldClick
from ._release_click import _ReleaseClick
from ..utilities import _validate_mouse_button, _apply_variation
from ..timing import Timing

class _Click(_MouseAction):
    def __init__(self, x = None, y = None, button = "left", clicks = 1, physics = None):
        super().__init__(physics = physics)
        self.x = x
        self.y = y
        self.button = button
        self.clicks = clicks
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
        hold_click = _HoldClick(button = self.button, physics = self.physics)
        release_click = _ReleaseClick(button = self.button, physics = self.physics)
        for i in range(self.clicks):
            hold_click.execute()
            release_click.execute()
            if i < self.clicks - 1:
                click_duration = self.physics.click_duration
                if self.physics.click_duration_variation > 0:
                    click_duration = _apply_variation(
                        click_duration, self.physics.click_duration_variation
                    )
                click_duration = max(0, click_duration)
                timing.wait(click_duration)