# Portfolio overview

I drive, acquire and analyse motorsport data, and build software for telemetry processing and vehicle/lap-time modelling. My entry point for a team is data preparation, performance analysis, testing support and simulation/control development.

## What I can contribute

| Team task | Evidence from the work |
|---|---|
| Prepare a trustworthy session dataset | Recover a complete shared replay, decode native best-lap data, check lap transitions and identify stale capture metadata |
| Explain where performance is lost | MX-5 qualifying-sector allocation, race slow-lap loss budget, F4 server speed comparison, Silverstone late-lap loss map |
| Turn vehicle traces into a test | Compare brake-release shapes, wheel unloading and front-lockup signals; define a separate pressure or brake-bias trial |
| Debrief repeatability as well as PB | Compare three races using median/MAD, retained chronological pace, damage episodes and cuts; review GT3 stint convergence |
| Support real-world acquisition | Personally ride and log motorcycle sessions; combine GNSS/IMU/OBD and video while controlling data quality |
| Implement models and tools | Python analysis/rendering, native binary reading, CasADi dynamics/OCP experiments and solver diagnostics |

## Simulation cases

The [simulation overview](SIM_RACING.md) describes a wider multi-car archive and six focused engineering cases. The strongest examples are:

- [MX-5 / Lime Rock](case_studies/lime-rock-mx5-race-analysis.md): P16 to official P5; accepted 57.784 s race PB; qualifying S1 accounts for 60.5% of the pole gap; seven major slow intervals cost 28.50 s against the planning baseline.
- [F4 / Paul Ricard](case_studies/paul-ricard-f4-development.md): match a 78,431-frame replay export to actual CM laps, compare a 0.623 s S1 gain through brake release and exit speed, and distinguish wheel-load observations from setup-test results.
- [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md): 50 Hz / 64,544 samples; valid-medium progression, wheel-speed lockup, pressure/temperature asymmetry, compound validity and fuel context.
- [Three-race comparison](case_studies/paul-ricard-race-consistency.md) and [Kyalami GT3 practice](case_studies/kyalami-720s-practice.md): show that peak speed, a narrow representative band, incident recovery and a successful race entry are different outcomes.
- [Acquisition and recovery](case_studies/sim-data-acquisition.md): choose among replay, native `.tc`, direct capture and Live Telemetry according to actual channel coverage.

## Real-track cases

| Case | Evidence | Engineering focus |
|---|---|---|
| [P1 GPR150](case_studies/p1-gpr150-telemetry.md) | 71 timed laps in nine sessions; 60.022 to 55.496 s reference progression; selected actual onboard frames | Quality checks, geographic alignment, linked corners, inferred gear and video context |
| [Hualong CBR650R](case_studies/hualong-cbr650r.md) | Four sessions; comparable best 47.869 to 42.641 s | OBD signal calibration, comparable-lap selection and low-rate GPS limitations |
| [Session feedback loop](TRACKSIDE_FEEDBACK_LOOP.md) | Dated reviews and next-run decisions | Translate a diagnosis into one controlled practice task and inspect the response |

## Implementation and scope

The private archive includes 26 modelling modules, 41 analysis/rendering tools and 15 model-test modules in the previously inventoried toolchain. This is separate from the wider local simulation export archive, which currently has 331 saved per-lap CSV files; the latter is a file inventory, not a valid-lap count.

[Technical profile](TECHNICAL_PROFILE.md) maps the tools and implementation to the case results. Published charts and aggregate values have [source notes](assets/sim/README.md). The portfolio retains observations, completed analyses and proposed tests as distinct results, with raw logs and private records kept locally.
