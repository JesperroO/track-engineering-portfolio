# Engineering contribution and evidence

[Portfolio contents](README.md)

## Real-track cases

| Case | Evidence | Engineering focus |
|---|---|---|
| [P1 aprilia GPR150](case_studies/p1-gpr150-telemetry.md) | 71 timed laps in nine sessions; 60.022 to 55.496 s reference progression; synchronized T2 onboard video | OBD throttle/RPM, T2 deceleration proxies, HR response, lean duration and schematic-map line comparison |
| [Session feedback loop](TRACKSIDE_FEEDBACK_LOOP.md) | Dated reviews and next-run decisions | Translate a diagnosis into one controlled practice task and inspect the response |

## Simulation cases

[Simulation overview](SIM_RACING.md)

- [MX-5 / Lime Rock](case_studies/lime-rock-mx5-race-analysis.md): P16 to official P5; accepted 57.784 s race PB; qualifying S1 accounts for 60.5% of the pole gap; seven major slow intervals cost 28.50 s against the planning baseline.
- [F4 / Paul Ricard](case_studies/paul-ricard-f4-development.md): match replay lap transitions to CM timing, compare brake release and exit speed in a 0.623 s S1 gain, then inspect rear-wheel load and the results of a pressure test.
- [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md): valid laps on medium tyres improve from 133.739 to 127.571 s; right-front lockup at 90.15–90.71% lap progress informs a proposed brake-bias test.

- [Three-race comparison](case_studies/paul-ricard-race-consistency.md): compare representative pace, incident recovery, late-race gains and cut-lap patterns.

## Further real-track case: CBR650R

| Case | Evidence | Engineering focus |
|---|---|---|
| [Hualong CBR650R](case_studies/hualong-cbr650r.md) | Four sessions; comparable best 47.869 to 42.641 s | Throttle normalization, duration-weighted use, target-event screening and OBD speed/RPM comparison |

## What I can contribute

| Team task | Evidence from the work |
|---|---|
| Prepare session data | Log real-track GNSS/IMU/OBD and video; check clocks, GPS quality and lap boundaries; recover missing simulator channels |
| Explain where performance is lost | aprilia GPR150 geographic sectors and linked-corner gains; MX-5 qualifying/loss allocation; F4 reference-speed comparison |
| Turn vehicle traces into a test | Compare brake-release shapes, wheel unloading and front-lockup signals; define a separate pressure or brake-bias trial |
| Debrief repeatability as well as PB | Review aprilia GPR150 multi-session progression and consecutive laps; compare three simulator races using median/MAD, damage and cuts |
| Support real-world acquisition | Ride and record motorcycle sessions; align GNSS/IMU/OBD with video and check channel coverage |
| Implement models and tools | [CBR650R inputs, envelope and path/speed results](modelling/cbr650r-p1-model.md); [runnable QSS code](modelling/code/README.md) |

## Implementation

[Tools and implementation](TECHNICAL_PROFILE.md) · [Simulation figure sources and calculations](assets/sim/README.md)

## Acquisition and analysis workflow

[Acquisition and trackside review](case_studies/data-acquisition-workflow.md) covers the sensor connections, source files, clock checks, video alignment and pit-room review, followed by simulator data recovery.
