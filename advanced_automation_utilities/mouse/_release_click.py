from ._base_click import _BaseClick
from ..backend.windows._mouse import _mouse_up

class _ReleaseClick(_BaseClick):
    def execute(self):
        self._move_if_needed()
        _mouse_up(self.button)