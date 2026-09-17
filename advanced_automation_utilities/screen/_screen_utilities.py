import mss
from typing import Optional

def take_screenshot(region: Optional[tuple[int, int, int, int]] = None, monitor_index: int = 0):
    with mss.mss() as screen_capture:
        if region is None: screen = screen_capture.monitors[monitor_index]
        else:
            left, top, right, bottom = region
            screen = {
                "left": int(left),
                "top": int(top),
                "width": int(right - left),
                "height": int(bottom - top)
            }
        screenshot = screen_capture.grab(screen)
    return screenshot

def adjust_coordinates_for_region(
    x: int,
    y: int,
    region: Optional[tuple[int, int, int, int]],
    monitor_index: int = 0
) -> tuple[int, int]:
    if region is not None:
        x += region[0]
        y += region[1]
    elif monitor_index != 0:
        with mss.mss() as screen_capture:
            monitor = screen_capture.monitors[monitor_index]
            x += monitor["left"]
            y += monitor["top"]
    return int(x), int(y)