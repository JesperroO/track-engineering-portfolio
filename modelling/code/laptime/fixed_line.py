"""Fixed-path quasi-steady motorcycle speed solve.

This is the speed-profile half of a minimum-lap-time method, not a racing-line
generator.  It uses the standard forward drive / backward brake feasibility
passes and a GGv friction ellipse.  Unlike TUM's generic helper interface, it
keeps positive drive and braking limits separate because they are materially
asymmetric for a motorcycle.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class FixedPath:
    """Closed path samples in physical metres, excluding the duplicated endpoint."""

    element_length_m: np.ndarray
    curvature_1_per_m: np.ndarray

    def __post_init__(self) -> None:
        if self.element_length_m.ndim != 1 or self.curvature_1_per_m.ndim != 1:
            raise ValueError("path inputs must be one-dimensional")
        if len(self.element_length_m) != len(self.curvature_1_per_m):
            raise ValueError("path length and curvature must have equal sample counts")
        if len(self.element_length_m) < 3 or np.any(self.element_length_m <= 0.0):
            raise ValueError("a closed path needs at least three positive-length elements")


@dataclass(frozen=True)
class MotorcycleGGv:
    """Speed-dependent positive longitudinal and lateral limits.

    Rows are ``[speed_mps, acceleration_mps2, lateral_acceleration_mps2]``.
    Braking is supplied separately because a motorcycle's braking envelope is
    asymmetric and must not be inferred from traction acceleration.
    """

    traction_and_lateral: np.ndarray
    braking_mps2: np.ndarray

    def __post_init__(self) -> None:
        ggv = self.traction_and_lateral
        if ggv.ndim != 2 or ggv.shape[1] != 3 or len(ggv) < 2:
            raise ValueError("GGv must have shape [n>=2, 3]")
        if not np.all(np.diff(ggv[:, 0]) > 0.0):
            raise ValueError("GGv speeds must increase strictly")
        if np.any(ggv[:, 1:] <= 0.0) or np.any(self.braking_mps2 <= 0.0):
            raise ValueError("acceleration, braking and lateral limits must be positive")
        if self.braking_mps2.shape != (len(ggv),):
            raise ValueError("braking limit must have one value per GGv speed")


@dataclass(frozen=True)
class FixedLineResult:
    speed_mps: np.ndarray
    time_s: np.ndarray
    iterations: int


def _interp(envelope: MotorcycleGGv, speed_mps: float, column: int) -> float:
    return float(np.interp(
        speed_mps,
        envelope.traction_and_lateral[:, 0],
        envelope.traction_and_lateral[:, column],
    ))


def _combined_longitudinal_limit(speed_mps: float,
                                 curvature_1_per_m: float,
                                 envelope: MotorcycleGGv,
                                 *,
                                 braking: bool,
                                 friction_scale: float,
                                 ellipse_exponent: float) -> float:
    """GGv longitudinal residual after paying the lateral acceleration demand."""
    ay_max = _interp(envelope, speed_mps, 2) * friction_scale
    ax_base = (
        float(np.interp(speed_mps, envelope.traction_and_lateral[:, 0], envelope.braking_mps2))
        if braking
        else _interp(envelope, speed_mps, 1)
    ) * friction_scale
    lateral_fraction = min(abs(curvature_1_per_m) * speed_mps**2 / ay_max, 1.0)
    residual = max(0.0, 1.0 - lateral_fraction**ellipse_exponent)
    return ax_base * residual ** (1.0 / ellipse_exponent)


def _lateral_speed_cap(curvature_1_per_m: float,
                       envelope: MotorcycleGGv,
                       friction_scale: float) -> float:
    """Largest tabulated speed satisfying v²|kappa| <= ay(v)."""
    speed_grid = np.linspace(
        envelope.traction_and_lateral[0, 0],
        envelope.traction_and_lateral[-1, 0],
        2049,
    )
    if abs(curvature_1_per_m) < 1e-12:
        return float(speed_grid[-1])
    feasible = speed_grid**2 * abs(curvature_1_per_m) <= np.interp(
        speed_grid,
        envelope.traction_and_lateral[:, 0],
        envelope.traction_and_lateral[:, 2],
    ) * friction_scale
    if feasible.any():
        return float(speed_grid[np.flatnonzero(feasible)[-1]])
    # The GGv table may begin above the tightest local corner speed.  NumPy's
    # interpolation elsewhere already holds the first table row at low speed;
    # use that same explicit low-speed extrapolation rather than creating a
    # fictitious zero-speed stop.
    return float(np.sqrt(envelope.traction_and_lateral[0, 2] * friction_scale / abs(curvature_1_per_m)))


def _brake_feasible_entry_speed(exit_speed_mps: float,
                                distance_m: float,
                                curvature_1_per_m: float,
                                upper_speed_mps: float,
                                envelope: MotorcycleGGv,
                                friction_scale: float,
                                ellipse_exponent: float) -> float:
    """Solve v_in² <= v_out² + 2*a_brake(v_in)*ds by bisection."""
    low, high = 0.0, upper_speed_mps
    for _ in range(48):
        trial = 0.5 * (low + high)
        braking = _combined_longitudinal_limit(
            trial, curvature_1_per_m, envelope,
            braking=True,
            friction_scale=friction_scale,
            ellipse_exponent=ellipse_exponent,
        )
        if trial**2 <= exit_speed_mps**2 + 2.0 * braking * distance_m:
            low = trial
        else:
            high = trial
    return low


def solve_closed_fixed_line(path: FixedPath,
                            envelope: MotorcycleGGv,
                            vehicle_mass_kg: float,
                            friction_scale: float = 1.0,
                            ellipse_exponent: float = 2.0,
                            convergence_mps: float = 1e-4,
                            max_iterations: int = 500) -> FixedLineResult:
    """Compute a closed minimum-time speed profile for one pre-defined path.

    ``friction_scale`` is intentionally explicit so a conservative Road 6
    envelope can be swept without relabelling a guess as measured grip.
    """
    if vehicle_mass_kg <= 0.0:
        raise ValueError("vehicle_mass_kg must be positive")
    if not 0.0 < friction_scale <= 1.0:
        raise ValueError("friction_scale must lie in (0, 1]")
    if ellipse_exponent <= 0.0:
        raise ValueError("ellipse_exponent must be positive")
    if convergence_mps <= 0.0 or max_iterations < 1:
        raise ValueError("convergence_mps and max_iterations must be positive")

    # The mass is carried in the constructed GGv (engine force, load transfer,
    # and brakes are all mass-dependent).  It remains an explicit argument so
    # callers cannot accidentally merge curves from different mass scenarios.
    _ = vehicle_mass_kg
    speed = np.array([
        _lateral_speed_cap(kappa, envelope, friction_scale)
        for kappa in path.curvature_1_per_m
    ])
    count = len(speed)
    for iteration in range(1, max_iterations + 1):
        previous = speed.copy()
        # Forward pass: finite available drive after lateral demand.
        for index in range(count):
            next_index = (index + 1) % count
            drive = _combined_longitudinal_limit(
                speed[index], path.curvature_1_per_m[index], envelope,
                braking=False,
                friction_scale=friction_scale,
                ellipse_exponent=ellipse_exponent,
            )
            reachable = np.sqrt(speed[index] ** 2 + 2.0 * drive * path.element_length_m[index])
            speed[next_index] = min(speed[next_index], reachable)
        # Backward pass: asymmetric braking limit after lateral demand.
        for index in range(count - 1, -1, -1):
            next_index = (index + 1) % count
            speed[index] = min(
                speed[index],
                _brake_feasible_entry_speed(
                    speed[next_index],
                    path.element_length_m[index],
                    path.curvature_1_per_m[index],
                    speed[index],
                    envelope,
                    friction_scale,
                    ellipse_exponent,
                ),
            )
        if np.max(np.abs(speed - previous)) <= convergence_mps:
            break
    else:
        raise RuntimeError("fixed-line QSS speed solve did not converge")

    next_speed = np.roll(speed, -1)
    dt = 2.0 * path.element_length_m / np.maximum(speed + next_speed, 1e-6)
    return FixedLineResult(speed_mps=speed, time_s=dt, iterations=iteration)
