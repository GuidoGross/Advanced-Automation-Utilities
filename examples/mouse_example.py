import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from examples.examples_utilities import start_stop_script
from advanced_automation_utilities.mouse import MousePhysics, Mouse, MouseInfo
from tui_utilities import (
    set_window_title, maximize_window, menu, confirm_exit, print, header, wait_for_key
)

def main():
    set_window_title("Prueba de Mouse")
    maximize_window()
    while True:
        selection = menu(
            title = "Prueba de Mouse",
            options = {
                "1": "Mover el puntero",
                "2": "Hacer clic",
                "3": "Hacer doble clic",
                "4": "Hacer clic derecho",
                "5": "Hacer clic medio",
                "6": "Mantener y soltar clic",
                "7": "Arrastrar",
                "8": "Desplazar",
                "9": "Desplazar hasta que se cumpla una condición",
                "10": "Obtener coordenadas del puntero",
                "11": "Obtener color del pixel en el que se encuentra el puntero",
                "12": "Detectar si el puntero está en la pantalla",
                "S": "Salir"
            }
        )
        match selection:
            case "1": test_move_pointer()
            case "2": test_click()
            case "3": test_double_click()
            case "4": test_right_click()
            case "5": test_middle_click()
            case "6": test_hold_and_release_click()
            case "7": test_drag()
            case "8": test_scroll()
            case "9": test_scroll_until()
            case "10": test_get_pointer_coordinates()
            case "11": test_get_pixel_color()
            case "12": test_is_pointer_on_screen()
            case "S": confirm_exit()

def test_move_pointer():
    def move():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25
        )
        mouse = Mouse(physics)
        mouse.move(300, 600)
    
    start_stop_script(move, "Mover el puntero")

def test_click():
    def click():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25,
            click_delay = 0.05,
            click_delay_variation = 0.1,
            click_duration = 0.05,
            click_duration_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.click(300, 600)
    
    start_stop_script(click, "Hacer clic")

def test_double_click():
    def double_click():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25,
            click_delay = 0.05,
            click_delay_variation = 0.1,
            click_duration = 0.05,
            click_duration_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.double_click(300, 600)
    
    start_stop_script(double_click, "Hacer doble clic")

def test_right_click():
    def right_click():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25,
            click_delay = 0.05,
            click_delay_variation = 0.1,
            click_duration = 0.05,
            click_duration_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.right_click(300, 600)
    
    start_stop_script(right_click, "Hacer clic derecho")

def test_middle_click():
    def middle_click():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25,
            click_delay = 0.05,
            click_delay_variation = 0.1,
            click_duration = 0.05,
            click_duration_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.middle_click(300, 600)
    
    start_stop_script(middle_click, "Hacer clic medio")

def test_hold_and_release_click():
    def hold_and_release_click():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25,
            click_delay = 0.05,
            click_delay_variation = 0.1,
            click_duration = 1,
            click_duration_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.hold_click(300, 600).release_click(300, 600)
    
    start_stop_script(hold_and_release_click, "Mantener y soltar clic")

def test_drag():
    def drag():
        physics = MousePhysics(
            speed = 1500,
            speed_variation = 0.1,
            base_duration = 0.1,
            base_duration_variation = 0.1,
            inconsistency = 0.25,
            target_radius = 25,
            readjustment_duration_ratio = 0.25,
            click_delay = 0.05,
            click_delay_variation = 0.1,
            click_duration = 0.05,
            click_duration_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.drag_and_drop(300, 600, 600, 600)
    
    start_stop_script(drag, "Arrastrar")

def test_scroll():
    def scroll():
        physics = MousePhysics(
            scroll_speed = 1000,
            scroll_speed_variation = 0.1,
            scroll_duration = 0,
            scroll_duration_variation = 0,
            scroll_step = 120,
            scroll_pause_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.scroll(1000).scroll(1000, "up").scroll(1000, "right").scroll(1000, "left")
    
    start_stop_script(scroll, "Desplazarse")

def test_scroll_until():
    def scroll_until():
        physics = MousePhysics(
            scroll_speed = 1000,
            scroll_speed_variation = 0.1,
            scroll_duration = 0,
            scroll_duration_variation = 0,
            scroll_step = 120,
            scroll_pause_variation = 0.1
        )
        mouse = Mouse(physics)
        mouse.scroll_until(condition_function = lambda: False, timeout = 2.5)
        mouse.scroll_until(condition_function = lambda: False, direction = "up", timeout = 2.5)
        mouse.scroll_until(condition_function = lambda: False, direction = "right", timeout = 2.5)
        mouse.scroll_until(condition_function = lambda: False, direction = "left", timeout = 2.5)
    
    start_stop_script(scroll_until, "Desplazarse hasta que se cumpla una condición")


def test_get_pointer_coordinates():
    def get_pointer_coordinates():
        header("Coordenadas del puntero")
        mouse_info = MouseInfo()
        coordinates = mouse_info.coordinates
        x = mouse_info.x
        y = mouse_info.y
        print([("Coordenadas del puntero: ", {"bold": True}), (str(coordinates).replace(",", ";"), {})])
        print([("Coordenada x: ", {"bold": True}), (f"{x}", {})])
        print([("Coordenada y: ", {"bold": True}), (f"{y}", {})])
        wait_for_key()
    
    start_stop_script(get_pointer_coordinates, "Obtener coordenadas del puntero")

def test_get_pixel_color():
    def get_pixel_color():
        header("Color del pixel bajo el puntero")
        mouse_info = MouseInfo()
        pixel_color = mouse_info.pixel_color()
        hexadecimal_pixel_color = mouse_info.pixel_color(format = "hexadecimal")
        print("Color del pixel bajo el puntero:", bold = True)
        print([("    - RGB:", {"bold": True}), (f" ■ {pixel_color}", {"color": hexadecimal_pixel_color})])
        print([
            ("    - Hexadecimal: ", {"bold": True}),
            (f" ■ {hexadecimal_pixel_color}", {"color": hexadecimal_pixel_color})
        ])
        wait_for_key()
    
    start_stop_script(get_pixel_color, "Obtener color del pixel bajo el puntero")

def test_is_pointer_on_screen():
    def is_pointer_on_screen():
        header("¿Está el puntero dentro de la pantalla?")
        mouse_info = MouseInfo()
        print([
            ("El puntero ", {}),
            (
                f"{"está" if mouse_info.on_screen else "no está"}",
                {"color": f"{"#00ff00" if mouse_info.on_screen else "#ff0000"}"}
            ),
            (" dentro de la pantalla", {})
        ], alignment = "center")
        wait_for_key()
    
    start_stop_script(is_pointer_on_screen, "Detectar si el puntero está dentro de la pantalla")

if __name__ == "__main__": main()