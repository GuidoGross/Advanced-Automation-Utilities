**[Home](Home)** ➔ **[Physics](Physics)**

<div align = "center">

# **Physics**

**To evade bot-detection mechanisms and simulate real user interactions, both `Mouse` and `Keyboard` modules are governed by highly configurable, immutable dataclasses (`MousePhysics` and `KeyboardPhysics`) that force pointer movements to follow randomized Bézier curves with dynamic speeds and overshoots, while making keyboard typing simulate human delays, keystroke variations, and even random typos with delayed corrections.**

</div>

---

> [!TIP]
> Physics parameters are highly granular. You can pass a custom physics object to their respective facades to alter their simulation parameters dynamically.

```python
mouse_physics = MousePhysics(
    speed = 1500,
    minimum_speed = 0,
    maximum_speed = 0,
    speed_variation = 0.1,
    duration = 0,
    duration_variation = 0,
    base_duration = 0.1,
    base_duration_variation = 0.1,
    inconsistency = 0.25,
    target_radius = 25,
    readjustment_duration_ratio = 0.25,
    click_delay = 0.05,
    click_delay_variation = 0.1,
    click_duration = 0.05,
    click_duration_variation = 0.1,
    scroll_speed = 1000,
    scroll_speed_variation = 0.1,
    scroll_duration = 0,
    scroll_duration_variation = 0,
    scroll_step = 120,
    scroll_pause_variation = 0.1
)
mouse = Mouse(mouse_physics)
keyboard_physics = KeyboardPhysics(
    press_delay = 0.15,
    press_delay_variation = 0.5,
    press_duration = 0.05,
    press_duration_variation = 0.1,
    hotkey_delay = 0.01,
    hotkey_delay_variation = 0.5,
    typing_error_chance = 0.025,
    typing_error_correction_delay = 0.25,
    typing_error_correction_delay_variation = 0.5,
    typing_error_delayed_realization_chance = 0.5,
    auto_repeat = True
)
keyboard = Keyboard(keyboard_physics)
```