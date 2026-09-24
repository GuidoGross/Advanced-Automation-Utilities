from ._system_action import _SystemAction
from ..backend.windows._system import _sign_out

class _SignOut(_SystemAction):
    def execute(self): _sign_out()