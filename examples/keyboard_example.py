import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from examples.examples_utilities import start_stop_script
from advanced_automation_utilities.keyboard import Keyboard, KeyboardInfo, KeyboardPhysics
from tui_utilities import (
    set_window_title, maximize_window, menu, confirm_exit, print, header, wait_for_key
)

def main():
    set_window_title("Prueba de Keyboard")
    maximize_window()
    while True:
        selection = menu(
            title = "Prueba de Keyboard",
            options = {
                "1": "Pulsar una tecla",
                "2": "Mantener y soltar una tecla",
                "3": "Ejecutar atajo",
                "4": "Escribir texto",
                "5": "Detectar si una tecla está presionada",
                "S": "Salir"
            }
        )
        match selection:
            case "1": test_press_key()
            case "2": test_hold_and_release_key()
            case "3": test_hotkey()
            case "4": test_write()
            case "5": test_is_key_pressed()
            case "S": confirm_exit()

def test_press_key():
    def press_key():
        physics = KeyboardPhysics(
            press_delay = 0.15,
            press_delay_variation = 0.5,
            press_duration = 0.05,
            press_duration_variation = 0.1
        )
        keyboard = Keyboard(physics)
        keyboard.press_key("a")
    
    start_stop_script(press_key, "Pulsar una tecla")

def test_hold_and_release_key():
    def hold_key():
        physics = KeyboardPhysics(
            press_delay = 0.15,
            press_delay_variation = 0.5,
            press_duration = 1,
            press_duration_variation = 0.1
        )
        keyboard = Keyboard(physics)
        keyboard.hold_key("a")
        keyboard.release_key("a")
    
    start_stop_script(hold_key, "Mantener y soltar una tecla")

def test_hotkey():
    def hotkey():
        physics = KeyboardPhysics(
            press_delay = 0.15,
            press_delay_variation = 0.5,
            press_duration = 0.05,
            press_duration_variation = 0.1,
            hotkey_delay = 0.15,
            hotkey_delay_variation = 0.5
        )
        keyboard = Keyboard(physics)
        keyboard.hotkey("ctrl", "c")
    
    start_stop_script(hotkey, "Ejecutar atajo")

def test_write():
    def write():
        physics = KeyboardPhysics(
            press_delay = 0.15,
            press_delay_variation = 0.5,
            press_duration = 0.05,
            press_duration_variation = 0.1,
            typing_error_chance = 0.025,
            typing_error_correction_delay = 0.25,
            typing_error_correction_delay_variation = 0.5,
            typing_error_delayed_realization_chance = 0.5
        )
        keyboard = Keyboard(physics)
        keyboard.write("Al escribir este texto, se generarán errores simulados muy avanzados.")
    
    start_stop_script(write, "Escribir texto")

def test_is_key_pressed():
    def is_key_pressed():
        header("¿Está presionada la tecla \"espacio\"?")
        keyboard_info = KeyboardInfo()
        is_pressed = keyboard_info.is_pressed("space")
        print([
            ("La tecla \"espacio\" ", {}),
            (
                f"{"está" if is_pressed else "no está"}",
                {"color": f"{"#00ff00" if is_pressed else "#ff0000"}"}
            ),
            (" presionada", {})
        ], alignment = "center")
        wait_for_key()
    
    start_stop_script(is_key_pressed, "Detectar si una tecla está presionada")

if __name__ == "__main__": main()