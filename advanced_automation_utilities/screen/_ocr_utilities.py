from typing import Optional
from winrt.windows.media.ocr import OcrResult, OcrEngine
import numpy
from winrt.windows.graphics.imaging import SoftwareBitmap, BitmapPixelFormat, BitmapAlphaMode
from winrt.windows.storage.streams import DataWriter
import asyncio

def _run_ocr_on_region(
    region: Optional[tuple[int, int, int, int]] = None,
    monitor_index: int = 0
) -> OcrResult:
    from ._screen_utilities import take_screenshot
    screenshot = take_screenshot(region, monitor_index)
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
            "No se pudo inicializar el motor OCR de Windows. Compruebe la configuración de idioma."
        )
    
    async def recognize(): return await engine.recognize_async(software_bitmap)
    
    return asyncio.run(recognize())