# CBR650R / Hualong — practice analysis

[Portfolio contents](../README.md)

**28 July 2026 · 2020 Honda CBR650R · four practice sessions**

I rode and analysed a four-session day on the compact Hualong circuit, using RaceChrono, OBD, heart-rate data and onboard footage. The comparison focused on early deceleration, coasting and repeated throttle applications through a driving corner.

## Session comparison

The comparable best lap improved from **47.869 s** in S01 to **44.421 s** in S02 and **42.641 s** in S04: a total gain of **5.228 s**. S03's 44.412 s record is retained as provisional because merged laps and degraded GPS interrupted the timing and position comparison.

I removed out-laps, in-laps and unstable segments, then used GPS for broad speed/position trends and OBD for throttle-event timing. Throttle was scaled over its recorded endpoints to compare opening, release and sustained input across laps.

## Driving sequence

I examined the transition from approach braking to minimum speed, maintenance throttle and a continuous exit roll-on. The faster laps carried more usable throttle time, while repeated opening and waiting phases remained in the selected corner.

The target action chain scored 1/6, 2/6 and 0/6 in the selected S01, S02 and S04 samples. Pace improved faster than the repeatability of that sequence, so I kept brake release and a single exit roll-on as the next practice focus.

My riding notes describe low-grip conditions and the transition between braking, small throttle input and standing the motorcycle up for drive. I used those notes with the OBD trace and video to select the control sequence for review. The low-rate phone GPS supports the session-level speed comparison; detailed line work uses the better-instrumented P1 programme.

## Work completed

I produced a comparable-lap selection, normalized throttle traces, session summaries and a corner-action review in Python and an Excel workbook. These outputs informed the next practice focus: shorten the waiting phase and repeat one continuous drive sequence through the exit.
