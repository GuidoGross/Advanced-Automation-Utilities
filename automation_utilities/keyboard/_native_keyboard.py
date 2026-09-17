from ..timing import Timing
import ctypes
from ctypes import wintypes
import threading
import _thread

_user32 = ctypes.windll.user32

_VIRTUAL_KEY_CODES = {
    "backspace": 0x08, "tab": 0x09, "clear": 0x0C, "enter": 0x0D, "shift": 0x10, "ctrl": 0x11,
    "alt": 0x12, "pause": 0x13, "caps_lock": 0x14, "esc": 0x1B, "space": 0x20, "page_up": 0x21,
    "page_down": 0x22, "end": 0x23, "home": 0x24, "left_arrow": 0x25, "up_arrow": 0x26,
    "right_arrow": 0x27, "down_arrow": 0x28, "select": 0x29, "print": 0x2A, "execute": 0x2B,
    "print_screen": 0x2C, "insert": 0x2D, "delete": 0x2E, "help": 0x2F, "0": 0x30, "1": 0x31, "2": 0x32,
    "3": 0x33, "4": 0x34, "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39, "a": 0x41, "b": 0x42,
    "c": 0x43, "d": 0x44, "e": 0x45, "f": 0x46, "g": 0x47, "h": 0x48, "i": 0x49, "j": 0x4A, "k": 0x4B,
    "l": 0x4C, "m": 0x4D, "n": 0x4E, "o": 0x4F, "p": 0x50, "q": 0x51, "r": 0x52, "s": 0x53, "t": 0x54,
    "u": 0x55, "v": 0x56, "w": 0x57, "x": 0x58, "y": 0x59, "z": 0x5A, "numpad_0": 0x60, "numpad_1": 0x61,
    "numpad_2": 0x62, "numpad_3": 0x63, "numpad_4": 0x64, "numpad_5": 0x65, "numpad_6": 0x66,
    "numpad_7": 0x67, "numpad_8": 0x68, "numpad_9": 0x69, "multiply_key": 0x6A, "add_key": 0x6B,
    "separator_key": 0x6C, "subtract_key": 0x6D, "decimal_key": 0x6E, "divide_key": 0x6F, "f1": 0x70,
    "f2": 0x71, "f3": 0x72, "f4": 0x73, "f5": 0x74, "f6": 0x75, "f7": 0x76, "f8": 0x77, "f9": 0x78,
    "f10": 0x79, "f11": 0x7A, "f12": 0x7B, "num_lock": 0x90, "scroll_lock": 0x91, "left_shift": 0xA0,
    "right_shift": 0xA1, "left_control": 0xA2, "right_control": 0xA3, "left_alt": 0xA4, "alt_gr": 0xA5,
    "left_windows": 0x5B, "right_windows": 0x5C
}

