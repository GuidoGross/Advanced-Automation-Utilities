from ._keyboard_physics import KeyboardPhysics

KEYBOARD_HUMAN = KeyboardPhysics(
    press_delay = 0.1,
    press_delay_variation = 0.1,
    press_duration = 0.05,
    press_duration_variation = 0.1,
    hotkey_delay = 0.05,
    hotkey_delay_variation = 0.1
)

KEYBOARD_SLOW = KeyboardPhysics(
    press_delay = 0.25,
    press_delay_variation = 0.1,
    press_duration = 0.1,
    press_duration_variation = 0.1,
    hotkey_delay = 0.25,
    hotkey_delay_variation = 0.1
)

KEYBOARD_FAST = KeyboardPhysics(
    press_delay = 0.05,
    press_delay_variation = 0.1,
    press_duration = 0.025,
    press_duration_variation = 0.1,
    hotkey_delay = 0.025,
    hotkey_delay_variation = 0.1
)