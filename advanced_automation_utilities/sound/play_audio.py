from ._sound_action import SoundAction
import os
import ctypes

class PlayAudio(SoundAction):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def execute(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No se ha encontrado el archivo de audio \"{self.file_path}\".")
        alias = "audio"
        ctypes.windll.winmm.mciSendStringW(f"close {alias}", None, 0, None)
        error = ctypes.windll.winmm.mciSendStringW(
            f"open \"{self.file_path}\" alias {alias}", None, 0, None
        )
        if error: raise RuntimeError("No se pudo reproducir el archivo.")
        command = f"play {alias} wait"
        ctypes.windll.winmm.mciSendStringW(command, None, 0, None)
        ctypes.windll.winmm.mciSendStringW(f"close {alias}", None, 0, None)