# Trackside feedback loop

[Portfolio contents](README.md)

The central capability in this portfolio is the turnaround between sessions. A session is not treated as an isolated run or as a final lap-time number:

```text
run a session
    -> export and audit the data
    -> identify one repeatable problem in one turn or linked section
    -> choose one change for the next session
    -> run the change while keeping the rest stable
    -> compare the new evidence and keep, reject, or refine the hypothesis
```

The useful deliverable is often the next on-track decision: which turn to watch, which control event to change, and what result would count as improvement. The cases below show this loop at different levels of maturity.

## P1 CBR650R: from a full-session impression to a one-turn drill

### Evidence after the first session

The first P1 session produced six complete laps and showed stable deep-lean samples around T14/T18, while T2 contained repeated throttle attempts. The combined video and telemetry review showed that the main limitation was not simply reaching more lean angle. The more useful pattern was early speed unloading, a waiting phase, and a second control input while trying to complete the turn.

### Decision for the next session

The next run was narrowed to one correction at a time:

- pre-position the body before turn-in;
- use a light, continuous brake release rather than finishing all deceleration too early;
- reach the apex with one stable maintenance-throttle phase;
- let the motorcycle stand up into one continuous roll-on;
- leave the other turns at the established baseline.

The plan explicitly rejected using a larger peak lean angle as the task. T2 or T18 was a repeatable test location; the observable outcome was a clean roll-in, apex platform, and single exit drive.

### What the next data showed

I aligned the later video review to TrackAddict using a visible camera timestamp and a fixed `17.0 s` offset. In the usable rear-camera segment, several laps showed a continuous `40–46°` roll-in and roll-out rather than a sudden extra input. The focused session also produced two approximately `59 s` laps and a later `47°` right-turn frame. The evidence confirmed that I could repeat the posture and vehicle motion, while leaving the exact first-throttle timing open because the available GPS was too slow and the camera coverage did not show every control channel.

The full-day sector comparison then showed improvement in all four coarse geographic sections: approximately `1 s`, `1 s`, `1 s`, and `2 s`, for a `1:03.994 → 58.998 s` representative-lap change. That made the result a control-and-rhythm improvement across the lap, not a claim that one turn alone explained the gain.

## Hualong CBR650R: baseline, single-variable practice, and data gates

The Hualong plan treated the four sessions as an experiment sequence rather than four unrelated lap attempts:

| Stage | On-track role | Decision rule |
|---|---|---|
| S01 | Dry baseline | Establish comparable laps and the recorded throttle/control pattern |
| S02 | Single-variable practice | Repeat the selected control idea after recovery; do not change several setup or riding variables together |
| S03 | Optional video/verification stage | Keep the data provisional when RaceChrono merged laps or GPS quality degraded |
| S04 | Comparable confirmation sample | Use only stable laps and stop when the tyre/track condition introduced a new uncontrolled variable |

The best comparable lap moved from `47.869 s` to `44.421 s` and then `42.641 s`, but the action-chain score for the selected drive corner was `1/6`, `2/6`, and `0/6` in the comparable S01, S02, and S04 samples. The faster lap therefore did not automatically count as proof that the intended turn technique had become repeatable.

This is the engineering loop in practice: calibrate the OBD throttle channel, choose usable laps, identify the one-turn pattern, run the next session, and allow the quality gate to reject a tempting but unsupported conclusion. S03 remains in the archive as a provisional trend because its merged laps and degraded GPS make it unsuitable for precise cross-session inference.

## P1 aprilia GPR150: separating a real next-session decision from retrospective analysis

The September P1 programme contains nine sessions and 71 timed laps. It also demonstrates why an honest portfolio must distinguish a closed loop from a retrospective review.

- After S06, the analysis identified a late-lap continuity pattern: the quickest complete T2 gate was not necessarily the quickest T2-plus-following-right complex.
- S07 supplied a repeatable seven-lap band and a faster complete opening complex without requiring the fastest standalone T2 gate.
- After S07, the documented decision was one more short, controlled session using the existing `56 s` rhythm as the ceiling rather than an immediate personal-best attack.
- S08 then produced `55.496 s`, but the post-session comparison showed that the gain was distributed: `0.400 s` in the `60–70%` region and `0.243 s` in the final `10%`, while `0.450 s` was returned in the immediately following `70–80%` transition.
- S09 changed purpose after the displayed lap entered the `58 s` range: it became deliberate right-turn exploration rather than continued personal-best assembly.

I did not read interim analysis between S04 and S07. I analysed those sessions retrospectively, so their lap improvements cannot be attributed to an interim telemetry review. That distinction is part of the method.

## Silverstone GT1 simulation: from observation to the next controlled test

The same loop exists in the simulation work. Three valid medium-tyre laps progressed from `2:13.739` to `2:10.561` to `2:07.571`. Fifty-hertz telemetry showed almost unchanged top speed, longer full-throttle time, less braking time, and front-wheel lockup signals around heavy-braking zones.

The resulting next-session instruction was concrete:

> Change front brake bias from `61.0%` to `60.5%`; hold the rest of the setup fixed; compare front-wheel lockup and exit performance in Village, Becketts, and Vale.

That intervention is recorded as a proposed test, not as a completed validation. The same distinction applies on track: a good engineer records what changed before the next run and what the next run actually proved.

## F4 simulation: learn from a local gain and an incomplete setup fix

The [F4 case](case_studies/paul-ricard-f4-development.md) shows a further turn-by-turn loop. A repeated S2 wheel-unload event prompted separate damping and rear-pressure variants. Event restrictions removed damping from the legal race setup; the pressure trial retained a valid 91.005 s lap but did not remove the repeated loss at the same transition. That outcome keeps the driving/transition hypothesis alive instead of declaring the car fixed from a new PB.

A separate S1 comparison finds 18.054 s versus 18.677 s, with earlier brake release and higher exit speed. The whole L28 lap remains slower, so the next task is to reproduce that control sequence inside a clean lap. Archived server speed traces then shift some attention to a larger final-sector deficit rather than allowing the repeatedly troublesome curb to dominate all training.

## Race review: preserve representative pace and the disruption timeline

The [three-race comparison](case_studies/paul-ricard-race-consistency.md) places the median/MAD pace band alongside repairs, damage episodes and cut laps. A narrow retained pace band can coexist with a badly interrupted race; a late PB can coexist with invalid following laps. The resulting next-session decision concerns repeatable legal execution, not merely reproducing the fastest number.

## What this demonstrates

This workflow shows experience with:

- fast post-session data triage under limited track time;
- selecting one turn or linked section instead of changing the whole lap at once;
- translating a data trace into a clear riding instruction;
- holding setup, gear, line, or measurement conditions stable where possible;
- using video, telemetry, and my riding notes as separate evidence layers;
- recognizing when a change improved a lap but did not validate the intended mechanism;
- stopping or downgrading a conclusion when the data quality, synchronization, or experimental control is insufficient.
