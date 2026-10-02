# T2 analysis: event definitions and sources

[Portfolio contents](../README.md)

The sequential comparison retains S02 and S04–S08, totalling 47 timed laps in the same external-GPS programme. S01/S03 use different GPS schemas. S09 became deliberate right-turn practice. The five selected session-PB event timings reproduce the existing channel summary.

- Deceleration onset: calculated longitudinal G ≤-0.15 for 0.20 s before the principal early deceleration trough. Sensitivity repeats the detection at -0.10 and -0.20 G.
- Left-lean landmark: calculated lean ≤-20° for 0.20 s after deceleration onset.
- Main-left minimum: minimum GNSS speed after the start of the main left and before the fixed T2 exit plane.
- Stable opening: archived normalized OBD throttle ≥40% for 0.30 s, searched after the larger of the principal deceleration-trough time and minimum-speed time minus 2 s. Laps already above the threshold at the search boundary are flagged in the per-lap evidence.
- Normalization: archived OBD endpoints 1.56863–94.5098%. Throttle values are plotted on that common scale.
- Event timing: 20 Hz interpolation provides consistent threshold evaluation. It does not change the independent sampling rate of the original OBD channels.
- Position: one rigid metric coordinate frame, rotated to the approach direction. The origin is S08 L8 deceleration onset. Projected position is distinct from distance travelled along a lap.
- Gates: fixed geographic entry/exit planes from the previous-day S04 L3 reference, with forward crossings interpolated between samples.

Calculated G and lean identify repeatable event landmarks. They are not direct brake-pressure or steering-input channels. GNSS and event detection uncertainty matter for metre-scale line differences; the figures retain the recorded trajectories without independently fitting each lap onto a common rail.

The S04 clip uses the VBO main-video clock. Visual checks at the upright/deceleration transition and main-left lean agree at approximately half-second inspection resolution. The S04 clip illustrates execution in an intermediate session, separately from the S02/S08 comparison.

The downstream timing and speed values in the main text are reproduced from the existing fixed-gate progression summary. The differences shown are observed comparisons; no isolated setup effect is inferred.

[Back to the study](p1-gpr150-analysis.md#t2-lines-control-and-reference-development)
