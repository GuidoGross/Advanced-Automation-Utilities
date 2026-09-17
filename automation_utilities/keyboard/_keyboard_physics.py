from dataclasses import dataclass

@dataclass
class KeyboardPhysics:
    press_delay: float = 0.05
    press_delay_variation: float = 0
    press_duration: float = 0.05
    press_duration_variation: float = 0
    hotkey_delay: float = 0.01
    hotkey_delay_variation: float = 0
    typing_error_chance: float = 0
    typing_error_correction_delay: float = 0.1
    typing_error_correction_delay_variation: float = 0
    typing_error_delayed_realization_chance: float = 0
    auto_repeat: bool = True