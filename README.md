# Track Engineering Portfolio

An independent motorsport data and vehicle-dynamics portfolio built around real-track motorcycle telemetry, simulation telemetry, and lap-time modelling.

The project is aimed at student engineer / data roles and technical conversations with race teams. It documents how measurements are acquired, checked, transformed into derived quantities, and used to form testable engineering hypotheses.

## What this portfolio covers

- Real-track motorcycle data: 25 Hz GNSS, IMU, and OBD-II acquisition, with lap and sector comparison, racing-line analysis, throttle and braking/deceleration behaviour, and consistency/repeatability analysis.
- Video alignment: one real-track session included multi-channel acquisition with multi-camera onboard video. The public version contains no raw media or private media references.
- Simulation telemetry: higher-rate traces with individual wheel speeds, brake bias, tyre state, fuel use, throttle, and braking channels.
- Modelling experiments: GGV envelopes, transient minimum-lap-time formulations, optimal-control formulations, and an exploratory SSN/KKT solver direction.

The 25 Hz and multi-camera details are project-level acquisition facts confirmed for the real-track programme. They are not assigned to every session by default. The case pages use session-level values only where the internal session reports record them, and keep the raw files in a separate private archive.

## Engineering method

The workflow is deliberately evidence-first:

1. Audit sampling rate, timestamps, source clocks, channel availability, lap boundaries, and data quality.
2. Keep measured channels separate from derived quantities such as geographic gates, GPS yaw, inferred gear, sector composites, or normalized throttle.
3. State an engineering hypothesis separately from the observation that motivated it.
4. Compare laps and sectors only after the alignment and quality gates are explicit.
5. Use video or rider context to test interpretations that telemetry alone cannot identify.

This prevents a fast lap, a noisy channel, or a model output from being promoted into a stronger claim than the evidence supports.

## Selected work

- [Portfolio overview](PORTFOLIO.md)
- [P1 GPR150 real-track telemetry](case_studies/p1-gpr150-telemetry.md)
- [Hualong CBR650R practice analysis](case_studies/hualong-cbr650r.md)
- [Silverstone GT1 simulation telemetry](case_studies/silverstone-gt1-sim.md)
- [Vehicle and lap-time modelling](modelling/lap-time-modelling.md)

## Scope and privacy

This is a sanitized public presentation layer. It intentionally excludes health and DEXA records, exact GPS traces and unnecessary location detail, private original media, local filesystem paths, raw high-frequency logs, temporary solver outputs, and personal equipment or riding records.

The underlying `track_engineering` repository remains an internal research archive. This portfolio is a selected account of methods and results, not a mirror of that archive and not a claim of professional race-engineer experience.
