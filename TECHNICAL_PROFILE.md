# Technical profile

[Portfolio contents](README.md)

I use this toolchain to acquire track data, analyse driving and vehicle response, align video, and build vehicle models.

## Toolchain

| Layer | Tools and data | What I use them for |
|---|---|---|
| Real-track acquisition | RaceChrono Pro, external GNSS/GPS, IMU, OBD-II, and onboard cameras | Session logging, lap timing, position and speed trends, control channels, and visual context |
| Export and inspection | RaceChrono CSV, VBO/Circuit Tools exports, GPX, JSON, and derived CSV tables | Preserve source records, compare schemas and clocks, and build auditable lap and sector summaries |
| Video workflow | DJI Action 5 Pro material, multi-camera onboard footage, MP4 proxy exports, and OpenCV-based utilities | Extract review frames, inspect my line and posture, and define explicit video-to-telemetry time anchors |
| Simulation acquisition and recovery | Assetto Corsa / ACC, Content Manager, native `.tc`, direct CSV capture, Live Telemetry 1.8.5, upstream `acreplay-parser` 0.3.0 and archived lapstat | Combine accepted timing, pedal traces, wheel loading, tyre state, damage/traffic and server speed references |
| Analysis software | Python 3.10+, uv, NumPy, Matplotlib, OpenCV, and pytest | Build repeatable ingestion, filtering, derived-channel, plotting, media, and regression-test workflows |
| Vehicle and lap-time modelling | CasADi, IPOPT/Fatrop-backed nonlinear optimisation, custom Python dynamics modules | Calculate drive/brake limits, fixed-line speed profiles, path optimisation, gear selection and constraint checks |
| Supporting tools | Excel workbooks and Open-Meteo historical weather data | Review session summaries, preserve hand-checkable tables, and separate measured conditions from reconstructed context |

## What I have built

My implementation covers acquisition, analysis, video alignment and numerical modelling:

- **Acquisition and data contracts:** identify source clocks, sampling behaviour, channel meaning, lap boundaries, missing data, GPS quality, and schema changes before comparing sessions.
- **Telemetry processing:** turn raw exports into session summaries, lap tables, geographic gates, sector allocations, GPS-yaw and kinematic signals, normalized throttle, and provisional gear inference.
- **Video and telemetry integration:** align camera and telemetry clocks using lap markers and visible start/finish crossings, then check the timing at braking and turn-in.
- **Vehicle-dynamics software:** implement road-frame motorcycle models, powertrain and gear logic, tyre-force interfaces, kinematic-demand checks, and fixed-line/free-path lap-time formulations.
- **Numerical engineering:** use CasADi automatic differentiation and nonlinear-programming interfaces, inspect constraint residuals and preserve failed solver states for diagnosis.
- **Experimental design:** convert a telemetry observation into a single-variable next test, such as changing front brake bias while holding the remaining setup fixed.
- **Reproducible outputs:** generate figures, model artifacts, session summaries and test reports from dated inputs.

## Evidence in the case studies

### P1 aprilia GPR150 real-track programme

I used fixed geographic gates to compare sessions with different GPS sources, then placed recorded lines and braking/throttle events on my photographed circuit board. The selected T2 pair shows deceleration beginning 12.3 m later and sustained 40% throttle moving from 1.50 to 0.10 s after minimum speed. The onboard excerpt uses the VBO video clock to align footage and telemetry.

### Simulation racing: performance, vehicle state and data integration

The [simulation overview](SIM_RACING.md) covers a multi-car workflow and dedicated cases:

- **MX-5 race analysis:** integrate official/game results, full shared replay and native best-lap data; allocate the qualifying gap, quantify slow-lap losses and recover an analog pedal-input trace when replay braking is binary.
- **Race consistency:** compare three events using a common median/MAD rule, retain excluded loss laps, and join damage episodes, repairs and cuts to the timeline.
- **F4 development:** match replay lap transitions to CM timing, compare brake-release and sector-exit behaviour, inspect low wheel-load phases, use a server speed reference and keep setup variants distinct.
- **GT1 practice:** compare four wheel speeds against brake input and vehicle speed, locate front lockup, and use tyre state and the saved setup to define a brake-bias test.
- **Acquisition checks:** inspect incomplete attempts, packet repetition and session-time resets; reject stale car/track capture labels through independent session identity.

The native `.tc` reading, dataset joins, derived analysis and charts are the personal implementation work. Replay decoding and high-rate capture use credited upstream tools.

### Hualong CBR650R practice analysis

The workflow combined RaceChrono, OBD, heart-rate data, action-camera evidence, derived CSV tables, and an Excel analysis workbook. OBD throttle was calibrated from its recorded endpoints; GPS was used for position and speed trends; degraded GPS and merged laps were gated out of precise comparison.

### Modelling and numerical methods

The [CBR650R / P1 worked model](modelling/cbr650r-p1-model.md) publishes the measured-data inputs, dyno curve, mass/geometry/gearbox values, adhesion scenarios, GPS scale-fit residual, calculated speed/gear policy and failed rate screen. The [selected runnable implementation](modelling/code/README.md) reproduces the archived 180-station fixed-line speed profile and 45.8689 s conditional QSS timing.


## Acquisition and analysis workflow

See the [final workflow chapter](case_studies/data-acquisition-workflow.md) for physical logging, source checks, video alignment and simulator data recovery.
