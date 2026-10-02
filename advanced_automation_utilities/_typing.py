from typing import Literal

MouseButton = Literal[
    "left", "right", "middle",
    "Left", "Right", "Middle",
    "LEFT", "RIGHT", "MIDDLE"
]
ScrollDirection = Literal[
    "up", "down", "left", "right",
    "Up", "Down", "Left", "Right",
    "UP", "DOWN", "LEFT", "RIGHT"
]
ColorFormat = Literal[
    "rgb", "hexadecimal",
    "Rgb", "Hexadecimal",
    "RGB", "HEXADECIMAL"
]
SystemSound = Literal[
    "info", "warning", "error", "question", "ok",
    "Info", "Warning", "Error", "Question", "Ok",
    "INFO", "WARNING", "ERROR", "QUESTION", "OK"
]