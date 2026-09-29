# Track Engineering Portfolio

An evidence-bounded motorsport data and vehicle-dynamics portfolio built around real-track motorcycle telemetry, onboard video, simulation telemetry, and lap-time modelling.

The project is aimed at student engineer / data roles and technical conversations with race teams. It documents how measurements are acquired, checked, connected to visual evidence, transformed into derived quantities, and used to form testable engineering hypotheses.

The current evidence package includes a nine-session P1 GPR150 programme with 71 timed laps, a reference progression from `60.022 s` to `55.496 s`, real onboard video/proxy material, and selected frame exports from daylight, overcast, and night running. The public figures show lap progression, geographic sector gains, and the relationship between a local T1 gate and the full-lap result.

## What this portfolio covers

- Real-track motorcycle data: 25 Hz GNSS, IMU, and OBD-II acquisition, with lap and sector comparison, racing-line analysis, throttle and braking/deceleration behaviour, and consistency/repeatability analysis.
- Video evidence: the private real-track archive contains multi-camera onboard material and proxy exports, including multiple camera files for one P1 session. The public version contains selected still frames only; cross-camera time synchronization remains an explicit analysis step rather than an implied completed result.
- Simulation telemetry: higher-rate traces with individual wheel speeds, brake bias, tyre state, fuel use, throttle, and braking channels.
- Modelling experiments: GGV envelopes, transient minimum-lap-time formulations, optimal-control formulations, and an exploratory SSN/KKT solver direction.

The 25 Hz and multi-camera details are project-level acquisition facts confirmed for the real-track programme. They are not assigned to every session by default. The case pages use session-level values only where the internal session reports or acquired media support them, and keep the raw files in a separate private archive.

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

## Visual evidence

The portfolio includes selected frame exports from the real-track video archive and figures regenerated from the dated P1 analysis tables. They show the evidence chain at three levels: what the camera saw, how lap time progressed, and where the measured gains were distributed.

<p align="center">
  <img src="assets/p1/video_frames/p1-s04-day-corner-01.jpg" alt="P1 daytime corner frame" width="31%" />
  <img src="assets/p1/video_frames/p1-s07-overlay-straight.jpg" alt="P1 onboard frame with timing display" width="31%" />
  <img src="assets/p1/video_frames/p1-s08-night-corner-02.jpg" alt="P1 night corner frame" width="31%" />
</p>

<p align="center">
  <img src="assets/p1/p1-lap-progression.png" alt="P1 GPR150 lap progression across 71 timed laps" width="96%" />
</p>

<p align="center">
  <img src="assets/p1/p1-sector-gains.png" alt="P1 sector gain heatmap across four reference transitions" width="96%" />
</p>

The full [P1 case study](case_studies/p1-gpr150-telemetry.md) contains the larger frame gallery and the T1 gate analysis. The public repository stores only these derived images; the original video archive remains private.

## Scope and privacy

This is a sanitized public presentation layer. It intentionally excludes health and DEXA records, exact GPS traces and unnecessary location detail, private original media, local filesystem paths, raw high-frequency logs, temporary solver outputs, and personal equipment or riding records.

The underlying `track_engineering` repository remains an internal research archive. This portfolio is a selected account of methods and results, not a mirror of that archive and not a claim of professional race-engineer experience.
