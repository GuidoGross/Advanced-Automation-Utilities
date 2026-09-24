from ._sound_action import _SoundAction
from ..backend.windows._sound import _play_audio
import os

class _PlayAudio(_SoundAction):
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file \"{file_path}\" does not exist or could not be found.")
    
    def execute(self): _play_audio(self.file_path)