# aprilia GPR150 / P1
## Real-track data acquisition & performance analysis

[Portfolio contents](../README.md) · [Detailed analysis](p1-gpr150-analysis.md) · [Measurement methods](p1-gpr150-methods.md)

![aprilia GPR150 on track at P1](../assets/p1/p1-showcase-on-track.png)

**Independent project · September 2026 · riding / acquisition / analysis**

I built a budget-conscious telemetry workflow for my own track riding, then combined recorded lines, OBD channels, heart rate and onboard video to explain performance differences. My work covered sensor integration, data preparation, event detection, geographic comparisons and the presentation of evidence.

The archive covers **nine sessions and 71 timed laps**. Its value is the ability to follow a difference from the physical braking reference through the control sequence to the time retained at the next corner.

### Selected work

- [T2 event comparison](#t2-lines-control-and-reference-development) — relate braking position, lean and throttle opening; track repeatability across 47 laps.
- [Linked corners and gain attribution](#whole-lap-performance-studies) — locate gains and losses using common geographic gates, measured lines and control traces.
- [OBD and rider-state analysis](#obd-control-timing-and-rider-state-analysis) — examine engine recovery, lean duration and event-aligned heart rate.
- [Acquisition and evidence delivery](#acquisition-and-evidence-delivery) — connect the recording stack, synchronized video and trackside review.

## T2: lines, control and reference development

**Engineering work:** I compared laps in one spatial frame and detected sustained deceleration, lean and throttle events. A chronological view of all 47 comparable laps shows how the braking reference moved and how its repeatability developed.

![T2 recorded lines and braking reference on the photographed P1 board](../assets/p1/aprilia-gpr150-p1-line-events.png)

In the selected S02 L2 / S08 L8 pair, deceleration starts **12.3 m farther downstream**, while the 20° lean landmark stays near the same approach position. Sustained 40% throttle moves from **1.50 to 0.10 s after minimum speed**. Comparing those events together connects the approach change to the exit sequence.

[![Play the synchronized T2 onboard excerpt](../assets/p1/aprilia-gpr150-t2-braking-reference.jpg)](https://raw.githubusercontent.com/JesperroO/track-engineering-portfolio/core/assets/p1/aprilia-gpr150-t2-braking-reference.mp4)

The **20-second S04 onboard excerpt** shows the raised kerb at the T1 kink and the main T2 left. The synchronized overlay and original engine audio give the event analysis a physical reference. The measured pair above is S02 / S08; the video illustrates the intermediate S04 session.

[Read the complete T2 study: lines, opening and 47-lap reference history](p1-gpr150-analysis.md#t2-lines-control-and-reference-development) · [Onboard and mapped reference](p1-gpr150-analysis.md#t2-onboard-example-developing-a-repeatable-braking-reference)

## Whole-lap performance studies

### Linked-corner diagnosis

**Engineering work:** I placed common geographic gates across laps and joined split times with measured paths, throttle, speed and lean. Comparing a complete corner sequence reveals whether a local gain survives the following transition.

![Linked-corner measured lines on the photographed P1 board](../assets/p1/p1-linked-board-lines.png)

The S06 L7 / S08 L8 comparison finds **0.431 s gained in one block and 0.461 s returned in the next**. The board shows the relative lines; the detailed control panels explain the sequence behind that trade-off. This supports a specific engineering question: which approach improves the whole linked section?

[Read the linked-corner diagnosis](p1-gpr150-analysis.md#1-linked-sequence-a-quicker-right-hand-block-can-cost-the-next-transition)

### Lap-time gain attribution

**Engineering work:** I partitioned laps with fixed geographic planes, computed interval gains and accumulated them around the circuit. A closer line/control comparison then examines the largest contributing package.

![Where the final lap improvement was gained and returned on the P1 board](../assets/p1/p1-pb-board-gains.png)

![Recorded L7 and L8 lines through the main gain package](../assets/p1/p1-pb-middle-board-lines.png)

The final **0.424 s** improvement contains only **0.036 s from the opening package**. G20–G40 contributes **0.371 s**; subsequent gains and losses explain the finish result. The method turns a lap-time number into locations and control sequences that can be examined.

[Read the gain attribution and closer G20–G40 comparison](p1-gpr150-analysis.md#2-s08-consecutive-pbs-where-the-final-0424-s-came-from) · [Fixed-gate definitions](p1-gpr150-methods.md#fixed-geographic-comparisons)

## OBD, control timing and rider-state analysis

**Engineering work:** I synchronized GPS speed with OBD engine speed and throttle, then aligned the comparisons at the corner minimum. Calculated lean adds episode shape and duration; heart-rate windows add a separate view of the rider response.

![GPS speed with OBD engine recovery and throttle timing](../assets/p1/p1-obd-engine-recovery.png)

Selected laps can have similar exit speed and different engine-speed recovery: S07 L5 exits at approximately **7,106 rpm**, against **9,346 rpm in S08 L8**. The combined channels make drivetrain and opening behaviour visible alongside the speed result.

The supporting studies compare **peak lean with time spent at deep lean**, and **event-aligned HR traces with session distributions**. Each uses a defined event and a comparable window, extending the analysis beyond single peak values.

[Engine recovery](p1-gpr150-analysis.md#engine-speed-recovery-what-the-speed-trace-leaves-out) · [Lean shape and duration](p1-gpr150-analysis.md#lean-the-shape-and-duration-of-the-cornering-episode) · [Heart-rate response](p1-gpr150-analysis.md#heart-rate-inspect-the-response-shape-against-the-session-pattern)

## Acquisition and evidence delivery

![Circuit Tools review on the pit-room laptop](../assets/workflow/p1-trackside-circuit-tools.png)

I use **RaceChrono** with GPS, IMU and a chest heart-rate strap, plus a **Vlinker MC+ BLE OBD2 interface** to the motorcycle's CAN-connected diagnostic port. A **DJI Action 5 Pro** records the helmet view. I align the video and telemetry afterwards, including additional camera views where available.

**Circuit Tools 3** on the pit-room laptop supports review between sessions and planning the next run. The analysis presented here also includes retrospective reconstruction of sessions ridden consecutively. Consumer hardware and DIY processing make the acquisition practical within my budget.

The published outputs include synchronized video, spatial event comparisons, line/control figures and inspectable aggregate results. Measurement definitions and detailed findings remain one click away.

[Acquisition and trackside workflow](data-acquisition-workflow.md) · [Complete analysis](p1-gpr150-analysis.md) · [Methods and source notes](p1-gpr150-methods.md) · [Aggregate evidence](../assets/p1/p1-development-detail-summary.json)

[Back to portfolio contents](../README.md)
