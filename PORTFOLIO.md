# Portfolio overview

## Position

Computer-science and engineering student working on personal motorsport data systems, vehicle-dynamics analysis, and lap-time modelling. The practical focus is turning imperfect telemetry into bounded, reviewable engineering decisions.

The most relevant direction for a race-team conversation is engineer/data support: data preparation, channel and timing checks, lap and sector comparison, setup-test bookkeeping, and clear separation between what the data shows and what still needs confirmation.

## Selected case studies

| Case | Evidence | Engineering focus |
|---|---|---|
| [P1 GPR150, 2026-09-03](case_studies/p1-gpr150-telemetry.md) | 71 timed laps across nine sessions; reference pace `60.022 → 55.496 s` | GPS quality, geographic alignment, linked corners, inferred gear, throttle continuity, video-alignment planning |
| [Hualong CBR650R, 2026-07-28](case_studies/hualong-cbr650r.md) | Four practice sessions; comparable best `47.869 → 42.641 s` | OBD throttle calibration, lap comparison, data-quality gating, limits of low-rate GPS |
| [Silverstone GT1 simulation, 2026-09-12](case_studies/silverstone-gt1-sim.md) | 50 Hz telemetry; 64,544 samples | Four-wheel speed, lockup signals, brake bias, tyre state, fuel, single-variable test design |

## Transferable engineering habits

- Start with the acquisition contract: sample rate, clock, channel meaning, missing data, and lap segmentation.
- Prefer geographic gates or source-consistent timing when distance channels cannot be compared directly.
- Treat gear labels, line explanations, and control interpretations as derived or provisional when they are not direct measurements.
- Use repeated laps and sector allocation, not a single personal-best number, to identify whether a change is repeatable.
- Turn a suspected cause into a controlled next test, such as changing brake bias while holding the rest of the setup fixed.
- Write down the uncertainty that would be removed by a synchronized video view, a better sensor, or a physical inspection.

## Relation to AGAC / Super Taikyu conversations

The portfolio is relevant to a student engineer/data discussion because it demonstrates the workflow around telemetry: organizing observations, checking data quality, comparing laps, tracking control traces, and designing the next measurement. It does not present private team experience or imply independent responsibility for a professional race car.

The strongest honest framing is: an existing personal track-data programme and simulation-analysis practice, with the goal of learning and contributing within a professional race-engineering workflow.

## Publication boundary

The public repository contains only explanatory Markdown. Raw telemetry, video, spreadsheets, exact coordinates, private media references, health records, local paths, and internal solver diagnostics stay in the private archive.
