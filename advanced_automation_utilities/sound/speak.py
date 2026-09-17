from ._sound_action import SoundAction
import subprocess

class Speak(SoundAction):
    def __init__(self, text: str): self.text = text

    def execute(self):
        safe_text = self.text.replace('"', '""')
        command = f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\"{safe_text}\")"
        subprocess.run(["powershell", "-Command", command], creationflags = 0x08000000)