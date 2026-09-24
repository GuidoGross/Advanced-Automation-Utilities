from ._sound_action import _SoundAction
from ..backend.windows._sound import _play_system_sound

class _PlaySystemSound(_SoundAction):
    def __init__(self, sound_type):
        self.sound_type = sound_type
        if self.sound_type.lower() not in ["info", "warning", "error", "question", "ok"]:
            raise ValueError(
                "Invalid sound type. Valid options: \"info\", \"warning\", \"error\", \"question\", \"ok\"."
            )
    
    def execute(self): _play_system_sound(self.sound_type)