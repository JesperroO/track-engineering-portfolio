# T2: braking-reference development and corner-exit control

**aprilia GPR150 · P1 · 3 September 2026**

I rode repeated practice sessions, collected telemetry and onboard video, and analysed how the T2 approach developed across the day. Over several sessions I moved the braking reference downstream, eventually using the raised kerb at the T1 kink as the visual marker before the main T2 left.

This study follows the connection between braking-reference position, driven line, throttle opening and downstream speed. The sequential analysis covers **47 timed laps from S02 and S04–S08**.

## Braking later did not require a later lean landmark

![Recorded lines and event positions](../assets/p1/p1-t2-line-analysis.png)

**S02 L2 → S08 L8:** the recorded deceleration onset moves approximately **12.3 m downstream**, while the sustained 20° left-lean landmark stays in a similar approach position. The two laps therefore show a substantial change in the approach without an equivalent downstream shift of the lean landmark.

Both lines use the same metric coordinate frame. The larger diagram shows the corner sequence; the detail views isolate the approach events. Circles identify deceleration onset, squares sustained left lean of 20°, and triangles sustained 40% throttle.

## Earlier opening appears in the control sequence

![Speed, throttle and lean aligned at minimum speed](../assets/p1/p1-t2-control-analysis.png)

The curves align each lap at its T2 minimum speed, marked by the vertical zero line. Sustained 40% throttle arrives **1.50 s after minimum speed in S02 L2**, compared with **0.10 s in S08 L8**. The speed traces then separate through the exit while both laps remain substantially leaned over.

At the fixed T2 exit gate, speed increases **58.8 → 64.6 km/h**. At the downstream gate it increases **43.4 → 46.0 km/h**. The measured T2-plus-downstream package improves by **0.722 s**: **0.569 s in T2** and **0.152 s after it**, with rounding applied to the components.

The full-lap PB and the fastest opening package capture different strengths. S07 L5 traverses the same opening package in **13.940 s**, compared with **14.192 s for S08 L8**, despite its lower T2 exit speed. Exit speed and the following transition must therefore be read together.

A second pair illustrates the distinction: **S04 L7 → S06 L7** has later deceleration and a later lean landmark, but the delay to sustained 40% opening grows **0.35 → 0.95 s**. The effect of moving the reference depends on the accompanying entry and corner sequence.

## The reference moved, returned and became more repeatable

![All 47 laps in riding order](../assets/p1/p1-t2-reference-history.png)

Each point is one timed lap; session boundaries preserve the riding order. Position is projected onto the common approach axis, with **S08 L8 onset at 0 m**. Pale bars show how the detected point changes when the deceleration threshold varies from -0.10 to -0.20 G.

The clearest reversal occurs within S07. Its first five laps have median onset **+9.9 m**, while the final four return to **+0.6 m**. S08 stays near that returned region. The sequence records downstream shifts and returns within the practice day; rider feedback supplies the reasons for individual adjustments.

The logged full position range narrows from **22.3 m in S07** to **2.8 m in S08**. The middle-half ranges narrow from **9.0 m** to **1.1 m**. Varying the event threshold preserves the broad difference between the sessions. The result describes relative consistency in the recorded onset position.

S04–S07 were ridden consecutively without interim telemetry debriefs. This analysis reconstructs the practice retrospectively.

## The physical reference in the onboard video

[![T1 raised-kerb reference](../assets/p1/aprilia-gpr150-t2-braking-reference.jpg)](https://raw.githubusercontent.com/JesperroO/track-engineering-portfolio/core/assets/p1/aprilia-gpr150-t2-braking-reference.mp4)

[Play the T2 onboard clip](https://raw.githubusercontent.com/JesperroO/track-engineering-portfolio/core/assets/p1/aprilia-gpr150-t2-braking-reference.mp4)

The S04 excerpt shows the tucked approach, the raised-kerb reference before T2, the transition into the main left and the following exit. It supplies the physical setting for the reference development. The S02/S08 pair above supplies the measured comparison.

## Method

GNSS supplies position and speed; OBD supplies throttle and engine speed. Deceleration onset uses calculated longitudinal G ≤-0.15 for 0.20 s, and the lean landmark uses calculated left lean ≥20° for 0.20 s. Stable opening uses normalized OBD throttle ≥40% for 0.30 s. The main-corner minimum is selected before the fixed geographic T2 exit plane.

[Event definitions and source details](p1-t2-development-method.md) · [Aggregate per-lap evidence](../assets/p1/aprilia_GPR150_T2_exploration.json)

## Acquisition and trackside workflow

[How the real-track data and footage were captured and reviewed](data-acquisition-workflow.md)