class _KeyboardInput(ctypes.Structure):
    _fields_ = (
        ("virtual_key_code", wintypes.WORD),
        ("scan_code", wintypes.WORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("extra_information", ctypes.POINTER(ctypes.c_ulong))
    )

class _MouseInput(ctypes.Structure):
    _fields_ = (
        ("delta_x", wintypes.LONG),
        ("delta_y", wintypes.LONG),
        ("mouse_data", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("extra_information", ctypes.POINTER(ctypes.c_ulong))
    )

class _HardwareInput(ctypes.Structure):
    _fields_ = (
        ("message", wintypes.DWORD),
        ("word_parameter_low", wintypes.WORD),
        ("word_parameter_high", wintypes.WORD)
    )

class _Input(ctypes.Structure):
    class _InputUnion(ctypes.Union):
        _fields_ = (
            ("keyboard_input", _KeyboardInput),
            ("mouse_input", _MouseInput),
            ("hardware_input", _HardwareInput)
        )
    _anonymous_ = ("_input_union",)
    _fields_ = (("type", wintypes.DWORD), ("_input_union", _InputUnion))

class _KeyboardHookStruct(ctypes.Structure):
    _fields_ = [
        ("virtual_key_code", wintypes.DWORD),
        ("scan_code", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("extra_information", ctypes.POINTER(ctypes.c_ulong))
    ]

def _get_virtual_key_code(key: str) -> int:
    key = key.lower()
    if key in _VIRTUAL_KEY_CODES: return _VIRTUAL_KEY_CODES[key]
    if len(key) == 1:
        virtual_key = _user32.VkKeyScanW(ord(key))
        return virtual_key & 0xFF
    return 0

def send_key(key: str, key_released: bool = False):
    virtual_key = _get_virtual_key_code(key)
    if not virtual_key: return
    input_struct = _Input(
        type = 1,
        keyboard_input = _KeyboardInput(
            virtual_key_code = virtual_key, flags = 0x0002 if key_released else 0
        )
    )
    _user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(input_struct))

def send_unicode(text: str):
    for character in text:
        surrogate = character.encode("utf-16-le")
        for i in range(0, len(surrogate), 2):
            code = int.from_bytes(surrogate[i: i + 2], "little")
            input_down = _Input(
                type = 1,
                keyboard_input = _KeyboardInput(
                    virtual_key_code = 0, scan_code = code, flags = 0x0004, time = 0
                )
            )
            _user32.SendInput(1, ctypes.byref(input_down), ctypes.sizeof(input_down))
            input_up = _Input(
                type = 1,
                keyboard_input = _KeyboardInput(
                    virtual_key_code = 0, scan_code = code, flags = 0x0004 | 0x0002, time = 0
                )
            )
            _user32.SendInput(1, ctypes.byref(input_up), ctypes.sizeof(input_up))

def is_pressed(key: str) -> bool:
    virtual_key = _get_virtual_key_code(key)
    if not virtual_key: return False
    if _key_states.get(virtual_key, False): return True
    return (_user32.GetAsyncKeyState(virtual_key) & 0x8000) != 0

_HookProcedure = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

_user32.SetWindowsHookExW.argtypes = [ctypes.c_int, _HookProcedure, wintypes.HINSTANCE, wintypes.DWORD]
_user32.SetWindowsHookExW.restype = wintypes.HHOOK
_user32.CallNextHookEx.argtypes = [wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM]
_user32.CallNextHookEx.restype = wintypes.LPARAM

_blocked_keys = set()
_key_states = {}
_hook_id = None
_hook_function = None
_hook_thread = None
_kill_switch_enabled = False
_kill_switch_key = 0
_kill_switch_modifiers = []

_WINDOWS_HOOK_KEYBOARD_LOW_LEVEL = 13
_WINDOW_MESSAGE_KEY_DOWN = 0x0100
_WINDOW_MESSAGE_KEY_UP = 0x0101
_WINDOW_MESSAGE_SYSTEM_KEY_DOWN = 0x0104
_WINDOW_MESSAGE_SYSTEM_KEY_UP = 0x0105

def _hook_worker():
    global _hook_id, _hook_function
    def _low_level_keyboard_handler(hook_code, window_message, hook_data):
        if hook_code >= 0:
            virtual_key = ctypes.cast(
                hook_data, ctypes.POINTER(_KeyboardHookStruct)
            ).contents.virtual_key_code
            if window_message in (_WINDOW_MESSAGE_KEY_DOWN, _WINDOW_MESSAGE_SYSTEM_KEY_DOWN):
                _key_states[virtual_key] = True
                if _kill_switch_enabled and virtual_key == _kill_switch_key:
                    all_modifiers_pressed = True
                    for modifier in _kill_switch_modifiers:
                        if not _key_states.get(modifier, False) and not (_user32.GetAsyncKeyState(modifier) & 0x8000):
                            all_modifiers_pressed = False
                            break
                    if all_modifiers_pressed:
                        _thread.interrupt_main()
                        return 1
            elif window_message in (_WINDOW_MESSAGE_KEY_UP, _WINDOW_MESSAGE_SYSTEM_KEY_UP):
                _key_states[virtual_key] = False
            if virtual_key in _blocked_keys: return 1
        return _user32.CallNextHookEx(_hook_id, hook_code, window_message, hook_data)
    _hook_function = _HookProcedure(_low_level_keyboard_handler)
    _hook_id = _user32.SetWindowsHookExW(_WINDOWS_HOOK_KEYBOARD_LOW_LEVEL, _hook_function, None, 0)
    message = wintypes.MSG()
    while _user32.GetMessageW(ctypes.byref(message), None, 0, 0) > 0:
        _user32.TranslateMessage(ctypes.byref(message))
        _user32.DispatchMessageW(ctypes.byref(message))

def _ensure_hook():
    global _hook_thread
    if _hook_thread is None or not _hook_thread.is_alive():
        _hook_thread = threading.Thread(target = _hook_worker, daemon = True)
        _hook_thread.start()
        timing = Timing()
        timing.wait(0.1)

def block_key(key: str):
    virtual_key = _get_virtual_key_code(key)
    if virtual_key:
        _blocked_keys.add(virtual_key)
        _ensure_hook()

def unblock_key(key: str):
    virtual_key = _get_virtual_key_code(key)
    if virtual_key and virtual_key in _blocked_keys: _blocked_keys.remove(virtual_key)

def enable_kill_switch(keys: list[str]):
    global _kill_switch_enabled, _kill_switch_key, _kill_switch_modifiers
    if not keys: return
    main_key = _get_virtual_key_code(keys[-1])
    modifiers = [_get_virtual_key_code(modifier) for modifier in keys[:-1]]
    if not main_key: return
    _kill_switch_key = main_key
    _kill_switch_modifiers = [modifier for modifier in modifiers if modifier]
    _kill_switch_enabled = True
    _ensure_hook()

def disable_kill_switch():
    global _kill_switch_enabled
    _kill_switch_enabled = False