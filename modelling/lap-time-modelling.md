# Vehicle and lap-time modelling

[Portfolio contents](../README.md)

The modelling work is a secondary research track behind the measured telemetry case studies. It is included to show technical breadth, while keeping model outputs separate from observed track performance.

## Current directions

### GGV and vehicle envelopes

Scenario-based GGV-style envelopes are used to reason about available longitudinal and lateral demand, power limits, and motorcycle operating assumptions. The focus is on explicit input contracts and interpretable diagnostics, not on presenting an unvalidated envelope as a measured vehicle capability.

### Transient minimum-lap-time models

The repository contains reduced-transient and planar minimum-lap-time experiments, including longitudinal actuation, road-frame motorcycle dynamics, powertrain assumptions, and fixed-line or free-path formulations. These models ask how speed, path, and actuation constraints interact over a lap.

### Optimal control

The OCP work explores fixed-line, free-path, hybrid, and structured-transient formulations. Feasibility gates, solver diagnostics, and tests are treated as part of the result. A solver returning a trajectory is not by itself evidence that the trajectory is physically realizable or faster on track.

### SSN / KKT experiments

SSN and KKT-related experiments investigate structured nonlinear-solver steps and warm-start possibilities for the lap-time formulations. This is an exploratory numerical-method direction. It is not presented as an end-to-end race-engineering speedup or as independently validated vehicle performance.

## Modelling discipline

Each model should state:

1. which quantities are measured, assumed, identified, or generated;
2. which constraints are physical, numerical, or merely exploratory;
3. which tests and feasibility checks passed;
4. what remains unvalidated against instrumented vehicle data.

That boundary keeps the modelling work useful for future engineering collaboration without allowing mathematical sophistication to outrun the evidence from the real-track programme.
