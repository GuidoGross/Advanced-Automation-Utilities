from ._sound_action import _SoundAction
import winsound

class _PlaySystemSound(_SoundAction):
    def __init__(self, sound_type: str) -> None:
        self.sound_type = sound_type
        if self.sound_type.lower() not in ["info", "warning", "error", "question", "ok"]:
            raise ValueError(
                "Invalid sound type. Valid options: \"info\", \"warning\", \"error\", \"question\", \"ok\"."
            )
    
    def execute(self) -> None:
        sounds = {
            "info": winsound.MB_ICONASTERISK,
            "warning": winsound.MB_ICONEXCLAMATION,
            "error": winsound.MB_ICONHAND,
            "question": winsound.MB_ICONQUESTION,
            "ok": winsound.MB_OK
        }
        sound_flag = sounds.get(self.sound_type.lower(), winsound.MB_OK)
        winsound.MessageBeep(sound_flag)