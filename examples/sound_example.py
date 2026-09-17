import os
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory in sys.path: sys.path.remove(script_directory)
parent_directory = os.path.dirname(script_directory)
if parent_directory not in sys.path: sys.path.insert(0, parent_directory)

from automation_utilities.sound import Sound
from tui_utilities import set_window_title, maximize_window, menu, confirm_exit, header, print

def main():
    set_window_title("Prueba de Sound")
    maximize_window()
    while True:
        selection = menu(
            title = "Prueba de Sound",
            options = {
                "1": "Reproducir un pitido",
                "2": "Reproducir un archivo de audio",
                "3": "Reproducir un sonido del sistema",
                "4": "Sintetizar texto a voz",
                "S": "Salir"
            }
        )
        match selection:
            case "1": test_play_beep_sound()
            case "2": test_play_audio()
            case "3": test_system_sound()
            case "4": test_speak()
            case "S": confirm_exit()

def test_play_beep_sound():
    header("Reproducir un pitido")
    print("Reproduciendo el pitido...", alignment = "center")
    sound = Sound()
    sound.play_beep_sound(1000, 500)

def test_play_audio():
    header("Reproducir un archivo de audio")
    print("Reproduciendo el archivo de audio...", alignment = "center")
    sound = Sound()
    sound.play_audio("test.mp3")

def test_system_sound():
    header("Reproducir un sonido del sistema")
    print("Reproduciendo el sonido del sistema...", alignment = "center")
    sound = Sound()
    sound.play_system_sound("warning")

def test_speak():
    header("Sintetizar texto a voz")
    print("Reprodciendo el mensaje...", alignment = "center")
    sound = Sound()
    sound.speak("¡Hola, mundo!")

if __name__ == "__main__": main()