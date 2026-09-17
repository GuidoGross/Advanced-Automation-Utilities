from .press_key import PressKey
from ._keyboard_action import KeyboardAction
from ._keyboard_physics import KeyboardPhysics
from ._native_keyboard import send_unicode
from ..timing import Timing
from typing import Optional
import random
import string
import copy

class Write(KeyboardAction):
    def __init__(self, text: str, physics: Optional[KeyboardPhysics] = None):
        super().__init__(physics = physics)
        self.text = text

    def execute(self):
        timing = Timing()
        correction_physics = copy.copy(self.physics)
        correction_physics.press_delay = self.physics.typing_error_correction_delay
        correction_physics.press_delay_variation = self.physics.typing_error_correction_delay_variation
        fast_navigation_physics = copy.copy(self.physics)
        fast_navigation_physics.press_delay = self.physics.press_delay / 3
        i = 0
        while i < len(self.text):
            character = self.text[i]
            if self.physics.typing_error_chance > 0 and random.random() < self.physics.typing_error_chance:
                possible_characters = string.ascii_letters.replace(character, "")
                incorrect_character = random.choice(possible_characters)
                send_unicode(incorrect_character)
                extra_characters_typed = 0
                while i + 1 + extra_characters_typed < len(self.text):
                    if random.random() < self.physics.typing_error_delayed_realization_chance:
                        press_delay = self.physics.press_delay
                        if self.physics.press_delay_variation > 0:
                            press_delay += random.uniform(-press_delay * self.physics.press_delay_variation, press_delay * self.physics.press_delay_variation)
                        timing.wait(max(0, press_delay))
                        send_unicode(self.text[i + 1 + extra_characters_typed])
                        extra_characters_typed += 1
                    else: break
                if extra_characters_typed < 5:
                    for j in range(extra_characters_typed + 1):
                        physics = correction_physics if j == 0 else fast_navigation_physics
                        PressKey("backspace", physics = physics).execute()
                    send_unicode(character)
                    for j in range(extra_characters_typed):
                        press_delay = self.physics.press_delay
                        if self.physics.press_delay_variation > 0:
                            press_delay += random.uniform(-press_delay * self.physics.press_delay_variation, press_delay * self.physics.press_delay_variation)
                        timing.wait(max(0, press_delay))
                        send_unicode(self.text[i + 1 + j])
                else:
                    press_delay = correction_physics.press_delay
                    if correction_physics.press_delay_variation > 0:
                        press_delay += random.uniform(-press_delay * correction_physics.press_delay_variation, press_delay * correction_physics.press_delay_variation)
                    timing.wait(max(0, press_delay))
                    for _ in range(extra_characters_typed):
                        PressKey("left_arrow", physics = fast_navigation_physics).execute()
                    PressKey("backspace", physics = fast_navigation_physics).execute()
                    send_unicode(character)
                    for _ in range(extra_characters_typed):
                        PressKey("right_arrow", physics = fast_navigation_physics).execute()
                after_correction_delay = self.physics.typing_error_correction_delay
                if self.physics.typing_error_correction_delay_variation > 0:
                    after_correction_delay += random.uniform(-after_correction_delay * self.physics.typing_error_correction_delay_variation, after_correction_delay * self.physics.typing_error_correction_delay_variation)
                timing.wait(max(0, after_correction_delay))
                i += extra_characters_typed + 1
                continue
            send_unicode(character)
            if i < len(self.text) - 1:
                press_delay = self.physics.press_delay
                if self.physics.press_delay_variation > 0:
                    press_delay += random.uniform(-press_delay * self.physics.press_delay_variation, press_delay * self.physics.press_delay_variation)
                timing.wait(max(0, press_delay))
            i += 1