from .play_beep_sound import PlayBeepSound
from .play_audio import PlayAudio
from .play_system_sound import PlaySystemSound
from .speak import Speak
from contextlib import contextmanager
import threading

class Sound:
    def __init__(self):
        self._queue_mode = False
        self._queue = []

    @contextmanager
    def asynchronous(self):
        self._queue_mode = True
        self._queue.clear()
        try: yield self
        finally:
            self._queue_mode = False
            if self._queue:
                queue_copy = list(self._queue)
                self._queue.clear()
                def worker(actions):
                    for action in actions: action.execute()
                thread = threading.Thread(target = worker, args = (queue_copy,), daemon = True)
                thread.start()

    def _execute_or_queue(self, action):
        self._queue.append(action) if self._queue_mode else action.execute()
        return self

    def play_beep_sound(self, frequency: int, duration: int):
        return self._execute_or_queue(PlayBeepSound(frequency = frequency, duration = duration))

    def play_audio(self, file_path: str): return self._execute_or_queue(PlayAudio(file_path = file_path))

    def play_system_sound(self, sound_type: str = "info"):
        return self._execute_or_queue(PlaySystemSound(sound_type = sound_type))

    def speak(self, text: str): return self._execute_or_queue(Speak(text = text))