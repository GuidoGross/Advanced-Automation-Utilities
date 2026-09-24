import ctypes

_LEFT_BUTTON_DOWN = 0x0002
_LEFT_BUTTON_UP = 0x0004
_RIGHT_BUTTON_DOWN = 0x0008
_RIGHT_BUTTON_UP = 0x0010
_MIDDLE_BUTTON_DOWN = 0x0020
_MIDDLE_BUTTON_UP = 0x0040
_WHEEL = 0x0800
_HORIZONTAL_WHEEL = 0x1000

class _Point(ctypes.Structure): _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def _mouse_down(button):
    match button:
        case "left": ctypes.windll.user32.mouse_event(_LEFT_BUTTON_DOWN, 0, 0, 0, 0)
        case "right": ctypes.windll.user32.mouse_event(_RIGHT_BUTTON_DOWN, 0, 0, 0, 0)
        case "middle": ctypes.windll.user32.mouse_event(_MIDDLE_BUTTON_DOWN, 0, 0, 0, 0)

def _mouse_up(button):
    match button:
        case "left": ctypes.windll.user32.mouse_event(_LEFT_BUTTON_UP, 0, 0, 0, 0)
        case "right": ctypes.windll.user32.mouse_event(_RIGHT_BUTTON_UP, 0, 0, 0, 0)
        case "middle": ctypes.windll.user32.mouse_event(_MIDDLE_BUTTON_UP, 0, 0, 0, 0)

def _get_cursor_position():
    point = _Point()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

def _set_cursor_position(x, y): ctypes.windll.user32.SetCursorPos(int(x), int(y))

def _scroll(amount, direction):
    match direction:
        case "up":
            sign = 1
            flag = _WHEEL
        case "down":
            sign = -1
            flag = _WHEEL
        case "right":
            sign = 1
            flag = _HORIZONTAL_WHEEL
        case "left":
            sign = -1
            flag = _HORIZONTAL_WHEEL
        case _: return
    ctypes.windll.user32.mouse_event(flag, 0, 0, int(amount) * sign, 0)