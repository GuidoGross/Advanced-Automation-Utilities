from ._sound_action import SoundAction
import winsound

class PlayBeepSound(SoundAction):
    def __init__(self, frequency: int, duration: int):
        self.frequency = frequency
        self.duration = duration

    def execute(self): winsound.Beep(self.frequency, self.duration)