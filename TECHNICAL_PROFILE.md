# Technical profile

This portfolio is backed by a working personal motorsport data and vehicle-dynamics toolchain. The public repository shows selected outputs and sanitized evidence; the raw telemetry, private media, exact coordinates, and full research archive remain private.

## Toolchain

| Layer | Tools and data | What I use them for |
|---|---|---|
| Real-track acquisition | RaceChrono Pro, external GNSS/GPS, IMU, OBD-II, and onboard cameras | Session logging, lap timing, position and speed trends, control channels, and visual context |
| Export and inspection | RaceChrono CSV, VBO/Circuit Tools exports, GPX, JSON, and derived CSV tables | Preserve source records, compare schemas and clocks, and build auditable lap and sector summaries |
| Video workflow | DJI Action 5 Pro material, multi-camera onboard footage, MP4 proxy exports, and OpenCV-based utilities | Extract review frames, inspect line and rider context, and define explicit video-to-telemetry time anchors |
| Simulation telemetry | Assetto Corsa, Content Manager, Live Telemetry 1.8.5, and SimTelemetry records | Analyse wheel speeds, throttle, braking, brake bias, tyre pressure/temperature, fuel, and sector timing |
| Analysis software | Python 3.10+, uv, NumPy, Matplotlib, OpenCV, and pytest | Build repeatable ingestion, filtering, derived-channel, plotting, media, and regression-test workflows |
| Vehicle and lap-time modelling | CasADi, IPOPT/Fatrop-backed nonlinear optimisation, custom Python dynamics modules | Implement GGV envelopes, fixed-line and free-path models, QSS and reduced-transient models, hybrid OCPs, gear policies, and solver diagnostics |
| Supporting tools | Excel workbooks and Open-Meteo historical weather data | Review session summaries, preserve hand-checkable tables, and separate measured conditions from reconstructed context |

## What I have built

The private implementation archive currently contains 26 Python `laptime` modules, 41 analysis and rendering tools, 15 pytest test modules, and 21 research notes. The work covers more than plotting a telemetry file:

- **Acquisition and data contracts:** identify source clocks, sampling behaviour, channel meaning, lap boundaries, missing data, GPS quality, and schema changes before comparing sessions.
- **Telemetry processing:** turn raw exports into session summaries, lap tables, geographic gates, sector allocations, GPS-yaw and kinematic signals, normalized throttle, and provisional gear inference.
- **Video and telemetry integration:** keep camera frames, lap markers, visible start/finish crossings, and telemetry timestamps as separate evidence until their alignment is demonstrated.
- **Vehicle-dynamics software:** implement road-frame motorcycle models, powertrain and gear logic, tyre-force interfaces, kinematic-demand checks, and fixed-line/free-path lap-time formulations.
- **Numerical engineering:** use CasADi automatic differentiation and nonlinear-programming interfaces, inspect feasibility and constraint residuals, and preserve failed solver states as diagnostics rather than presenting every trajectory as a result.
- **Experimental design:** convert a telemetry observation into a single-variable next test, such as changing front brake bias while holding the remaining setup fixed.
- **Reproducible outputs:** generate figures, JSON/NPZ artifacts, CSV summaries, dashboards, and test reports from dated inputs rather than manually editing a final chart.

## Evidence in the case studies

### P1 GPR150 real-track programme

Nine RaceChrono sessions and 71 timed laps were processed with GPS-quality checks, source/schema comparison, external-GPS reference selection, geographic sector gates, lap-progression tables, T1 summaries, and video-review shortlists. The wider archive also contains VBO exports and multiple onboard-camera files for one session. The public case study exposes the result figures and selected video frames while keeping the raw files private.

### Hualong CBR650R practice analysis

The workflow combined RaceChrono, OBD, heart-rate data, action-camera evidence, derived CSV tables, and an Excel analysis workbook. OBD throttle was calibrated from its recorded endpoints; GPS was used for position and speed trends; degraded GPS and merged laps were gated out of precise comparison. This is a concrete example of sensor semantics and data-quality control changing the conclusion.

### Silverstone GT1 simulation telemetry

An Assetto Corsa practice capture was recorded through Live Telemetry 1.8.5 at 50 Hz, producing 64,544 samples. The analysis joined lap timing with four wheel speeds, brake and throttle traces, brake bias, tyre state, fuel, and setup metadata. The result was a controlled next-test proposal, not a claim that a setup change had already been validated.

### Modelling and numerical methods

The secondary modelling track includes scenario-based GGV envelopes, planar and road-frame motorcycle dynamics, powertrain and gear-policy models, fixed-line and free-path minimum-lap-time formulations, reduced-transient and structured hybrid OCPs, and SSN/KKT experiments. Each model records its input contract, assumptions, feasibility gates, solver diagnostics, and validation status. Model output is kept separate from measured track performance.

## Public evidence boundary

The public repository contains representative figures, selected video frames, explanations, and the method used to interpret them. It does not contain private original video, raw high-frequency telemetry, exact track coordinates, health records, local filesystem paths, or temporary solver artifacts. The omission is deliberate: the portfolio demonstrates the engineering workflow without exposing unrelated personal data or an unfiltered research archive.
