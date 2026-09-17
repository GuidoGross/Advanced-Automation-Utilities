from ._sound_action import SoundAction
import winsound

class PlaySystemSound(SoundAction):
    def __init__(self, sound_type: str = "info"):
        self.sound_type = sound_type

    def execute(self):
        sounds = {
            "info": winsound.MB_ICONASTERISK,
            "warning": winsound.MB_ICONEXCLAMATION,
            "error": winsound.MB_ICONHAND,
            "question": winsound.MB_ICONQUESTION,
            "ok": winsound.MB_OK
        }
        sound_flag = sounds.get(self.sound_type.lower(), winsound.MB_OK)
        winsound.MessageBeep(sound_flag)