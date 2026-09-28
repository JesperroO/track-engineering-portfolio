# Case study: Silverstone GT1 simulation telemetry

**Date:** 2026-09-12
**Platform:** Assetto Corsa simulation
**Vehicle:** GT1-class simulation car
**Context:** pre-qualification practice
**Primary question:** can a telemetry comparison turn a driving observation into a controlled setup test?

## Dataset

The final practice capture contained 50 Hz telemetry and 64,544 samples. The analysed channels included:

- individual wheel speeds;
- throttle and braking;
- brake bias;
- tyre pressure and temperature state;
- fuel use;
- lap and sector timing.

The raw high-frequency file is intentionally not included in the public repository.

## Result

Three valid medium-tyre laps progressed from `2:13.739` to `2:10.561` to `2:07.571`. The top speed changed by only about `0.2 km/h` between the last two laps, while full-throttle time increased by `7.8 s` and braking time fell by `0.6 s`. The observed gain therefore pointed toward corner execution and throttle connection rather than a straight-line-speed change.

The telemetry also showed front-wheel lockup signals around heavy-braking zones, with the right front most prominent. This made brake release and peak pedal application a more useful next question than moving the braking point earlier.

## Single-variable test logic

The proposed next test was:

> Change front brake bias from `61.0%` to `60.5%`; hold the rest of the setup fixed; compare front-wheel lockup and exit performance in Village, Becketts, and Vale.

This is a test plan, not a claimed result. The portfolio preserves the distinction between a telemetry observation, a proposed intervention, and the result that would only exist after the intervention is run.

## Why this case matters

The simulation environment provides higher-rate channels than the real-track motorcycle sessions and makes individual-wheel and tyre-state reasoning visible. Its role here is to demonstrate telemetry handling and controlled-test design, not to substitute for real vehicle or professional race-team experience.
