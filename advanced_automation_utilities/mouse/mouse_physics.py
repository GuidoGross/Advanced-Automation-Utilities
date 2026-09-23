from dataclasses import dataclass

@dataclass
class MousePhysics:
    """
    **Description:**

    Configuration class that defines the timing and movement characteristics
    for mouse actions, allowing for human-like or instantaneous execution.

    **Arguments:**

    - **`speed`** (`float`): Must be >= 0.
    - **`minimum_speed`** (`float`): Must be >= 0.
    - **`maximum_speed`** (`float`): Must be >= 0.
    - **`speed_variation`** (`float`): Must be >= 0.
    - **`duration`** (`float`): Seconds. Must be >= 0.
    - **`duration_variation`** (`float`): Must be >= 0.
    - **`base_duration`** (`float`): Seconds. Must be >= 0.
    - **`base_duration_variation`** (`float`): Must be >= 0.
    - **`inconsistency`** (`float`): Must be >= 0.
    - **`target_radius`** (`float`): Must be >= 0.
    - **`readjustment_duration_ratio`** (`float`): Must be >= 0 and <= 1.
    - **`click_delay`** (`float`): Seconds. Must be >= 0.
    - **`click_delay_variation`** (`float`): Must be >= 0.
    - **`click_duration`** (`float`): Seconds. Must be >= 0.
    - **`click_duration_variation`** (`float`): Must be >= 0.
    - **`scroll_speed`** (`float`): Must be >= 0.
    - **`scroll_speed_variation`** (`float`): Must be >= 0.
    - **`scroll_duration`** (`float`): Seconds. Must be >= 0.
    - **`scroll_duration_variation`** (`float`): Must be >= 0.
    - **`scroll_step`** (`int`): Must be >= 1.
    - **`scroll_pause_variation`** (`float`): Must be >= 0.
    """
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

    def __post_init__(self) -> None:
        if self.speed < 0: raise ValueError("Speed cannot be negative.")
        if self.minimum_speed < 0: raise ValueError("Minimum speed cannot be negative.")
        if self.maximum_speed < 0: raise ValueError("Maximum speed cannot be negative.")
        if self.speed_variation < 0: raise ValueError("Speed variation cannot be negative.")
        if self.duration < 0: raise ValueError("Duration cannot be negative.")
        if self.duration_variation < 0: raise ValueError("Duration variation cannot be negative.")
        if self.base_duration < 0: raise ValueError("Base duration cannot be negative.")
        if self.base_duration_variation < 0:
            raise ValueError("Base duration variation cannot be negative.")
        if self.inconsistency < 0: raise ValueError("Inconsistency cannot be negative.")
        if self.target_radius < 0: raise ValueError("Target radius cannot be negative.")
        if not (0 <= self.readjustment_duration_ratio <= 1):
            raise ValueError("Readjustment duration ratio must be between 0 and 1.")
        if self.click_delay < 0: raise ValueError("Click delay cannot be negative.")
        if self.click_delay_variation < 0: raise ValueError("Click delay variation cannot be negative.")
        if self.click_duration < 0: raise ValueError("Click duration cannot be negative.")
        if self.click_duration_variation < 0:
            raise ValueError("Click duration variation cannot be negative.")
        if self.scroll_speed < 0: raise ValueError("Scroll speed cannot be negative.")
        if self.scroll_speed_variation < 0: raise ValueError("Scroll speed variation cannot be negative.")
        if self.scroll_duration < 0: raise ValueError("Scroll duration cannot be negative.")
        if self.scroll_duration_variation < 0:
            raise ValueError("Scroll duration variation cannot be negative.")
        if self.scroll_step < 1: raise ValueError("Scroll step must be greater than or equal to 1.")
        if self.scroll_pause_variation < 0: raise ValueError("Scroll pause variation cannot be negative.")