from ._native_keyboard import is_pressed

class KeyboardInfo:
    def is_pressed(self, key: str) -> bool: return is_pressed(key)