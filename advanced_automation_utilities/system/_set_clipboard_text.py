from ._system_action import _SystemAction
import pyperclip

class _SetClipboardText(_SystemAction):
    def __init__(self, text: str) -> None: self.text = text
    
    def execute(self) -> None: pyperclip.copy(str(self.text))