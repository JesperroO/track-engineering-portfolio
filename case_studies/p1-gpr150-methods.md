# aprilia GPR150 / P1 — measurement and source notes

[Project showcase](p1-gpr150-telemetry.md) · [Detailed analysis](p1-gpr150-analysis.md) · [Portfolio contents](../README.md)

## Source channels

RaceChrono exports retain GNSS position/speed/precision, OBD RPM/throttle/coolant and chest-strap HR. Longitudinal/lateral G and lean are RaceChrono **calculated** channels. GPS speed is used with OBD RPM because the ECU speed PID is unusable. Throttle is normalized over the archived **1.56863–94.5098%** endpoints. The common 20 Hz event-analysis grid interpolates the logged channels; it retains their original source-rate limitations.

## T2 events

[T2 event definitions and source details](p1-t2-development-method.md) specify sustained deceleration, main-left lean and throttle-opening thresholds. Deceleration represents net longitudinal change; lean landmarks represent calculated roll-state events. Brake pressure and steering angle were not recorded.

## Fixed geographic comparisons

The T2 package uses fixed transverse planes from the Sep 2 S04 L3 reference: entry at 2.82 s, exit at 12.37 s and downstream endpoint at 18.50 s. All 71 laps cross these planes in time order, using interpolated crossings. The principal comparison uses S02 and S04–S08; S01/S03 have different GPS schemas and S09 changes the exercise.

The whole-lap studies use G10–G90 transverse planes at 10% increments of **S08 L8's reference GPS path**. G0/G100 retain recorded lap endpoints. The same planes apply to each lap; forward crossings are interpolated with progress-order checks. Section totals are not rescaled. G60–G80 are reference stations, not corner numbers or each lap's own distance percentages.

Spatial figures use a shared local east/north frame with the S08 L8 start as origin. Curves retain each lap's measured path. The PB map colours each interval by its complete fixed-gate time difference; it does not encode pointwise delta within that interval. Positive gains mean the later lap traversed the interval faster.

Control plots begin at a common geographic gate or at each lap's minimum-speed event, as labelled. An equal elapsed time can correspond to different track positions. GNSS precision and path differences limit physical interpretation; milliseconds are displayed to make the arithmetic inspectable.

## Heart-rate windows

The deceleration trough anchors each event. HR is interpolated onto a 20 Hz grid and median-filtered over five seconds. The baseline is the median from −3 to −1 s; the response summary is the maximum from +2 to +12 s minus baseline. The new trace panel shows the relative HR shape for three selected laps. The session panel uses the retained full-session aggregates: dots are medians and vertical segments are the 25th–75th percentiles. The window spans later cornering and sensor delay, so it cannot isolate a physiological reaction to braking. Session 9 has no HR.

## Video and map alignment

The S04 L4 clip uses the VBO's `avisynctime` mapping. Index 1 supplies the continuous main-video clock through later overlapping camera-index changes. L4 starts approximately 2.21 s into the excerpt. The onboard previous-lap display rounds to 57.5 s, matching L3's recorded 57.488 s. Upright/deceleration and main-left-lean picture checks agree at approximately half-second inspection resolution.

The BT.2020/HLG source is converted to BT.709 SDR with a Hable tone map and highlight desaturation. The short rendered clip preserves engine audio. Other camera files require their own alignment.

One similarity fit registers S08 L8 to the existing P1 main-corridor schematic; the same transform applies to S02 and its events. Fit discrepancy is approximately 18 px RMS, about 3 m at that scale. The map provides schematic correspondence to the raised kerb, with no surveyed pavement or apex claim.

## Photographed-board comparisons

The same similarity registration used by the published T2 comparison also places the linked-corner lines, geographic gates, PB interval gains and HR window on the photographed P1 board. Its parameters were recovered from the published S08 overlay, then applied unchanged to every compared lap. Recovery discrepancy against that rendered line is below one board pixel; this is separate from the original approximately 18 px schematic-fit discrepancy. Each trajectory retains its measured shape and relative position.

Board colours distinguish laps or interval gains as indicated by each legend. Native metric and control figures provide the quantitative comparisons alongside the board views.

## Supporting comparisons

The S09 exercise reuses the published G60/G70/G80 crossing times. The directional-lean panel uses per-session medians from the retained whole-lap lean summary; open circles show right lean and crosses left lean. S09 has no HR channel.

Gear-trial and same-session trace figures interpolate native GNSS crossings of the original three T2 planes. Their display crossings can differ by approximately 0.01–0.03 s from the retained analysis-grid aggregates. The text uses the retained aggregate package results; neither timing series is rescaled. Squares mark each lap's T2 exit. All throttle traces use the same archived-endpoint normalization.

The deceleration display uses a five-sample moving mean on the 0.05 s grid. Its onset markers and reported effective-average values come from the retained channel aggregates. Speed loss divided by onset-to-minimum elapsed time supplies the average net-deceleration proxy.

## Session context

S04–S07 were ridden consecutively without interim telemetry debriefs. Their changes are retrospective observations. The generic pit-room review workflow is documented separately in the [acquisition chapter](data-acquisition-workflow.md).

Rider feedback supplies the progressively moved physical braking reference, deliberate third-gear trial, tyre-pressure observations and S09 exercise objective. Gear is rider-confirmed or inferred from RPM/speed; transient ratios also depend on clutch state and cross-channel timing.

The broader previous-day 60.022 s reference gives approximately 1.50 s improvement across the T2/downstream package (15.692 → 14.192 s). This spans acquisition schemas; the same-programme comparison carries the main result.

[Project showcase](p1-gpr150-telemetry.md) · [Detailed analysis](p1-gpr150-analysis.md)
