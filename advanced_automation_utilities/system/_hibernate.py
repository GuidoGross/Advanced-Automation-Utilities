from ._system_action import _SystemAction
from ..backend.windows._system import _hibernate

class _Hibernate(_SystemAction):
    def execute(self): _hibernate()