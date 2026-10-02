# Simulation racing: driving, data and engineering decisions

[Portfolio contents](README.md) · [中文概述](zh/sim-racing.md)

I drive the sessions and carry out the data preparation, analysis and follow-up work. My simulation work spans cup cars, TCR, F4 and GT cars. The selected cases cover race review, braking, wheel-load analysis and setup testing.

I locate time losses, inspect the control and vehicle-state traces, then select a driving exercise or setup test for the next run.

## Selected engineering work

| Work | Concrete result | What I did |
|---|---|---|
| [MX-5 / Lime Rock qualifying and race](case_studies/lime-rock-mx5-race-analysis.md) | P16 to P5; accepted race PB 57.784 s; S1 accounts for 60.5% of the qualifying gap | Reconstruct a complete shared replay, reconcile timing sources, quantify valid-lap supply and slow-lap losses, recover the continuous best-lap pedal trace |
| [Three-event race consistency](case_studies/paul-ricard-race-consistency.md) | Compare 26, 12 and 14 completed intervals; separate late-race pace gains from consistency and incident recovery | Apply a common median/MAD rule across different cars and tracks, retain excluded laps, join damage episodes and cuts with the lap timeline |
| [SMP F4 / Paul Ricard development](case_studies/paul-ricard-f4-development.md) | Four consecutive valid practice laps; a 0.623 s S1 gain with earlier brake release and higher exit speed | Match replay lap transitions to CM lap records, compare controls and wheel loads, inspect a server speed reference, manage distinct setup tests |
| [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md) | Three valid medium-tyre laps: 133.739 to 127.571 s; locate right-front lockup at 90.15–90.71% lap progress | Analyse time-loss geography, wheel-speed lockup signals, tyre heat/pressure, compound comparability, fuel and brake-bias test design |

![F4 brake-release comparison](assets/sim/f4-s1-release.png)

L28 gains 0.623 s in S1 through earlier brake release and a stronger exit. Its complete lap is slower than L15, so I selected that opening sequence for further practice within a clean lap.

## Working outputs

The linked cases contain sector comparisons, pedal and wheel traces, race-loss calculations and damage timelines. [Tools and implementation](TECHNICAL_PROFILE.md) describes the readers, data joins and calculations.

[Figure sources and aggregate results](assets/sim/README.md).

## Acquisition and analysis workflow

[Acquisition, processing and simulator recovery](case_studies/data-acquisition-workflow.md) describes how I record sessions and recover missing channels.
