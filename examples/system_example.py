import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from examples.examples_utilities import start_stop_script
from automation_utilities.system import System, SystemInfo
from automation_utilities.timing import Timing
from tui_utilities import (
    set_window_title,
    maximize_window,
    menu,
    confirm_exit,
    header,
    print,
    wait_for_key,
    success_message,
    error_message
)

def main():
    set_window_title("Prueba de System")
    maximize_window()
    while True:
        selection = menu(
            title = "Prueba de System",
            options = {
                "1": "Obtener texto del portapapeles y modificarlo",
                "2": "Obtener el título de la ventana activa",
                "3": "Abrir y matar un proceso",
                "4": "Redimensionar y mover ventana",
                "5": "Bloquear la pantalla",
                "6": "Cerrar sesión",
                "7": "Suspender el dispositivo",
                "8": "Hibernar el dispositivo",
                "9": "Apagar el dispositivo",
                "10": "Reiniciar el dispositivo",
                "11": "Probar Kill Switch",
                "S": "Salir"
            }
        )
        match selection:
            case "1": test_get_clipboard_text_and_modify_it()
            case "2": test_get_active_window_title()
            case "3": test_open_and_kill_process()
            case "4": test_resize_and_move_window()
            case "5": test_screen_lock()
            case "6": test_sign_out()
            case "7": test_sleep()
            case "8": test_hibernate()
            case "9": test_shutdown()
            case "10": test_restart()
            case "11": test_kill_switch()
            case "S": confirm_exit()

def test_get_clipboard_text_and_modify_it():
    header("Texto actual en el portapapeles")
    system = System()
    system_info = SystemInfo()
    print([
        ("Texto actual en el portapapeles:", {"bold": True}),
        (f" {system_info.clipboard_text}", {"color": "#00bfff"})
    ])
    wait_for_key()
    header("Texto sobreescrito en el portapapeles")
    system.set_clipboard_text("¡Hola mundo!")
    print([
        ("Se ha sobrescrito el portapapeles con:", {"bold": True}),
        (f" {system_info.clipboard_text}", {"color": "#00bfff"})
    ])
    wait_for_key()

def test_get_active_window_title():
    def get_active_window_title():
        header("Título de la ventana activa")
        system_info = SystemInfo()
        title = system_info.active_window_title
        print([
            ("La ventana actualmente enfocada es: ", {"bold": True}),
            (f"{title}", {"color": "#00bfff"})
        ])
        wait_for_key()
    
    start_stop_script(get_active_window_title, "Obtener el título de la ventana activa")

def test_open_and_kill_process():
    header("Abrir un proceso")
    system = System()
    process_name = "notepad.exe"
    print([
        ("Abriendo ", {}),
        (f"{process_name}", {"color": "#00bfff"})
    ], alignment = "center")
    try:
        system.open_process(process_name)
        success_message(f"{process_name.capitalize()} abierta con éxito.")
    except Exception as error: error_message(f"Error al abrir {process_name}: {error}")
    header("Matar un proceso")
    print([
        ("Cerrando ", {}),
        (f"{process_name}", {"color": "#00bfff"})
    ], alignment = "center")
    try:
        system.kill_process(process_name, force = True)
        success_message(f"{process_name.capitalize()} cerrado con éxito.")
    except Exception as error: error_message(f"Error al cerrar {process_name}: {error}")

def test_resize_and_move_window():
    header("Mover y redimensionar ventana")
    system = System()
    system_info = SystemInfo()
    timing = Timing()
    process_name = "notepad.exe"
    try:
        system.open_process(process_name)
        timing.wait(1)
        window_title = system_info.active_window_title
        system.resize_window(window_title, 500, 500)
        system.move_window(window_title, 100, 100)
        success_message(f"Se ha movido y redimensionado {process_name}")
        system.kill_process(process_name)
    except Exception as error: error_message(f"Error: {error}")

def test_screen_lock():
    header("Bloquear pantalla")
    print("Bloqueando la pantalla...", alignment = "center")
    system = System()
    system.lock_screen()

def test_sign_out():
    header("Cerrar sesión")
    print("Cerrando la sesión...", alignment = "center")
    system = System()
    system.sign_out()

def test_sleep():
    header("Suspender el dispositivo")
    print("Suspendiendo el dispositivo...", alignment = "center")
    system = System()
    system.sleep()

def test_hibernate():
    header("Hibernar el dispositivo")
    print("Hibernando el dispositivo...", alignment = "center")
    system = System()
    system.hibernate()

def test_shutdown():
    header("Apagar el dispositivo")
    print("Apagando el dispositivo...", alignment = "center")
    system = System()
    system.shutdown(delay = 15)

def test_restart():
    header("Reiniciar el dispositivo")
    print("Reiniciando el dispositivo...", alignment = "center")
    system = System()
    system.restart(delay = 15)

def test_kill_switch():
    header("Probar Kill Switch")
    system = System()
    timing = Timing()
    system.enable_kill_switch()
    print([
        ("El Kill Switch está activado. Presione ", {}),
        ("Ctrl + Shift + Alt + K", {"color": "#00bfff"}),
        (" para abortar, o espere 10 segundos para que la prueba termine normalmente...", {})
    ], alignment = "center")
    try:
        timing.wait(10)
        system.disable_kill_switch()
        success_message("Prueba finalizada sin usar el Kill Switch")
    except KeyboardInterrupt:
        error_message("Prueba abortada")
    finally: system.disable_kill_switch()

if __name__ == "__main__": main()