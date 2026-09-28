# Case study: Hualong CBR650R practice analysis

**Date:** 2026-07-28
**Vehicle:** 2020 Honda CBR650R
**Context:** four-session practice day on a compact circuit
**Primary question:** how much of the improvement was supported by comparable data, and where did the measurement limits stop the conclusion?

## Result

The comparable best lap improved from `47.869 s` in S01 to `42.641 s` in S04, a `5.228 s` reduction. S03 remained provisional because its automatic laps were merged and its GPS quality degraded.

| Session | Best lap | Data status |
|---|---:|---|
| S01 | `47.869 s` | comparable |
| S02 | `44.421 s` | comparable |
| S03 | `44.412 s` | provisional |
| S04 | `42.641 s` | comparable |

## Data and calibration

The session combined RaceChrono and OBD data. OBD throttle was treated as an observed ECU/PID signal and normalized over its recorded range; it was not presented as a physical throttle-plate angle or engine torque measurement.

The analysis first removed out-laps, in-laps, and unstable segments. S03 was kept in the archive but excluded from precise cross-session claims. GPS was used for position and speed trends, while OBD channels were used for control-event timing.

## What the comparison showed

- The faster session had higher overall pace, more usable throttle time, and a different control rhythm.
- The strict target sequence—approach, controlled minimum-speed phase, maintenance throttle, then continuous roll-on—was not confirmed as stable across all selected laps.
- A low-rate phone-GPS trace could support broad trends, but it could not support metre-level racing-line claims or prove that the remaining time was caused by lean angle alone.
- The analysis kept low-grip feedback, line choice, throttle input, and tyre condition as separate possible contributors instead of forcing them into one explanation.

## Engineering interpretation

This case is useful because the headline result is easy to over-read. A `5.228 s` improvement is a measured timing difference between selected laps; it is not by itself proof of a single technique, vehicle-state change, or transferable performance gain.

The useful engineering output is the data-quality gate: decide which laps can be compared, calibrate the meaning of each channel, then state what additional sensor or video evidence would be needed for a stronger line or braking conclusion.
