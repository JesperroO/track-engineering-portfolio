# Engineering contribution and evidence

[Portfolio contents](README.md)

I drive, acquire and analyse motorsport data, and build software for telemetry processing and vehicle/lap-time modelling. My entry point for a team is data preparation, performance analysis, testing support and simulation/control development.

## Real-track cases

| Case | Evidence | Engineering focus |
|---|---|---|
| [P1 aprilia GPR150](case_studies/p1-gpr150-telemetry.md) | 71 timed laps in nine sessions; 60.022 to 55.496 s reference progression; selected actual onboard frames | OBD throttle/RPM, T2 deceleration proxies, HR response, lean duration and schematic-map line comparison |
| [Session feedback loop](TRACKSIDE_FEEDBACK_LOOP.md) | Dated reviews and next-run decisions | Translate a diagnosis into one controlled practice task and inspect the response |

## Simulation cases

The [simulation overview](SIM_RACING.md) describes a wider multi-car archive and four focused performance cases. The strongest examples are:

- [MX-5 / Lime Rock](case_studies/lime-rock-mx5-race-analysis.md): P16 to official P5; accepted 57.784 s race PB; qualifying S1 accounts for 60.5% of the pole gap; seven major slow intervals cost 28.50 s against the planning baseline.
- [F4 / Paul Ricard](case_studies/paul-ricard-f4-development.md): match a 78,431-frame replay export to actual CM laps, compare a 0.623 s S1 gain through brake release and exit speed, and distinguish wheel-load observations from setup-test results.
- [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md): 50 Hz / 64,544 samples; valid-medium progression, wheel-speed lockup, pressure/temperature asymmetry, compound validity and fuel context.

- [Three-race comparison](case_studies/paul-ricard-race-consistency.md): compare representative pace, incident recovery, late-race gains and cut-lap patterns.

## Further real-track case: CBR650R

| Case | Evidence | Engineering focus |
|---|---|---|
| [Hualong CBR650R](case_studies/hualong-cbr650r.md) | Four sessions; comparable best 47.869 to 42.641 s | OBD signal calibration, comparable-lap selection and low-rate GPS limitations |

## What I can contribute

| Team task | Evidence from the work |
|---|---|
| Prepare a trustworthy session dataset | Log real-track GNSS/IMU/OBD and video; check clocks, GPS quality and lap boundaries; recover missing simulator channels |
| Explain where performance is lost | aprilia GPR150 geographic sectors and linked-corner gains; MX-5 qualifying/loss allocation; F4 reference-speed comparison |
| Turn vehicle traces into a test | Compare brake-release shapes, wheel unloading and front-lockup signals; define a separate pressure or brake-bias trial |
| Debrief repeatability as well as PB | Review aprilia GPR150 multi-session progression and consecutive laps; compare three simulator races using median/MAD, damage and cuts |
| Support real-world acquisition | Personally ride and log motorcycle sessions; combine GNSS/IMU/OBD and video while controlling data quality |
| Implement models and tools | Python analysis/rendering, native binary reading, CasADi dynamics/OCP experiments and solver diagnostics |

## Implementation and scope

The private archive includes 26 modelling modules, 41 analysis/rendering tools and 15 model-test modules in the previously inventoried toolchain. This is separate from the wider local simulation export archive, which currently has 331 saved per-lap CSV files; the latter is a file inventory, not a valid-lap count.

[Technical profile](TECHNICAL_PROFILE.md) maps the tools and implementation to the case results. Published charts and aggregate values have [source notes](assets/sim/README.md). The portfolio retains observations, completed analyses and proposed tests as distinct results, with raw logs and private records kept locally.

## Acquisition and analysis workflow

The final supporting chapter, [from real-track acquisition to an engineering decision](case_studies/data-acquisition-workflow.md), explains how I log GNSS/IMU/OBD and onboard video, retain source files, check clocks and channel quality, select comparable laps, and turn the review into the next test. It also covers simulator source recovery and missing-channel handling.
