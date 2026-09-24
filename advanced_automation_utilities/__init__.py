import os

if os.name != "nt":
    raise NotImplementedError("Advanced Automation Utilities is currently only supported on Windows.")

import ctypes

try: ctypes.windll.user32.SetProcessDPIAware()
except Exception: pass

from .mouse import (
    Mouse,
    MouseInfo,
    MousePhysics,
    MOUSE_NORMAL,
    MOUSE_SLOW,
    MOUSE_FAST
)
from .keyboard import (
    Keyboard,
    KeyboardInfo,
    KeyboardPhysics,
    KEYBOARD_NORMAL,
    KEYBOARD_SLOW,
    KEYBOARD_FAST
)
from .screen import (Screen, ScreenInfo)
from .timing import (Timing, TimingInfo, measure_time)
from .sound import Sound
from .system import (System, SystemInfo)
from .exceptions import WindowNotFoundError

__all__ = [
    "Mouse",
    "MouseInfo",
    "MousePhysics",
    "MOUSE_NORMAL",
    "MOUSE_SLOW",
    "MOUSE_FAST",
    "Keyboard",
    "KeyboardInfo",
    "KeyboardPhysics",
    "KEYBOARD_NORMAL",
    "KEYBOARD_SLOW",
    "KEYBOARD_FAST",
    "Screen",
    "ScreenInfo",
    "Timing",
    "TimingInfo",
    "measure_time",
    "Sound",
    "System",
    "SystemInfo",
    "WindowNotFoundError",
]