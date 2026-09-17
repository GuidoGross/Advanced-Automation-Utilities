from ._system_action import SystemAction
import pyperclip

class SetClipboardText(SystemAction):
    def __init__(self, text: str): self.text = text

    def execute(self): pyperclip.copy(str(self.text))