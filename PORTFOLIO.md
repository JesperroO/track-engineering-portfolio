# Portfolio overview

## Position

I build a personal motorsport data and vehicle-dynamics toolchain spanning real-track acquisition, video review, simulation telemetry, Python analysis, and lap-time modelling. The practical focus is turning imperfect telemetry into bounded, reviewable engineering decisions.

The practical focus is data preparation, channel and timing checks, lap and sector comparison, setup-test bookkeeping, and clear separation between what the data shows and what still needs confirmation.

The implementation behind the selected work includes RaceChrono and VBO/Circuit Tools exports, OBD-II and multi-camera video workflows, Assetto Corsa telemetry, Python/NumPy/Matplotlib/OpenCV, CasADi nonlinear optimisation, and pytest-based model checks. [Technical profile](TECHNICAL_PROFILE.md) maps those tools to the work they support.

## What this demonstrates

- I can take a mixed acquisition package—GPS/GNSS, IMU, OBD-II, timing records, VBO exports, and onboard video—and turn it into a traceable analysis dataset.
- I can distinguish raw measurements from derived quantities such as geographic gates, GPS yaw, normalized throttle, inferred gear, sector allocation, and kinematic demand.
- I can write analysis and rendering tools rather than relying only on a telemetry viewer: the underlying archive contains 26 modelling modules, 41 analysis tools, and 15 test modules.
- I can carry a result from observation to decision: identify a repeatable pattern, state the uncertainty, and propose the next controlled measurement or setup test.
- I can work across the full loop from data-quality audit to vehicle model, while keeping model assumptions and solver feasibility separate from real-vehicle performance.

## Selected case studies

| Case | Evidence | Engineering focus |
|---|---|---|
| [P1 GPR150, 2026-09-03](case_studies/p1-gpr150-telemetry.md) | 71 timed laps across nine sessions; reference pace `60.022 → 55.496 s`; actual onboard/proxy video with multi-camera material | GPS quality, geographic alignment, linked corners, inferred gear, throttle continuity, frame-level video evidence, synchronization boundaries |
| [Hualong CBR650R, 2026-07-28](case_studies/hualong-cbr650r.md) | Four practice sessions; comparable best `47.869 → 42.641 s` | OBD throttle calibration, lap comparison, data-quality gating, limits of low-rate GPS |
| [Silverstone GT1 simulation, 2026-09-12](case_studies/silverstone-gt1-sim.md) | 50 Hz telemetry; 64,544 samples | Four-wheel speed, lockup signals, brake bias, tyre state, fuel, single-variable test design |

## Transferable engineering habits

- Start with the acquisition contract: sample rate, clock, channel meaning, missing data, and lap segmentation.
- Prefer geographic gates or source-consistent timing when distance channels cannot be compared directly.
- Treat gear labels, line explanations, and control interpretations as derived or provisional when they are not direct measurements.
- Use repeated laps and sector allocation, not a single personal-best number, to identify whether a change is repeatable.
- Use frame-level video evidence to inspect line and visual context, while reserving time-specific control claims for explicitly aligned footage.
- Turn a suspected cause into a controlled next test, such as changing brake bias while holding the rest of the setup fixed.
- Write down the uncertainty that would be removed by a synchronized video view, a better sensor, or a physical inspection.

## Publication boundary

The public repository contains only explanatory Markdown. Raw telemetry, video, spreadsheets, exact coordinates, private media references, health records, local paths, and internal solver diagnostics stay in the private archive.
