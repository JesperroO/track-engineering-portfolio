# GPR150 / Subo: rider and motorcycle adapting to a new circuit

[Visual case, Chinese](../previews/subo/index.html) · [Six-page PDF](../assets/subo/subo-case-study.pdf) · [中文分析与证据口径](../zh/subo-gpr150.md)

On 6 October 2026, I rode an Aprilia GPR150 at Subo in Guangzhou, acquired telemetry and supplied trackside feedback. The work combines linked-corner time accounting with rider-state analysis. AI collaboration supported processing, figures and review; riding, observations, questions and corrections came from the rider.

## Repeatable pace

Best lap improved from 62.118 s in the morning to 60.741 s. Fourteen afternoon/evening laps were below 61.6 s. The three fastest laps in the 17:19 session were separated by 0.326 s.

![Session best laps](../assets/subo/pace.svg)

## A process improvement can lose time downstream

In the 18:14 session, lap 9 spent 0.816 s less waiting at low speed before the T8 transition than lap 4. It gained 0.181 s by the intermediate gate, then lost 0.762 s through T9 and the downstream section: the complete T7–T9 package was 0.582 s slower.

![Fixed-gate cumulative time comparison](../assets/subo/linked-time.svg)

There was also a successful example: in the 17:19 session, lap 6 had a T7 peak 3.109 km/h lower than lap 3, yet completed T7–T9 0.754 s faster. Its tail section then lost 0.550 s. The result changed the acceptance criterion from faster speed recovery to complete linked-corner and downstream time.

The 18:14 lap 9 tail advantage survived to the end of the main-straight study window: 0.150 s faster than lap 4. This supports a local reference, not a universal best lap or a causal claim about the widest entry.

## Heart rate has a repeatable spatial structure

![Heart-rate profiles after removing each lap's linear time trend](../assets/subo/heart-position.svg)

Raw heart rate fell in the T13-exit/T14 region in 33 of 35 retained laps, with a median local drop of approximately 1.7 bpm across five sessions. After removing each lap's linear time trend, 34 laps showed a decrease.

The rider suggested that smoother riding through the long T13 left-hander contributed to the later trough. The trough followed the upright crossing by a median of about 3 s, but its location did not strongly track the variation in that crossing. This remains a working explanation; rider effort, breathing and sensor effects are not separated.

## Team tasks and work evidence

|Task|Evidence from the work|
|---|---|
|Account for linked-corner gains|Track 0.181 s gained upstream and 0.762 s returned downstream using fixed geographical planes.|
|Evaluate exits|Extend the tail comparison to the straight's final study gate rather than rank speed-recovery time alone.|
|Integrate rider and motorcycle data|Compare heart-rate time progression, spatial profiles and reported fatigue/pressure.|
|Maintain test provenance|Retain original hypotheses, execution identity, counterexamples and current status.|
|Correct measurement-based attribution|Withdraw a T9 0.6 s loss claim affected by a cross-session common-position offset.|

## Measurement boundaries

Subo had no OBD data; lean is GPS-calculated, not a measured chassis attitude. Raw CSV/VBO, complete GNSS and private records remain local. Heart-rate profiles exclude first laps, unclosed tails and final yielding candidates; exploratory spatial findings await independent replication. The relative reference path is approximately 883 m, distinct from the circuit's advertised 1100 m. The diagram is used for turn identification and display, not performance calculations. Warmers and stable 1.70/1.60 bar hot readings provide a working setup baseline, not an optimum-pressure claim.
