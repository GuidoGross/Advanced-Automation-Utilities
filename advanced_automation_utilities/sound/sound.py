from ._sound_action import _SoundAction
from ._play_beep_sound import _PlayBeepSound
from ._play_audio import _PlayAudio
from ._play_system_sound import _PlaySystemSound
from ._speak import _Speak
from contextlib import contextmanager
import threading
from typing import Annotated

class Sound:
    """
    Main controller for audio operations.
    Allows playing beeps, audio files, system sounds, and text-to-speech.
    """
    def __init__(self) -> None:
        """
        Initializes the Sound controller.
        """
        self._queue_mode = False
        self._queue = []
    
    @contextmanager
    def asynchronous(self) -> None:
        """
        Context manager to queue actions and execute them asynchronously.

        Example:
        ```python
        with sound.asynchronous():
            sound.play_beep_sound(1000, 500)
            sound.speak("Hello World")
        ```
        """
        self._queue_mode = True
        self._queue.clear()
        try: yield self
        finally:
            self._queue_mode = False
            if self._queue:
                queue_copy = list(self._queue)
                self._queue.clear()

                def worker(actions: list) -> None:
                    for action in actions: action.execute()
                
                thread = threading.Thread(target = worker, args = (queue_copy,), daemon = True)
                thread.start()
    
    def _execute_or_queue(self, action: _SoundAction) -> None:
        self._queue.append(action) if self._queue_mode else action.execute()
        return self
    
    def play_beep_sound(
        self, 
        frequency: Annotated[int, "Must be between 37 and 32767"], 
        duration: Annotated[int, "Milliseconds. Must be > 0"]
    ) -> None:
        """
        Plays a motherboard beep with a specific frequency and duration.

        Example:
        ```python
        Sound().play_beep_sound(frequency = 1000, duration = 0.5)
        ```
        """
        return self._execute_or_queue(_PlayBeepSound(frequency = frequency, duration = duration))
    
    def play_audio(self, file_path: str) -> None:
        """
        Plays an audio file from the file system.

        Example:
        ```python
        Sound().play_audio("alert.wav")
        ```
        """
        return self._execute_or_queue(_PlayAudio(file_path = file_path))
    
    def play_system_sound(
        self, 
        sound_type: Annotated[str, "Valid options: \"info\", \"warning\", \"error\", \"question\", \"ok\""]
    ) -> None:
        """
        Plays a default Windows system sound.
        
        Example:
        ```python
        Sound().play_system_sound("warning")
        ```
        """
        return self._execute_or_queue(_PlaySystemSound(sound_type = sound_type))
    
    def speak(self, text: str) -> None:
        """
        Synthesizes text to speech using the default Windows voice.
        
        Example:
        ```python
        Sound().speak("Hello, world!")
        ```
        """
        return self._execute_or_queue(_Speak(text = text))