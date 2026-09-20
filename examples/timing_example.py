import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from examples.examples_utilities import start_stop_script
from advanced_automation_utilities.timing import Timing, TimingInfo, measure_time
from advanced_automation_utilities.keyboard import KeyboardInfo
from tui_utilities import (
    set_window_title,
    maximize_window,
    menu,
    confirm_exit,
    print,
    header,
    wait_for_key,
    decimal_format,
    success_message,
    error_message
)

def main():
    set_window_title("Prueba de Timing")
    maximize_window()
    while True:
        selection = menu(
            title = "Prueba de Timing",
            options = {
                "1": "Esperar",
                "2": "Esperar aleatoriamente",
                "3": "Esperar por condición",
                "4": "Obtener el tiempo de ejecución de una función",
                "S": "Salir"
            }
        )
        match selection:
            case "1": test_wait()
            case "2": test_wait_random()
            case "3": test_wait_until()
            case "4": test_measure_time()
            case "S": confirm_exit()

def test_wait():
    header("Espera")
    waiting_time = 3
    print([
        ("Esperando ", {}),
        (f"{waiting_time}", {"color": "#00bfff"}),
        (" segundos...\n", {})
    ], alignment = "center")
    timing = Timing()
    timing.wait(waiting_time)
    print("\nEspera terminada", alignment = "center")
    wait_for_key()

def test_wait_random():
    header("Espera aleatoria")
    lower_waiting_time = 1
    upper_waiting_time = 5
    print([
        ("Esperando aleatoriamente entre ", {}),
        (f"{lower_waiting_time}", {"color": "#00bfff"}),
        (" y ", {}),
        (f"{upper_waiting_time}", {"color": "#00bfff"}),
        (" segundos...\n", {})
    ], alignment = "center")
    timing = Timing()
    timing_info = TimingInfo()
    start_time = timing_info.time
    timing.wait_random(lower_waiting_time, upper_waiting_time)
    end_time = timing_info.time
    print([
        ("\nEspera terminada en ", {}),
        (f"{decimal_format((end_time - start_time) * 1000, decimals = 0)}ms", {"color": "#00bfff"})
    ], alignment = "center")
    wait_for_key()

def test_wait_until():
    def _test():
        header("Espera por condición")
        print([
            ("Esperando hasta un máximo de 5 segundos a que pulse la tecla ", {}),
            ("Space", {"color": "#00bfff"}),
            ("...\n", {})
        ], alignment = "center")
        keyboard_info = KeyboardInfo()
        timing = Timing()
        
        def condition(): return keyboard_info.is_pressed("space")
        
        success = timing.wait_until(condition, timeout = 5)
        if success:
            wait_for_key(text = "")
            success_message("Ha pulsado la tecla \"Space\" a tiempo")
        else: error_message("No ha pulsado la tecla \"Space\" a tiempo")
        while keyboard_info.is_pressed("space"): timing.wait(0.01)
    start_stop_script(_test, "Esperar por condición")

def test_measure_time():
    header("Medir tiempo de ejecución de una función")
    timing = Timing()
    
    @measure_time
    def simulated_task():
        print("Iniciando una tarea simulada...\n", alignment = "center")
        timing.wait_random(1, 3)
    
    simulated_task()
    wait_for_key()

if __name__ == "__main__": main()