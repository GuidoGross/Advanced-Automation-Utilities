from dataclasses import dataclass
from typing import Annotated

@dataclass
class KeyboardPhysics:
    """
    Configuration class that defines the timing characteristics
    for keyboard actions, allowing for human-like typing speeds or instantaneous execution.
    """
    press_delay: Annotated[float, "Seconds. Must be >= 0"] = 0.05
    press_delay_variation: Annotated[float, "Must be >= 0"] = 0
    press_duration: Annotated[float, "Seconds. Must be >= 0"] = 0.05
    press_duration_variation: Annotated[float, "Must be >= 0"] = 0
    hotkey_delay: Annotated[float, "Seconds. Must be >= 0"] = 0.01
    hotkey_delay_variation: Annotated[float, "Must be >= 0"] = 0
    typing_error_chance: Annotated[float, "Must be >= 0 and <= 1"] = 0
    typing_error_correction_delay: Annotated[float, "Seconds. Must be >= 0"] = 0.1
    typing_error_correction_delay_variation: Annotated[float, "Must be >= 0"] = 0
    typing_error_delayed_realization_chance: Annotated[float, "Must be >= 0 and <= 1"] = 0
    auto_repeat: bool = True

    def __post_init__(self) -> None:
        if self.press_delay < 0: raise ValueError("Press delay cannot be negative.")
        if self.press_delay_variation < 0: raise ValueError("Press delay variation cannot be negative.")
        if self.press_duration < 0: raise ValueError("Press duration cannot be negative.")
        if self.press_duration_variation < 0:
            raise ValueError("Press duration variation cannot be negative.")
        if self.hotkey_delay < 0: raise ValueError("Hotkey delay cannot be negative.")
        if self.hotkey_delay_variation < 0: raise ValueError("Hotkey delay variation cannot be negative.")
        if not (0 <= self.typing_error_chance <= 1):
            raise ValueError("Typing error chance must be between 0 and 1.")
        if self.typing_error_correction_delay < 0:
            raise ValueError("Typing error correction delay cannot be negative.")
        if self.typing_error_correction_delay_variation < 0:
            raise ValueError("Typing error correction delay variation cannot be negative.")
        if not (0 <= self.typing_error_delayed_realization_chance <= 1):
            raise ValueError("Typing error delayed realization chance must be between 0 and 1.")