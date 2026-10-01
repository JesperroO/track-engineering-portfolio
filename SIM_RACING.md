# Simulation racing: driving, data and engineering decisions

I drive the sessions and carry out the data preparation, analysis and follow-up work. The simulation archive covers rear-wheel-drive cup cars, front-wheel-drive touring cars, F4, GT1 and GT3. It includes formal online races, practice, native best-lap records, replay reconstruction and continuous telemetry capture.

The useful work is the combination: find where time is lost, inspect the control or vehicle-state trace, select a practice or setup change, and check whether the next run supports it.

## Selected engineering work

| Work | Concrete result | What I did |
|---|---|---|
| [MX-5 / Lime Rock qualifying and race](case_studies/lime-rock-mx5-race-analysis.md) | P16 to P5; accepted race PB 57.784 s; S1 accounts for 60.5% of the qualifying gap | Reconstruct a complete shared replay, reconcile timing sources, quantify valid-lap supply and slow-lap losses, recover the continuous best-lap pedal trace |
| [Three-event race consistency](case_studies/paul-ricard-race-consistency.md) | Compare 26, 12 and 14 completed intervals; separate late-race pace gains from consistency and incident recovery | Apply a common median/MAD rule across different cars and tracks, retain excluded laps, join damage episodes and cuts with the lap timeline |
| [SMP F4 / Paul Ricard development](case_studies/paul-ricard-f4-development.md) | Four consecutive valid practice laps; a 0.623 s S1 gain with earlier brake release and higher exit speed | Match a 78,431-frame replay export to CM lap records, compare controls and wheel loads, inspect a server speed reference, manage distinct setup tests |
| [GT1 / Silverstone](case_studies/silverstone-gt1-sim.md) | Three valid medium-tyre laps: 133.739 to 127.571 s; 50 Hz and 64,544 samples | Analyse time-loss geography, wheel-speed lockup signals, tyre heat/pressure, compound comparability, fuel and brake-bias test design |
| [GT3 / Kyalami practice](case_studies/kyalami-720s-practice.md) | 12 recorded laps; best 106.337 s; final five-lap range 0.370 s | Reconcile ACC results and logs, quantify stint repeatability, preserve the setup baseline and distinguish practice pace from event admission |
| [Acquisition and source recovery](case_studies/sim-data-acquisition.md) | Recover useful channels when one recorder omits a lap or quantizes an input | Combine direct CSV capture, AC native `.tc`, CM results, replay-derived data and Live Telemetry; audit frame continuity and session metadata |

![F4 brake-release comparison](assets/sim/f4-s1-release.png)

The F4 figure is a local S1 comparison, not a claim that the faster sector made the whole lap faster. L28 has the stronger S1 but a slower complete lap. This is why I keep a sector result connected to the full-session record.

## Practice breadth

The local per-lap export archive currently contains **331 CSV files**, including a separately recovered reference export. The ordinary export groups include:

| Car / track combination | Saved export files |
|---|---:|
| MX-5 / Lime Rock | 169 |
| Hyundai Elantra N TCR / Zhejiang | 30 |
| Audi RS3 LMS TCR / Zhejiang | 15 |
| Honda Civic TCR / Zhejiang | 4 |
| Lotus Elise SC / Zhejiang | 13 |
| Lynk & Co 03 TCR / Brands Hatch Indy | 14 |
| Audi RS3 LMS TCR / Brands Hatch Indy | 11 |
| MX-5 / Brands Hatch Indy | 21 |
| Toyota GR86 Cup / Tsukuba | 28 |
| Lotus Exige S / Monza | 24 |
| LO206 kart / Conghua | 1 |

These are saved-file counts checked on 2026-10-01, not counts of valid, comparable laps. Some exports contain out-laps, aborted runs or resets. The TCR and other practice records establish breadth; the selected cases above carry the stronger, inspected engineering results.

## Working outputs

My outputs include lap/sector tables, input traces, loss allocation, repeatability statistics, damage timelines, acquisition checks and a next-session test instruction. A setup recommendation is evaluated against both the mechanism it targets and valid-lap performance. A new PB on its own does not identify why the car improved.

The tools are Python, NumPy, Matplotlib, native binary-file parsing, Content Manager/AC/ACC result records, Live Telemetry and an upstream replay parser. I distinguish my analysis and integration work from the third-party capture and parsing tools it uses.

[Figure provenance and aggregate evidence](assets/sim/README.md) explain the source of each published result. Original replays, full-rate logs, private session conversations and unfiltered participant records remain in the local archive.
