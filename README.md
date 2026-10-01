# Track Engineering Portfolio

**[Preview the current P1 revision](previews/p1/README.md)** — photographic opening, rebuilt T2 analysis and the real-track acquisition workflow.

I am a computer science and engineering student who drives, acquires data and builds analysis tools for motorsport. My work combines real-track motorcycle telemetry with simulation race analysis, vehicle modelling and control-oriented numerical methods.

The portfolio shows practical outputs: a lap comparison, a braking trace, a tyre or wheel-state diagnosis, a loss budget, and an explanation of where performance was gained or returned.

## Real-track motorcycle engineering

I independently perform the riding, logging and analysis for the motorcycle work. The acquisition programme uses RaceChrono Pro, GNSS/IMU, OBD-II and onboard cameras, with Python processing and source-quality checks.

- [P1 aprilia GPR150](case_studies/p1-gpr150-telemetry.md): nine sessions, 71 timed laps and a reference progression from 60.022 to 55.496 s; OBD opening/RPM analysis, T2 deceleration and turn-in proxies, HR event windows, lean distributions, linked-sequence trade-offs and consecutive-PB gain allocation.
- [Trackside feedback loop](TRACKSIDE_FEEDBACK_LOOP.md): post-session review becomes a one-turn or one-variable task, followed by a check of what the next session actually demonstrated.

The 25 Hz and multi-camera details describe the wider acquisition programme; individual case pages use session-specific claims only where their source records support them.

### aprilia GPR150: onboard evidence and measured progression

The P1 programme connects actual onboard footage with lap progression and geographic sector analysis: what happened on track, how performance changed, and where the gains were distributed.

<p align="center">
  <img src="assets/p1/video_frames/p1-s04-day-corner-01.jpg" alt="P1 daytime corner frame" width="31%" />
  <img src="assets/p1/video_frames/p1-s07-overlay-straight.jpg" alt="P1 onboard frame with timing display" width="31%" />
  <img src="assets/p1/video_frames/p1-s08-night-corner-02.jpg" alt="P1 night corner frame" width="31%" />
</p>

<p align="center">
  <img src="assets/p1/p1-lap-progression.png" alt="P1 aprilia GPR150 lap progression across 71 timed laps" width="96%" />
</p>

<p align="center">
  <img src="assets/p1/p1-sector-gains.png" alt="P1 sector gain heatmap across four reference transitions" width="96%" />
</p>

The full [P1 case study](case_studies/p1-gpr150-telemetry.md) contains a [20-second T2 onboard/telemetry clip](case_studies/p1-gpr150-telemetry.md#t2-onboard-example-developing-a-repeatable-braking-reference), the larger frame gallery, T2 gate analysis and [three detailed performance studies](case_studies/p1-gpr150-telemetry.md#three-performance-studies). The public repository stores only these derived images; the original video archive remains private.

## Simulation race engineering

The [simulation portfolio](SIM_RACING.md) now covers formal race review, driver-input analysis, stint consistency, F4 development and GT1 tyre/brake analysis.

| Selected work | Evidence | Engineering result |
|---|---|---|
| [MX-5 / Lime Rock](case_studies/lime-rock-mx5-race-analysis.md) | Full shared replay, native best lap, qualifying and official results | S1 contributes 60.5% of the qualifying gap; 7 slow intervals cost 28.50 s; recover the continuous 57.784 s PB pedal trace |
| [Three-event consistency](case_studies/paul-ricard-race-consistency.md) | 26 / 12 / 14 completed intervals across three races | Separate robust pace, recovery losses, late-race speed and valid-lap repeatability |
| [F4 / Paul Ricard](case_studies/paul-ricard-f4-development.md) | 78,431 replay frames matched to CM timing; archived server reference | Identify a 0.623 s S1 gain, inspect wheel unloading and keep setup variants and event restrictions explicit |
| [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md) | 50 Hz, 64,544 samples, tyre/sector records and saved setup | Map gains and late-lap losses; inspect front-wheel lockup, tyre asymmetry, fuel and a brake-bias test |

![F4 S1 control comparison](assets/sim/f4-s1-release.png)

## Further real-track case: CBR650R

- [Hualong CBR650R](case_studies/hualong-cbr650r.md): four practice sessions; OBD throttle calibration, comparable-lap selection and explicit handling of GPS degradation.

## Vehicle modelling and numerical implementation

[Vehicle and lap-time modelling](modelling/lap-time-modelling.md) covers GGV envelopes, motorcycle dynamics, fixed-line/free-path formulations and exploratory SSN/KKT work. These are modelling experiments with explicit feasibility and validation status. The [technical profile](TECHNICAL_PROFILE.md) records the tools and implementation behind the cases.

## Reading the portfolio

Start with [aprilia GPR150](case_studies/p1-gpr150-telemetry.md) for personally acquired real-track data and visual evidence, continue with the [simulation cases](SIM_RACING.md), then [CBR650R](case_studies/hualong-cbr650r.md) for signal calibration and imperfect-sensor handling, followed by the [modelling work](modelling/lap-time-modelling.md). The [overview](PORTFOLIO.md) connects these outputs to engineering tasks.

## Scope and privacy

This public repository contains selected analysis, aggregate evidence, charts and curated video frames. Original replays, raw telemetry, exact GNSS traces, private media, health records, local paths and unfiltered session conversations stay in the private archive. The experience presented here comes from personal driving and engineering project work.

## Acquisition and analysis workflow

The final supporting chapter, [from real-track acquisition to an engineering decision](case_studies/data-acquisition-workflow.md), shows the RaceChrono Pro, GPS/IMU/heart-rate, vLinker MC+ BLE OBD and Action 5 Pro helmet-camera stack, Circuit Tools 3 review on the pit-room laptop, later multi-camera alignment and engineering within a self-funded budget. It also covers simulator source recovery and missing-channel handling.
