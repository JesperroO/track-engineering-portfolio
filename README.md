# Track Engineering Portfolio

I am a computer science and engineering student who drives, acquires data and builds analysis tools for motorsport. My work combines real-track motorcycle telemetry with simulation race analysis, vehicle modelling and control-oriented numerical methods.

The portfolio shows practical outputs: a lap comparison, a braking trace, a tyre or wheel-state diagnosis, a loss budget, and a specific instruction for the next session.

## Simulation race engineering

The [simulation portfolio](SIM_RACING.md) now covers formal race review, driver-input analysis, stint consistency, F4 development, GT1 tyre/brake analysis, GT3 practice and acquisition recovery.

| Selected work | Evidence | Engineering result |
|---|---|---|
| [MX-5 / Lime Rock](case_studies/lime-rock-mx5-race-analysis.md) | Full shared replay, native best lap, qualifying and official results | S1 contributes 60.5% of the qualifying gap; 7 slow intervals cost 28.50 s; recover the continuous 57.784 s PB pedal trace |
| [Three-event consistency](case_studies/paul-ricard-race-consistency.md) | 26 / 12 / 14 completed intervals across three races | Separate robust pace, recovery losses, late-race speed and valid-lap repeatability |
| [F4 / Paul Ricard](case_studies/paul-ricard-f4-development.md) | 78,431 replay frames matched to CM timing; archived server reference | Identify a 0.623 s S1 gain, inspect wheel unloading and keep setup variants and event restrictions explicit |
| [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md) | 50 Hz, 64,544 samples, tyre/sector records and saved setup | Map gains and late-lap losses; inspect front-wheel lockup, tyre asymmetry, fuel and a brake-bias test |
| [GT3 / Kyalami](case_studies/kyalami-720s-practice.md) | ACC results, logs and retained setup | Build a twelve-lap practice baseline and quantify the final five-lap pace band |

![F4 S1 control comparison](assets/sim/f4-s1-release.png)

## Real-track motorcycle engineering

I independently perform the riding, logging and analysis for the motorcycle work. The acquisition programme uses RaceChrono Pro, GNSS/IMU, OBD-II and onboard cameras, with Python processing and source-quality checks.

- [P1 GPR150](case_studies/p1-gpr150-telemetry.md): nine sessions, 71 timed laps and a reference progression from 60.022 to 55.496 s; geographic sectors, linked-corner continuity and selected onboard frames.
- [Hualong CBR650R](case_studies/hualong-cbr650r.md): four practice sessions; OBD throttle calibration, comparable-lap selection and explicit handling of GPS degradation.
- [Trackside feedback loop](TRACKSIDE_FEEDBACK_LOOP.md): post-session review becomes a one-turn or one-variable task, followed by a check of what the next session actually demonstrated.

The 25 Hz and multi-camera details describe the wider acquisition programme; individual case pages use session-specific claims only where their source records support them.

## Data, simulation and numerical implementation

The [technical profile](TECHNICAL_PROFILE.md) describes Python/NumPy/Matplotlib/OpenCV, binary best-lap reading, replay integration, Live Telemetry, RaceChrono/VBO exports and CasADi vehicle models. The [acquisition case](case_studies/sim-data-acquisition.md) shows how I recover missing channels and detect discontinuities or incorrect session metadata.

[Vehicle and lap-time modelling](modelling/lap-time-modelling.md) covers GGV envelopes, motorcycle dynamics, fixed-line/free-path formulations and exploratory SSN/KKT work. These are modelling experiments with explicit feasibility and validation status.

## Reading the portfolio

Start with the [overview](PORTFOLIO.md), then a case relevant to the task. The simulator cases give a car-focused view of race data and engineering decisions; the real-track cases add physical acquisition, riding context and imperfect-sensor handling. [Figure provenance](assets/sim/README.md) records the sources and recomputed checks behind the simulator charts.

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

This public repository contains selected analysis, aggregate evidence, charts and curated video frames. Original replays, raw telemetry, exact GNSS traces, private media, health records, local paths and unfiltered session conversations stay in the private archive. The experience presented here comes from personal driving and engineering project work.
