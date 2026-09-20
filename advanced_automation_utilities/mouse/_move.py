from ._mouse_action import _MouseAction
from .mouse_info import MouseInfo
from .mouse_physics import MousePhysics
from typing import Optional
import math
import random
import ctypes
import time

class _Move(_MouseAction):
    def __init__(self, x: int, y: int, physics: Optional[MousePhysics] = None) -> None:
        super().__init__(physics = physics)
        self.x = x
        self.y = y
    
    def execute(self) -> None:
        original_target_x = self.x
        original_target_y = self.y
        info = MouseInfo()
        initial_x, initial_y = info.coordinates
        if math.hypot(original_target_x - initial_x, original_target_y - initial_y) <= self.physics.target_radius:
            return
        distance = math.hypot(self.x - initial_x, self.y - initial_y)
        speed = self.physics.speed
        duration = self.physics.duration
        if duration <= 0 and speed > 0:
            if self.physics.speed_variation > 0:
                speed += random.uniform(-speed * self.physics.speed_variation, speed * self.physics.speed_variation)
                speed = max(1e-15, speed)
            base_duration = self.physics.base_duration
            if self.physics.base_duration_variation > 0:
                base_duration += random.uniform(-base_duration * self.physics.base_duration_variation, base_duration * self.physics.base_duration_variation)
                base_duration = max(0, base_duration)
            duration = base_duration + (distance / speed)
        elif duration > 0 and self.physics.duration_variation > 0:
            duration += random.uniform(-duration * self.physics.duration_variation, duration * self.physics.duration_variation)
            duration = max(1e-15, duration)
        if self.physics.target_radius > 0:
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(0, self.physics.target_radius)
            self.x += math.cos(angle) * radius
            self.y += math.sin(angle) * radius
        if duration <= 0:
            ctypes.windll.user32.SetCursorPos(int(self.x), int(self.y))
            return
        if self.physics.inconsistency <= 0:
            _execute_movement_phase(
                initial_x = initial_x,
                initial_y = initial_y,
                final_x = self.x,
                final_y = self.y,
                duration = duration,
                inconsistency = 0,
                speed = speed,
                minimum_speed = self.physics.minimum_speed,
                maximum_speed = self.physics.maximum_speed
            )
            return
        speed = distance / duration
        initial_movement_duration = duration * (1 - self.physics.readjustment_duration_ratio)
        readjust_duration = duration * self.physics.readjustment_duration_ratio
        speed_factor = max(1, speed / 500)
        maximum_overshoot = speed * 0.05 * self.physics.inconsistency * speed_factor
        movement_angle = math.atan2(self.y - initial_y, self.x - initial_x)
        if random.random() < 0.5: overshoot_angle = random.gauss(movement_angle, math.pi / 4)
        else: overshoot_angle = random.gauss(movement_angle + math.pi, math.pi / 4)
        speed_factor = 500 / max(1, speed)
        overshoot_radius = (random.random() ** speed_factor) * maximum_overshoot
        error_x = math.cos(overshoot_angle) * overshoot_radius
        error_y = math.sin(overshoot_angle) * overshoot_radius
        phase_1_x = self.x + error_x
        phase_1_y = self.y + error_y
        _execute_movement_phase(
            initial_x = initial_x,
            initial_y = initial_y,
            final_x = phase_1_x,
            final_y = phase_1_y,
            duration = initial_movement_duration,
            inconsistency = self.physics.inconsistency,
            speed = speed,
            minimum_speed = self.physics.minimum_speed,
            maximum_speed = self.physics.maximum_speed
        )
        if readjust_duration <= 0: return
        if speed >= 2000: number_of_phases = 3
        elif speed >= 1000: number_of_phases = 2
        else: number_of_phases = 1
        pauses = []
        for _ in range(number_of_phases - 1): pauses.append(random.uniform(0.1, 0.025))
        total_pause_time = sum(pauses)
        available_time = readjust_duration - total_pause_time
        if available_time < 0.025:
            number_of_phases = 1
            pauses = []
            available_time = readjust_duration
        if number_of_phases == 1: phase_times = [available_time]
        elif number_of_phases == 2:
            split_proportion = random.uniform(0.4, 0.6)
            phase_times = [available_time * split_proportion, available_time * (1 - split_proportion)]
        else:
            proportion_1 = random.uniform(0.2, 0.4)
            proportion_2 = random.uniform(0.2, 0.4)
            proportion_3 = 1 - proportion_1 - proportion_2
            phase_times = [
                available_time * proportion_1,
                available_time * proportion_2,
                available_time * proportion_3
            ]
        error_fractions = []
        match number_of_phases:
            case 1: error_fractions = [1]
            case 2:
                fraction_1 = 2 / 3 + random.uniform(-0.1, 0.1)
                error_fractions = [min(1, fraction_1), 1]
            case 3:
                fraction_1 = 0.5 + random.uniform(-0.1, 0.1)
                fraction_2 = 0.75 + random.uniform(-0.1, 0.1)
                error_fractions = [min(1, fraction_1), min(1, fraction_2), 1]
        for i in range(number_of_phases):
            fraction = error_fractions[i]
            phase_time = phase_times[i]
            remaining_error_x = error_x * (1 - fraction)
            remaining_error_y = error_y * (1 - fraction)
            target_x = self.x + remaining_error_x
            target_y = self.y + remaining_error_y
            current_x, current_y = info.coordinates
            _execute_movement_phase(
                current_x,
                current_y,
                target_x,
                target_y,
                phase_time,
                self.physics.inconsistency,
                speed * 0.5,
                self.physics.minimum_speed,
                self.physics.maximum_speed
            )
            if self.physics.target_radius > 0:
                final_current_x, final_current_y = info.coordinates
                if math.hypot(final_current_x - original_target_x, final_current_y - original_target_y) <= self.physics.target_radius:
                    break
            if i < number_of_phases - 1:
                target_time = time.perf_counter() + pauses[i]
                while time.perf_counter() < target_time: pass

