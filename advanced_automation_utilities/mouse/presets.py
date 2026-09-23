from .mouse_physics import MousePhysics

MOUSE_NORMAL = MousePhysics(
    speed = 1250,
    speed_variation = 0.1,
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
    scroll_step = 120,
    scroll_pause_variation = 0.1
)

MOUSE_SLOW = MousePhysics(
    speed = 625,
    speed_variation = 0.1,
    base_duration = 0.1,
    base_duration_variation = 0.1,
    inconsistency = 0.1,
    target_radius = 5,
    readjustment_duration_ratio = 0.25,
    click_delay = 0.05,
    click_delay_variation = 0.1,
    click_duration = 0.05,
    click_duration_variation = 0.1,
    scroll_speed = 500,
    scroll_speed_variation = 0.1,
    scroll_step = 120,
    scroll_pause_variation = 0.1
)

MOUSE_FAST = MousePhysics(
    speed = 2500,
    speed_variation = 0.1,
    base_duration = 0.1,
    base_duration_variation = 0.1,
    inconsistency = 0.25,
    target_radius = 50,
    readjustment_duration_ratio = 0.25,
    click_delay = 0.025,
    click_delay_variation = 0.1,
    click_duration = 0.025,
    click_duration_variation = 0.1,
    scroll_speed = 2000,
    scroll_speed_variation = 0.1,
    scroll_step = 120,
    scroll_pause_variation = 0.1
)