from ._sound_action import _SoundAction
import subprocess

class _Speak(_SoundAction):
    def __init__(self, text: str) -> None: self.text = text
    
    def execute(self) -> None:
        safe_text = self.text.replace('"', '""')
        command = f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\"{safe_text}\")"
        subprocess.run(["powershell", "-Command", command], creationflags = 0x08000000)