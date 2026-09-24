import asyncio
import mss
import ctypes
import ctypes.wintypes
import numpy
import cv2
from winrt.windows.graphics.imaging import SoftwareBitmap, BitmapPixelFormat, BitmapAlphaMode
from winrt.windows.storage.streams import DataWriter
from winrt.windows.media.ocr import OcrEngine

_SPI_GETWORKAREA = 48

_ocr_loop = asyncio.new_event_loop()

def _get_screen_resolution():
    with mss.mss() as screen_capture_tool:
        monitor = screen_capture_tool.monitors[1]
        return monitor["width"], monitor["height"]

def _get_pixel_color(x, y):
    with mss.mss() as screen_capture_tool:
        virtual = screen_capture_tool.monitors[0]
        if not (virtual["left"] <= x < virtual["left"] + virtual["width"] and
                virtual["top"] <= y < virtual["top"] + virtual["height"]):
            raise ValueError(f"Coordinates ({x}, {y}) are out of screen bounds.")
    device_context = ctypes.windll.user32.GetDC(0)
    color = ctypes.windll.gdi32.GetPixel(device_context, x, y)
    ctypes.windll.user32.ReleaseDC(0, device_context)
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    return (r, g, b)

def _get_work_area():
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.SystemParametersInfoW(_SPI_GETWORKAREA, 0, ctypes.byref(rect), 0)
    return rect.left, rect.top, rect.right, rect.bottom

def _take_screenshot(region = None, monitor_index = 0):
    with mss.mss() as screen_capture_tool:
        if region is None: screen = screen_capture_tool.monitors[monitor_index]
        else:
            left, top, right, bottom = region
            screen = {
                "left": int(left),
                "top": int(top),
                "width": int(right - left),
                "height": int(bottom - top)
            }
        screenshot = screen_capture_tool.grab(screen)
    return screenshot

def _adjust_coordinates_for_region(x, y, region, monitor_index = 0):
    if region is not None:
        x += region[0]
        y += region[1]
    elif monitor_index != 0:
        with mss.mss() as screen_capture_tool:
            monitor = screen_capture_tool.monitors[monitor_index]
            x += monitor["left"]
            y += monitor["top"]
    return int(x), int(y)

def _locate_image(image_path, confidence, region, monitor_index):
    with open(image_path, "rb") as file:
        image_array = numpy.frombuffer(file.read(), numpy.uint8)
    template = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    if template is None:
        raise ValueError(
            f"Failed to read image at \"{image_path}\". Ensure it is a valid image file."
        )
    screenshot = _take_screenshot(region, monitor_index)
    image = numpy.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, max_value, _, max_location = cv2.minMaxLoc(result)
    if max_value >= confidence:
        height, width = template.shape[:2]
        x = max_location[0] + width / 2
        y = max_location[1] + height / 2
        return _adjust_coordinates_for_region(x, y, region, monitor_index)
    return None, None

def _run_ocr_on_region(region = None, monitor_index = 0):
    screenshot = _take_screenshot(region, monitor_index)
    width = screenshot.width
    height = screenshot.height
    image = numpy.array(screenshot, dtype = numpy.uint8)
    software_bitmap = SoftwareBitmap(
        BitmapPixelFormat.BGRA8, width, height, BitmapAlphaMode.PREMULTIPLIED
    )
    data_writer = DataWriter()
    data_writer.write_bytes(image.tobytes())
    buffer = data_writer.detach_buffer()
    software_bitmap.copy_from_buffer(buffer)
    engine = OcrEngine.try_create_from_user_profile_languages()
    if engine is None:
        raise SystemError(
            "Windows OCR engine could not be initialized. Please check your language settings."
        )
    
    async def recognize(): return await engine.recognize_async(software_bitmap)
    
    return _ocr_loop.run_until_complete(recognize())