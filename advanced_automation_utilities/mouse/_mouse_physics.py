from dataclasses import dataclass

@dataclass
class MousePhysics:
    speed: float = 0
    minimum_speed: float = 0
    maximum_speed: float = 0
    speed_variation: float = 0
    duration: float = 0
    duration_variation: float = 0
    base_duration: float = 0
    base_duration_variation: float = 0
    inconsistency: float = 0
    target_radius: float = 0
    readjustment_duration_ratio: float = 0.25
    click_delay: float = 0.05
    click_delay_variation: float = 0
    click_duration: float = 0.05
    click_duration_variation: float = 0
    scroll_speed: float = 0
    scroll_speed_variation: float = 0
    scroll_duration: float = 0
    scroll_duration_variation: float = 0
    scroll_step: int = 1
    scroll_pause_variation: float = 0