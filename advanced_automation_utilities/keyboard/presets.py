from .keyboard_physics import KeyboardPhysics

KEYBOARD_HUMAN = KeyboardPhysics(
    press_delay = 0.1,
    press_delay_variation = 0.1,
    press_duration = 0.05,
    press_duration_variation = 0.1,
    hotkey_delay = 0.05,
    hotkey_delay_variation = 0.1,
    typing_error_chance = 0.025,
    typing_error_correction_delay = 0.25,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.5
)

KEYBOARD_SLOW_AND_PRECISE = KeyboardPhysics(
    press_delay = 0.25,
    press_delay_variation = 0.1,
    press_duration = 0.1,
    press_duration_variation = 0.1,
    hotkey_delay = 0.25,
    hotkey_delay_variation = 0.1,
    typing_error_chance = 0.1,
    typing_error_correction_delay = 0.5,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.1
)

KEYBOARD_FAST_AND_IMPRECISE = KeyboardPhysics(
    press_delay = 0.05,
    press_delay_variation = 0.1,
    press_duration = 0.025,
    press_duration_variation = 0.1,
    hotkey_delay = 0.025,
    hotkey_delay_variation = 0.1,
    typing_error_chance = 0.05,
    typing_error_correction_delay = 0.1,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.75
)