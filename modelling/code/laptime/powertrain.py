"""CBR rear-wheel power ceiling derived from its measured Dyno curve.

This module deliberately returns only the acceleration *ceiling imposed by
available rear-wheel power*.  A tyre GGv, wheelie boundary and aerodynamic
losses are separate constraints and must reduce this ceiling before a lap-time
claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


PS_TO_WATT = 735.49875


@dataclass(frozen=True)
class PowerCurve:
    rpm: np.ndarray
    rear_wheel_power_ps: np.ndarray

    def __post_init__(self) -> None:
        if self.rpm.ndim != 1 or self.rear_wheel_power_ps.ndim != 1:
            raise ValueError("power curve values must be one-dimensional")
        if len(self.rpm) < 2 or len(self.rpm) != len(self.rear_wheel_power_ps):
            raise ValueError("power curve needs matching arrays with at least two points")
        if np.any(np.diff(self.rpm) <= 0.0) or np.any(self.rear_wheel_power_ps < 0.0):
            raise ValueError("rpm must increase and power must be non-negative")


@dataclass(frozen=True)
class Gearbox:
    ratios: np.ndarray
    primary_reduction: float
    final_reduction: float
    loaded_rear_radius_m: float
    usable_rpm_interval: tuple[float, float]

    def engine_rpm(self, speed_mps: float, gear_index: int) -> float:
        wheel_rps = speed_mps / (2.0 * np.pi * self.loaded_rear_radius_m)
        return wheel_rps * 60.0 * self.ratios[gear_index] * self.primary_reduction * self.final_reduction


@dataclass(frozen=True)
class PowerCeiling:
    speed_mps: np.ndarray
    selected_gear: np.ndarray
    engine_rpm: np.ndarray
    rear_wheel_power_w: np.ndarray
    acceleration_ceiling_mps2: np.ndarray


def power_limited_acceleration(
    speed_mps: np.ndarray,
    curve: PowerCurve,
    gearbox: Gearbox,
    total_mass_kg: float,
    power_scale: float = 1.0,
) -> PowerCeiling:
    """Select the best legal gear and calculate P/(m*v) at each speed.

    Results are intentionally an upper bound: no drag, wheelie, tyre or
    shift-time penalty has been deducted.  Those belong in the later GGv merge.
    """
    if total_mass_kg <= 0.0 or power_scale <= 0.0:
        raise ValueError("mass and power_scale must be positive")
    if speed_mps.ndim != 1 or np.any(speed_mps <= 0.0):
        raise ValueError("speeds must be a positive one-dimensional array")
    low_rpm, high_rpm = gearbox.usable_rpm_interval
    if not 0.0 < low_rpm < high_rpm:
        raise ValueError("usable rpm interval must be increasing and positive")

    selected_gear = np.full(len(speed_mps), -1, dtype=int)
    selected_rpm = np.full(len(speed_mps), np.nan)
    selected_power = np.zeros(len(speed_mps))
    for row, speed in enumerate(speed_mps):
        candidates: list[tuple[float, int, float]] = []
        for gear in range(len(gearbox.ratios)):
            rpm = gearbox.engine_rpm(float(speed), gear)
            if low_rpm <= rpm <= high_rpm:
                power = float(np.interp(rpm, curve.rpm, curve.rear_wheel_power_ps)) * PS_TO_WATT * power_scale
                candidates.append((power, gear, rpm))
        if candidates:
            power, gear, rpm = max(candidates)
            selected_gear[row] = gear + 1
            selected_rpm[row] = rpm
            selected_power[row] = power
    return PowerCeiling(
        speed_mps=speed_mps,
        selected_gear=selected_gear,
        engine_rpm=selected_rpm,
        rear_wheel_power_w=selected_power,
        acceleration_ceiling_mps2=selected_power / (total_mass_kg * speed_mps),
    )
