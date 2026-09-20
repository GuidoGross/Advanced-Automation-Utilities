import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from examples.examples_utilities import start_stop_script
from advanced_automation_utilities.screen import Screen, ScreenInfo
from tui_utilities import (
    set_window_title,
    maximize_window,
    menu,
    confirm_exit,
    print,
    header,
    wait_for_key,
    success_message,
    error_message
)

def main():
    set_window_title("Prueba de Screen")
    maximize_window()
    while True:
        selection = menu(
            title = "Prueba de Screen",
            options = {
                "1": "Obtener resolución de pantalla",
                "2": "Obtener color del píxel",
                "3": "Localizar imagen en pantalla",
                "4": "Leer texto de la pantalla",
                "5": "Localizar texto en la pantalla",
                "S": "Salir"
            }
        )
        match selection:
            case "1": test_get_resolution()
            case "2": test_get_pixel_color()
            case "3": test_locate_image()
            case "4": test_read_text()
            case "5": test_locate_text()
            case "S": confirm_exit()

def test_get_resolution():
    header("Resolución de la pantalla")
    screen_info = ScreenInfo()
    print([
        ("Resolución: ", {"bold": True}),
        (f"{str(screen_info.resolution).replace(",", ";")}", {})
    ])
    print([("Ancho: ", {"bold": True}), (f"{screen_info.width}", {})])
    print([("Alto: ", {"bold": True}), (f"{screen_info.height}", {})])
    wait_for_key()

def test_get_pixel_color():
    def get_pixel_color():
        header("Color del píxel")
        screen_info = ScreenInfo()
        x = 300
        y = 600
        pixel_color = screen_info.pixel_color(x, y)
        hexadecimal_color = screen_info.pixel_color(x, y, format = "hexadecimal")
        print(f"Color del píxel en ({x}; {y}): ", bold = True)
        print([("    - RGB: ", {"bold": True}), (f"■ {pixel_color}", {"color": hexadecimal_color})])
        print([
            ("    - Hexadecimal: ", {"bold": True}),
            (f"■ {hexadecimal_color}", {"color": hexadecimal_color})
        ])
        wait_for_key()
    
    start_stop_script(get_pixel_color, "Obtener color del píxel")

def test_locate_image():
    def locate_image():
        header("Localizar imagen en pantalla")
        screen = Screen()
        x, y = screen.locate_image("", confidence = 0.9, monitor_index = 0)
        if x is not None and y is not None: success_message(f"Imagen encontrada en la posición ({x}; {y})")
        else: error_message("Imagen no encontrada")
    
    start_stop_script(locate_image, "Localizar imagen en pantalla")

def test_read_text():
    def read_text():
        header("Leer texto de la pantalla")
        screen = Screen()
        text = screen.read_text(monitor_index = 0)
        print([("Texto en la pantalla:", {"bold": True}), (f" {text}", {})])
        wait_for_key()
    
    start_stop_script(read_text, "Leer texto de la pantalla")

def test_locate_text():
    def locate_text():
        header("Localizar texto en pantalla")
        screen = Screen()
        text = "Prueba"
        x, y = screen.locate_text(text, exact_match = False, monitor_index = 0)
        if x is not None and y is not None:
            success_message(f"Texto \"{text}\" encontrado en la posición ({x}; {y})")
        else: error_message(f"Texto \"{text}\" no encontrado")
    
    start_stop_script(locate_text, "Localizar texto en pantalla")

if __name__ == "__main__": main()