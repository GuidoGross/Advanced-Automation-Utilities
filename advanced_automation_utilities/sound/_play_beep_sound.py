from ._sound_action import _SoundAction
import winsound

class _PlayBeepSound(_SoundAction):
    def __init__(self, frequency: int, duration: int) -> None:
        self.frequency = frequency
        self.duration = duration
        if self.duration < 0: raise ValueError("Duration cannot be negative.")
        if not (37 <= self.frequency <= 32767):
            raise ValueError("Frequency must be between 37Hz and 32.767Hz.")
    
    def execute(self) -> None: winsound.Beep(self.frequency, self.duration)