def _execute_movement_phase(
    initial_x: int,
    initial_y: int,
    final_x: int,
    final_y: int,
    duration: float,
    inconsistency: float,
    speed: float,
    minimum_speed: float = 0,
    maximum_speed: float = 0
) -> None:
    if duration <= 0: return
    distance = duration * speed
    steps = int(max(duration * 120, distance / 5, 60))
    path = _generate_human_path(initial_x, initial_y, final_x, final_y, steps, inconsistency, speed)
    speed_factor = max(1, speed / 500)
    tremor_chance = 0.25 * inconsistency / speed_factor
    start_time = time.perf_counter()
    expected_time = start_time
    previous_x, previous_y = initial_x, initial_y
    distortion_factor = random.uniform(-0.1, 0.1)
    for i in range(steps):
        progress = (i + 1) / steps
        ease = _distorted_ease(progress, distortion_factor)
        index = int(ease * (steps - 1))
        current_x, current_y = path[index]
        if random.random() < tremor_chance and i < steps - 1:
            tremor_x, tremor_y = _calculate_tremor(current_x, current_y, final_x, final_y, inconsistency, speed)
            current_x += tremor_x
            current_y += tremor_y
        ctypes.windll.user32.SetCursorPos(int(current_x), int(current_y))
        step_distance = math.hypot(current_x - previous_x, current_y - previous_y)
        step_duration = duration / steps
        instant_speed = step_distance / step_duration
        if minimum_speed > 0 and instant_speed < minimum_speed:
            step_duration = step_distance / minimum_speed
        if maximum_speed > 0 and instant_speed > maximum_speed:
            step_duration = step_distance / maximum_speed
        expected_time += step_duration
        while time.perf_counter() < expected_time: pass
        previous_x, previous_y = current_x, current_y

