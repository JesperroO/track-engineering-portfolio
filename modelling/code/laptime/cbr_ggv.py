"""Scenario-based CBR650R / Road 6 GGv construction.

Every number that is not measured is carried as a named scenario.  The result
is a speed-dependent, asymmetric envelope suitable for the free-path OCP, not
a claim of the Road 6's absolute tyre limit.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

import numpy as np

from laptime.fixed_line import MotorcycleGGv
from laptime.powertrain import Gearbox, PowerCurve, power_limited_acceleration


G = 9.80665


@dataclass(frozen=True)
class CBRGGvScenario:
    name: str
    lateral_g: float
    tyre_braking_g: float
    rear_traction_g: float
    rider_mass_kg: float
    power_scale: float
    front_static_load_fraction: float
    combined_cg_height_m: float
    evidence_class: str


@dataclass(frozen=True)
class CBRGGvBuild:
    scenario: CBRGGvScenario
    envelope: MotorcycleGGv
    power_ceiling_mps2: np.ndarray
    wheelie_limit_mps2: float
    stoppie_limit_mps2: float


def initial_p1_scenarios() -> tuple[CBRGGvScenario, ...]:
    """Return named, auditable scenarios instead of an invented point estimate."""
    return (
        CBRGGvScenario(
            name="p1_observed_conservative",
            lateral_g=0.90,
            tyre_braking_g=0.846,
            rear_traction_g=0.90,
            rider_mass_kg=55.25,
            power_scale=0.95,
            front_static_load_fraction=0.46,
            combined_cg_height_m=0.65,
            evidence_class="P1 42-degree lean lower anchor plus independent Road 6 GT wet-braking average; deliberately conservative for dry P1",
        ),
        CBRGGvScenario(
            name="p1_observed_upper",
            lateral_g=1.07,
            tyre_braking_g=0.846,
            rear_traction_g=1.00,
            rider_mass_kg=52.25,
            power_scale=1.05,
            front_static_load_fraction=0.50,
            combined_cg_height_m=0.60,
            evidence_class="P1 approximately 47-degree lean anchor; longitudinal limits remain wet-test-conservative because no dry CBR brake measurement exists",
        ),
        CBRGGvScenario(
            name="p1_dry_ideal_nominal",
            lateral_g=1.15,
            tyre_braking_g=1.12,
            rear_traction_g=1.10,
            rider_mass_kg=52.25,
            power_scale=1.05,
            front_static_load_fraction=0.50,
            combined_cg_height_m=0.60,
            evidence_class="legacy dry sensitivity hypothesis; it is not constrained by the rider's 47-degree observation and is not a measured Road 6 force model",
        ),
        CBRGGvScenario(
            name="p1_dry_ideal_upper",
            lateral_g=1.22,
            tyre_braking_g=1.22,
            rear_traction_g=1.15,
            rider_mass_kg=52.25,
            power_scale=1.05,
            front_static_load_fraction=0.50,
            combined_cg_height_m=0.60,
            evidence_class="upper dry sensitivity hypothesis; it is not constrained by current rider capability, and longitudinal limits are clipped by explicit wheelie/stoppie geometry",
        ),
        CBRGGvScenario(
            name="p1_exploratory_49s_target",
            lateral_g=1.84,
            tyre_braking_g=1.22,
            rear_traction_g=1.15,
            rider_mass_kg=52.25,
            power_scale=1.05,
            front_static_load_fraction=0.50,
            combined_cg_height_m=0.60,
            evidence_class="inverse performance-target envelope: chosen to test a sub-49 s full-width line against P1 references; not a Road 6 force claim and not rider instruction",
        ),
        CBRGGvScenario(
            name="p1_exploratory_45s_target",
            lateral_g=2.00,
            tyre_braking_g=1.22,
            rear_traction_g=1.15,
            rider_mass_kg=52.25,
            power_scale=1.05,
            front_static_load_fraction=0.50,
            combined_cg_height_m=0.60,
            evidence_class="inverse competitive-target envelope: chosen to search the 45 s P1 class reference with the CBR full-width path; not a Road 6 force claim and not rider instruction",
        ),
        CBRGGvScenario(
            name="p1_vehicle_ideal_untrained",
            lateral_g=2.00,
            tyre_braking_g=1.22,
            rear_traction_g=1.15,
            rider_mass_kg=52.25,
            power_scale=1.05,
            front_static_load_fraction=0.50,
            combined_cg_height_m=0.60,
            evidence_class="working vehicle-only hypothesis: 2.0 g lateral envelope excludes present rider lean record, fatigue and current execution skill; it remains an uncalibrated Road 6 assumption pending future measurement",
        ),
    )


def _load_vehicle_inputs(manifest_path: Path) -> tuple[PowerCurve, Gearbox, float]:
    manifest = json.loads(manifest_path.read_text())
    vehicle = manifest["vehicle"]
    points = vehicle["rear_wheel_torque_curve"]["value"]
    curve = PowerCurve(
        rpm=np.asarray([point["rpm"] for point in points], dtype=float),
        rear_wheel_power_ps=np.asarray([point["power_ps"] for point in points], dtype=float),
    )
    assumptions = vehicle["powertrain_scenario_assumptions"]
    gearbox = Gearbox(
        ratios=np.asarray(vehicle["gear_ratios"]["value"], dtype=float),
        primary_reduction=float(vehicle["primary_reduction"]["value"]),
        final_reduction=float(vehicle["final_reduction"]["value"]),
        loaded_rear_radius_m=float(assumptions["loaded_rear_radius_m"]),
        usable_rpm_interval=tuple(map(float, assumptions["usable_engine_rpm_interval"])),
    )
    return curve, gearbox, float(vehicle["curb_mass_kg"]["value"])


def build_cbr_ggv(manifest_path: Path,
                  scenario: CBRGGvScenario,
                  speed_mps: np.ndarray | None = None) -> CBRGGvBuild:
    """Merge rear-wheel dyno power with named tyre/weight-transfer scenarios."""
    curve, gearbox, curb_mass = _load_vehicle_inputs(manifest_path)
    if speed_mps is None:
        # The QSS table must cover the CBR's mechanical top speed, not an
        # accidental kart-track cap.  Sixth-gear redline is the physical
        # endpoint implied by the supplied gearbox and dyno RPM interval.
        _, redline_rpm = gearbox.usable_rpm_interval
        sixth_redline_mps = redline_rpm / 60.0 * (2.0 * np.pi * gearbox.loaded_rear_radius_m) / (
            gearbox.ratios[-1] * gearbox.primary_reduction * gearbox.final_reduction
        )
        speed = np.linspace(8.0, sixth_redline_mps, 128)
    else:
        speed = np.asarray(speed_mps, dtype=float)
    if speed.ndim != 1 or len(speed) < 2 or np.any(speed <= 0.0) or np.any(np.diff(speed) <= 0.0):
        raise ValueError("speed_mps must be a strictly increasing positive grid")
    total_mass = curb_mass + scenario.rider_mass_kg
    power = power_limited_acceleration(speed, curve, gearbox, total_mass, scenario.power_scale)
    wheelbase_m = 1.45
    wheelie = G * scenario.front_static_load_fraction * wheelbase_m / scenario.combined_cg_height_m
    stoppie = G * (1.0 - scenario.front_static_load_fraction) * wheelbase_m / scenario.combined_cg_height_m
    drive = np.minimum.reduce((
        power.acceleration_ceiling_mps2,
        np.full_like(speed, scenario.rear_traction_g * G),
        np.full_like(speed, wheelie),
    ))
    brake = np.full_like(speed, min(scenario.tyre_braking_g * G, stoppie))
    lateral = np.full_like(speed, scenario.lateral_g * G)
    envelope = MotorcycleGGv(
        traction_and_lateral=np.column_stack((speed, drive, lateral)),
        braking_mps2=brake,
    )
    return CBRGGvBuild(
        scenario=scenario,
        envelope=envelope,
        power_ceiling_mps2=power.acceleration_ceiling_mps2,
        wheelie_limit_mps2=wheelie,
        stoppie_limit_mps2=stoppie,
    )
