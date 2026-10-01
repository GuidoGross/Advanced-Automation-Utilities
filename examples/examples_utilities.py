import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from advanced_automation_utilities import Keyboard, KeyboardInfo, Timing, Sound
from tui_utilities import clear_console, header, print

def update_test_state(title, running):
    clear_console()
    header(title)
    print([
        ("The test is ", {}),
        ("stopped" if not running else "running", {"color": "#ff0000" if not running else "#00ff00"}),
        (". Press ", {}),
        ("F1", {"color": "#00bfff"}),
        (f" to {"run" if not running else "stop"} the test, or ", {}),
        ("F2", {"color": "#00bfff"}),
        (" to return to main menu", {})
    ], alignment = "center")

def start_stop_script(test_function, title):
    keyboard = Keyboard()
    keyboard_info = KeyboardInfo()
    sound = Sound()
    timing = Timing()
    running = False
    update_test_state(title, running)
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