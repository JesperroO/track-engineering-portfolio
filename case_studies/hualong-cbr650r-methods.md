# CBR650R / Hualong: methods and source notes

[Case study](hualong-cbr650r.md) · [中文](../zh/hualong-cbr650r.md)

## Sources and lap selection

The source is four RaceChrono Pro v10.2.4 exports from **28 July 2026**, the same-day analysis workbook, per-lap and throttle-event tables, riding notes and one saved S02 onboard frame.

The plotted laps are **S01 L4–L9, S02 L2–L7 and S04 L2–L7**. Out-laps, in-laps and cooldown running are excluded. Lap duration is the last minus first logged elapsed time within the automatic lap label, matching the archived derived tables.

S03 has merged automatic laps and repeated GPS-accuracy degradation to roughly 36–38 m. Its historical equal-split estimate of 44.412 s remains provisional and is excluded from the comparative figures.

## Channels and normalization

- **OBD:** speed, engine RPM and throttle. The channel plots use OBD speed in km/h and normalized throttle.
- **GPS:** position, distance travelled, speed and accuracy. Phone position updates are approximately 1 Hz. The export contains interpolated rows between those updates.
- **Lean:** RaceChrono-calculated lean. Selected-lap peak values retain the reported GPS accuracy at that sample in the public summary.
- **Heart rate:** chest-strap data. Filled points are each selected lap's mean of available readings; open points are its maximum.

Throttle uses the recorded endpoint values:

`normalized_throttle = clip((raw − 9.80392) / (90.19608 − 9.80392) × 100, 0, 100)`

The session throttle-use chart weights each reading by the elapsed interval to the next sample within the same lap. Intervals with unavailable throttle are excluded from its denominator. This yields **8.7176%, 14.5190% and 19.0786%** above 8% for S01/S02/S04. The earlier workbook's sample-count percentages were 8.6622%, 14.4046% and 18.9392%; the published chart uses duration weighting.

## Target-corner event rule

I preserve the same selection rule used in the original analysis:

1. Group consecutive available throttle readings into **closed ≤1%**, **small input >1–8%**, and **opening >8%**.
2. Select a closed run lasting at least 1 s, starting 65–105 m after the lap's first available throttle reading, followed by small input. Distance is the exported GPS-derived distance; this broad window locates the repeatable passage.
3. If several runs qualify, choose the one whose start is nearest 85 m.
4. Flag small input lasting at least 1 s and followed directly by the >8% state. Preserve the original duration convention: last minus first sample time plus 0.05 s.

This reproduces **1/6, 2/6 and 0/6** flags. The flag has no minimum duration for the subsequent >8% state. The continuous control plot therefore shows how long that opening lasts and whether another closure follows.

The selected columns are **S01 L6, S02 L2 and S04 L6**. Each is aligned at its own first small-input time. They compare the control sequence through the chosen passage; the horizontal axis is event-relative elapsed time.

## Figure sources

| Figure | Calculation or source |
|---|---|
| Session progression | Six selected lap durations per session, their mean and minimum; duration-weighted throttle states |
| Target sequences | Available normalized-throttle intervals from −4 to +9 s around the selected small-input onset |
| Corner controls | Original OBD throttle, speed and RPM, from −5 to +10 s around the same onset |
| Heart rate and lean | Mean/maximum recorded heart rate and maximum calculated lean for each selected lap |
| S02 onboard still | Original saved rear-facing frame, copied without colour or overlay edits |

The public [summary](../assets/hualong/hualong-analysis-summary.json) contains lap results, target-event durations and definitions. The [trace excerpts](../assets/hualong/hualong-selected-traces.json) contain relative time, throttle, OBD speed and RPM. Original GNSS coordinates, absolute timestamps, full telemetry and the workbook remain in the local track archive.
