from .keyboard_physics import KeyboardPhysics

KEYBOARD_NORMAL = KeyboardPhysics(
    press_delay = 0.15,
    press_delay_variation = 0.5,
    press_duration = 0.05,
    press_duration_variation = 0.1,
    hotkey_delay = 0.15,
    hotkey_delay_variation = 0.5,
    typing_error_chance = 0.025,
    typing_error_correction_delay = 0.25,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.5
)

KEYBOARD_SLOW = KeyboardPhysics(
    press_delay = 0.3,
    press_delay_variation = 0.5,
    press_duration = 0.1,
    press_duration_variation = 0.1,
    hotkey_delay = 0.3,
    hotkey_delay_variation = 0.5,
    typing_error_chance = 0.125,
    typing_error_correction_delay = 0.5,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.25
)

KEYBOARD_FAST = KeyboardPhysics(
    press_delay = 0.075,
    press_delay_variation = 0.5,
    press_duration = 0.025,
    press_duration_variation = 0.1,
    hotkey_delay = 0.075,
    hotkey_delay_variation = 0.5,
    typing_error_chance = 0.05,
    typing_error_correction_delay = 0.125,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.75
)