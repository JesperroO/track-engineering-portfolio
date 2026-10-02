# Trackside feedback loop

[Portfolio contents](README.md)

I use session review to choose the focus for the next run:

```text
run a session
    -> export and audit the data
    -> identify one repeatable problem in one turn or linked section
    -> choose one change for the next session
    -> run the change while keeping the rest stable
    -> compare the new evidence and keep, reject, or refine the hypothesis
```

Each review identifies a corner or sequence to work on and a result to compare after the next run.

## P1 CBR650R: from a full-session impression to a one-turn drill

### Evidence after the first session

The first P1 session produced six complete laps and showed stable deep-lean samples around T14/T18, while T2 contained repeated throttle attempts. Video and telemetry showed early speed unloading, a waiting phase and a second control input while completing the turn.

### Decision for the next session

The next run was narrowed to one correction at a time:

- pre-position the body before turn-in;
- carry a light, continuous brake release into the turn;
- reach the apex with one stable maintenance-throttle phase;
- let the motorcycle stand up into one continuous roll-on;
- leave the other turns at the established baseline.

The plan explicitly rejected using a larger peak lean angle as the task. T2 or T18 was a repeatable test location; the observable outcome was a clean roll-in, apex platform, and single exit drive.

### What the next data showed

I aligned the later video review to TrackAddict using a visible camera timestamp and a fixed `17.0 s` offset. In the usable rear-camera segment, several laps showed a continuous `40–46°` roll-in and roll-out. The focused session also produced two approximately `59 s` laps and a later `47°` right-turn frame. The video review showed repeatable posture and vehicle motion; throttle timing remained a focus for the later OBD-instrumented programme.

The full-day sector comparison then showed improvement in all four coarse geographic sections: approximately `1 s`, `1 s`, `1 s`, and `2 s`, for a `1:03.994 → 58.998 s` representative-lap change. The improvement was distributed across the lap.

## Hualong CBR650R: baseline, single-variable practice, and data gates

The Hualong practice plan assigned a role to each session:

| Stage | On-track role | Decision rule |
|---|---|---|
| S01 | Dry baseline | Establish comparable laps and the recorded throttle/control pattern |
| S02 | Single-variable practice | Repeat the selected control idea after recovery; do not change several setup or riding variables together |
| S03 | Optional video/verification stage | Keep the data provisional when RaceChrono merged laps or GPS quality degraded |
| S04 | Comparable confirmation sample | Use only stable laps and stop when the tyre/track condition introduced a new uncontrolled variable |

The best comparable lap moved from `47.869 s` to `44.421 s` and then `42.641 s`, but the action-chain score for the selected drive corner was `1/6`, `2/6`, and `0/6` in the comparable S01, S02, and S04 samples. Pace improved while the target action chain remained inconsistent.

I calibrated the OBD throttle channel, selected comparable laps and reviewed the target corner between sessions. S03 remains a provisional trend: merged laps and degraded GPS limit precise cross-session comparison.

## P1 aprilia GPR150: session progression and review

The September P1 programme contains nine sessions and 71 timed laps. I rode S04–S07 consecutively and reviewed them afterward.

- The S06 review identified a late-lap continuity pattern: the quickest complete T2 gate was not necessarily the quickest T2-plus-following-right complex.
- S07 supplied a repeatable seven-lap band and a faster complete opening complex without requiring the fastest standalone T2 gate.
- After S07, the documented decision was one more short, controlled session using the existing `56 s` rhythm as the ceiling rather than an immediate personal-best attack.
- S08 then produced `55.496 s`, but the post-session comparison showed that the gain was distributed: `0.400 s` in the `60–70%` region and `0.243 s` in the final `10%`, while `0.450 s` was returned in the immediately following `70–80%` transition.
- S09 changed purpose after the displayed lap entered the `58 s` range: it became deliberate right-turn exploration rather than continued personal-best assembly.

## Silverstone GT1 simulation: from observation to the next controlled test

The same loop exists in the simulation work. Three valid medium-tyre laps progressed from `2:13.739` to `2:10.561` to `2:07.571`. Fifty-hertz telemetry showed almost unchanged top speed, longer full-throttle time, less braking time, and front-wheel lockup signals around heavy-braking zones.

The resulting next-session instruction was concrete:

> Change front brake bias from `61.0%` to `60.5%`; hold the rest of the setup fixed; compare front-wheel lockup and exit performance in Village, Becketts, and Vale.

The brake-bias change remains a proposed test.

## F4 simulation: learn from a local gain and an incomplete setup fix

The [F4 case](case_studies/paul-ricard-f4-development.md) shows a further turn-by-turn loop. A repeated S2 wheel-unload event prompted separate damping and rear-pressure variants. Event restrictions removed damping from the legal race setup; the pressure trial retained a valid 91.005 s lap but did not remove the repeated loss at the same transition. I retained the driving-transition problem as the next review focus.

A separate S1 comparison finds 18.054 s versus 18.677 s, with earlier brake release and higher exit speed. The whole L28 lap remains slower, so the next task is to reproduce that control sequence inside a clean lap. The server speed comparison also identified a larger deficit in the final braking sequence.

## Race review: preserve representative pace and the disruption timeline

The [three-race comparison](case_studies/paul-ricard-race-consistency.md) places the median/MAD pace band alongside repairs, damage episodes and cut laps. A narrow retained pace band can coexist with a badly interrupted race; a late PB can coexist with invalid following laps. I use the review to target consecutive valid laps at the improved pace.

## Review tasks

My session reviews cover:

- fast post-session data triage under limited track time;
- selecting one turn or linked section instead of changing the whole lap at once;
- translating a data trace into a clear riding instruction;
- holding setup, gear, line, or measurement conditions stable where possible;
- using video, telemetry, and my riding notes as separate evidence layers;
- checking the target control sequence alongside lap-time improvement;
- flagging laps affected by poor data quality or synchronization and selecting comparable runs.
