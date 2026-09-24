import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from advanced_automation_utilities.keyboard import Keyboard, KeyboardInfo
from advanced_automation_utilities.sound import Sound
from advanced_automation_utilities.timing import Timing
from tui_utilities import clear_console, header, print

def update_test_state(title, running):
    clear_console()
    header(title)
    print([
        ("La prueba está ", {}),
        (
            "detenida" if not running else "ejecutándose",
            {"color": "#ff0000" if not running else "#00ff00"}
        ),
        (". Pulse ", {}),
        ("F1", {"color": "#00bfff"}),
        (f" para {"ejecutar" if not running else "detener"} la prueba, o ", {}),
        ("F2", {"color": "#00bfff"}),
        (" para volver al menú principal", {})
    ], alignment = "center")

def start_stop_script(test_function, title):
    running = False
    update_test_state(title, running)
    keyboard = Keyboard()
    keyboard_info = KeyboardInfo()
    sound = Sound()
    timing = Timing()
    keyboard.block_key("f1")
    keyboard.block_key("f2")
    while True:
        if keyboard_info.is_pressed("f2"):
            with sound.asynchronous() as sound_task: sound.play_beep_sound(500, 0.25)
            break
        if keyboard_info.is_pressed("f1"):
            running = not running
            update_test_state(title, running)
            with sound.asynchronous() as sound_task: sound.play_beep_sound(1000, 0.25)
            while keyboard_info.is_pressed("f1"): timing.wait(0.01)
            if running:
                test_function()
                running = False
                update_test_state(title, running)
                with sound.asynchronous() as sound_task: sound.play_beep_sound(500, 0.25)
        timing.wait(0.05)
    keyboard.unblock_key("f1")
    keyboard.unblock_key("f2")