from ._sound_action import _SoundAction
from ..backend.windows._sound import _play_beep_sound

class _PlayBeepSound(_SoundAction):
    def __init__(self, frequency, duration):
        self.frequency = frequency
        self.duration = duration
        if self.duration <= 0: raise ValueError("Duration must be greater than 0.")
        if not (37 <= self.frequency <= 32767):
            raise ValueError("Frequency must be between 37Hz and 32.767Hz.")
    
    def execute(self): _play_beep_sound(self.frequency, self.duration)