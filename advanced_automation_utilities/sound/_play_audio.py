from ._sound_action import _SoundAction
import os
import ctypes

class _PlayAudio(_SoundAction):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file \"{file_path}\" does not exist or could not be found.")
    
    def execute(self) -> None:
        alias = "audio"
        ctypes.windll.winmm.mciSendStringW(f"close {alias}", None, 0, None)
        error = ctypes.windll.winmm.mciSendStringW(
            f"open \"{self.file_path}\" alias {alias}", None, 0, None
        )
        if error: raise RuntimeError("Could not play the audio file.")
        command = f"play {alias} wait"
        ctypes.windll.winmm.mciSendStringW(command, None, 0, None)
        ctypes.windll.winmm.mciSendStringW(f"close {alias}", None, 0, None)