def _generate_human_path(
    initial_x: int,
    initial_y: int,
    target_x: int,
    target_y: int,
    steps: int,
    inconsistency: float,
    speed: float
) -> list[tuple[float, float]]:
    distance = math.hypot(target_x - initial_x, target_y - initial_y)
    if distance == 0: return [(target_x, target_y)] * steps
    speed_factor = max(1, speed / 500)
    adjusted_inconsistency = inconsistency / speed_factor
    segments = 4
    segment_lengths = []
    remaining = 1
    for i in range(segments - 1):
        length = 1 / segments
        variation = length * 0.5
        segment_length = min(length + random.uniform(-variation, variation), remaining - 0.05)
        segment_lengths.append(segment_length)
        remaining -= segment_length
    segment_lengths.append(remaining)
    points = []
    current_x, current_y = initial_x, initial_y
    remaining_steps = steps
    for i, length_percentage in enumerate(segment_lengths):
        segment_target_x = initial_x + (target_x - initial_x) * sum(segment_lengths[:i + 1])
        segment_target_y = initial_y + (target_y - initial_y) * sum(segment_lengths[:i + 1])
        segment_distance = distance * length_percentage
        segment_steps = int(steps * length_percentage)
        if i == segments - 1: segment_steps = remaining_steps
        remaining_steps -= segment_steps
        direction_x = (segment_target_x - current_x) / max(segment_distance, 1e-15)
        direction_y = (segment_target_y - current_y) / max(segment_distance, 1e-15)
        perpendicular_x, perpendicular_y = -direction_y, direction_x
        maximum_curve = segment_distance * adjusted_inconsistency
        control_point_1_x = current_x + (segment_target_x - current_x) * 1 / 3 + perpendicular_x * random.uniform(-maximum_curve, maximum_curve)
        control_point_1_y = current_y + (segment_target_y - current_y) * 1 / 3 + perpendicular_y * random.uniform(-maximum_curve, maximum_curve)
        control_point_2_x = current_x + (segment_target_x - current_x) * 2 / 3 + perpendicular_x * random.uniform(-maximum_curve, maximum_curve)
        control_point_2_y = current_y + (segment_target_y - current_y) * 2 / 3 + perpendicular_y * random.uniform(-maximum_curve, maximum_curve)
        for j in range(1, segment_steps + 1):
            progress = j / segment_steps
            points.append(
                _bezier_point(
                    (current_x, current_y),
                    (control_point_1_x, control_point_1_y),
                    (control_point_2_x, control_point_2_y),
                    (segment_target_x, segment_target_y),
                    progress
                )
            )
        current_x, current_y = segment_target_x, segment_target_y
    return points

def _bezier_point(
    point_0: tuple[float, float],
    point_1: tuple[float, float],
    point_2: tuple[float, float],
    point_3: tuple[float, float],
    progress: float
) -> tuple[float, float]:
    x = (1 - progress) ** 3 * point_0[0] + 3 * (1 - progress) ** 2 * progress * point_1[0] + 3 * (1 - progress) * progress ** 2 * point_2[0] + progress ** 3 * point_3[0]
    y = (1 - progress) ** 3 * point_0[1] + 3 * (1 - progress) ** 2 * progress * point_1[1] + 3 * (1 - progress) * progress ** 2 * point_2[1] + progress ** 3 * point_3[1]
    return x, y

def _distorted_ease(progress: float, distortion_factor: float) -> float:
    base_ease = _ease(progress)
    distortion = distortion_factor * (progress ** 2) * ((1 - progress) ** 2) * 16
    ease = max(0, min(1, base_ease + distortion))
    return ease

def _calculate_tremor(
    current_x: float,
    current_y: float,
    target_x: int,
    target_y: int,
    inconsistency: float,
    speed: float
) -> tuple[float, float]:
    speed_factor = max(1, speed / 500)
    magnitude = random.uniform(1, 5) * inconsistency / speed_factor
    if magnitude == 0: return 0, 0
    angle = random.gauss(0, 30)
    while abs(angle) >= 90 or angle == 0: angle = random.gauss(0, 30)
    angle_radians = math.radians(angle)
    difference_x = target_x - current_x
    difference_y = target_y - current_y
    distance = math.hypot(difference_x, difference_y)
    if distance == 0: return 0, 0
    direction_angle = math.atan2(difference_y, difference_x)
    final_angle = direction_angle + angle_radians
    tremor_x = math.cos(final_angle) * magnitude
    tremor_y = math.sin(final_angle) * magnitude
    return tremor_x, tremor_y

def _ease(n: float) -> float:
    if n < 0.5: return 2 * n * n
    else:
        n = 2 * n - 1
        return -0.5 * (n * (n - 2) - 1)