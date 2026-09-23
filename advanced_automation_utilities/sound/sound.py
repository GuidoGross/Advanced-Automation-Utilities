from ._play_beep_sound import _PlayBeepSound
from ._play_audio import _PlayAudio
from ._play_system_sound import _PlaySystemSound
from ._speak import _Speak
from .._queueable_controller import _QueueableController

class Sound(_QueueableController):
    """
    **Description:**

    Main controller for audio operations.
    Allows playing beeps, audio files, system sounds, and text-to-speech.
    """
    def __init__(self) -> None:
        """
        **Description:**

        Initializes the Sound controller.

        **Returns:**

        **`None`**
        """
        super().__init__()
    
    def play_beep_sound(self, frequency: int, duration: int) -> None:
        """
        **Description:**

        Plays a motherboard beep with a specific frequency and duration.

        **Arguments:**

        - **`frequency`** (`int`): Must be between 37 and 32767.
        - **`duration`** (`int`): Milliseconds. Must be > 0.

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Sound().play_beep_sound(frequency = 1000, duration = 0.5)
        ```
        """
        return self._execute_or_queue(_PlayBeepSound(frequency = frequency, duration = duration))
    
    def play_audio(self, file_path: str) -> None:
        """
        **Description:**

        Plays an audio file from the file system.

        **Arguments:**

        - **`file_path`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Sound().play_audio("alert.wav")
        ```
        """
        return self._execute_or_queue(_PlayAudio(file_path = file_path))
    
    def play_system_sound(self, sound_type: str) -> None:
        """
        **Description:**

        Plays a default Windows system sound.

        **Arguments:**

        - **`sound_type`** (`str`): Valid options: "info", "warning", "error", "question", "ok".

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Sound().play_system_sound("warning")
        ```
        """
        return self._execute_or_queue(_PlaySystemSound(sound_type = sound_type))
    
    def speak(self, text: str) -> None:
        """
        **Description:**

        Synthesizes text to speech using the default Windows voice.

        **Arguments:**

        - **`text`** (`str`)

        **Returns:**

        **`None`**

        **Example:**

        ```python
        Sound().speak("Hello, world!")
        ```
        """
        return self._execute_or_queue(_Speak(text = text))