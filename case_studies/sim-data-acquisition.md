# Simulation data engineering: capture, recovery and source semantics

The simulation work uses several acquisition paths because no single source preserves every useful channel or every failed attempt. I integrate the sources, check their meaning and coverage, and choose the smallest dataset that can answer the current question.

## Source selection

| Source | Useful evidence | Important constraint |
|---|---|---|
| CM/AC/ACC session results | Accepted lap times, sectors, cuts, tyre labels and session identity | Summary timing does not contain a complete high-rate vehicle-state trace |
| Native AC `.tc` | Best-lap speed, normalized pedal inputs and gear | A completed best/last lap can differ from the latest unfinished attempt |
| Replay plus upstream `acreplay-parser` | Session timeline, car positions, controls, wheel channels and damage | Coverage depends on the replay buffer; multiplayer channels can be quantized |
| Direct CSV polling | Packet IDs, time, lap progress, pedals, steering, gear, wheel slip/load/speed, pressure/temperature and assists | Repeated packet IDs and session resets must be checked before counting unique physics samples |
| Live Telemetry | Continuous high-rate vehicle and tyre channels, setup context | Startup metadata can be stale; an empty temporary file is not a completed capture |
| Archived server lapstat | Benchmark speed versus distance | Does not supply the reference driver's control inputs |

## Recovering an event after live logging was unavailable

For the MX-5 Lime Rock race, I combined a shared complete replay with a local tail buffer, official timing and native best-lap data. The 56,969-frame reconstruction restored the lap/traffic/damage timeline. When its brake channel proved binary, the `.tc` reader supplied the continuous accepted-PB input trace. This is a concrete source-recovery workflow rather than an assumption that every recorder saved equivalent data.

The binary-reader work locates the native header, accepted lap time and sample records, then exports speed, track progress, pedals and gear to analysis tables and plots. The upstream replay parser is credited separately; my work is the source integration, timing reconciliation and analysis built around it.

## Recording incomplete and invalid attempts

An earlier MX-5 T1 investigation exposed gaps in lap-based records: the latest unfinished attempt was not the completed lap held in `.tc`, and an alternative lap export had discontinuities around the critical event. The workflow added direct CSV capture so invalid or aborted running would remain inspectable.

A current audit of the preserved direct-capture file finds **152,189 polling rows**, four session-time resets and **18.14% adjacent repeated packet IDs**. I retain packet/time continuity checks instead of presenting polling rows as an equal number of unique physics frames. The current file is an acquisition example; its rows are not assigned wholesale to the earlier failed T1 attempt.

## Preventing silent session contamination

For F4, the 78,431-frame, 30 ms replay export is matched against CM valid-lap transitions. For Silverstone, a later incorrectly labelled telemetry filename is rejected after CM identifies the actual Macau/Evo session. These checks prevent comparing different sessions under the same apparent car/track label.

## Engineering outputs

The resulting analysis stack supports:

- valid-lap and source-coverage tables;
- speed/input traces and brake-event windows;
- four-wheel loading and lockup investigations;
- traffic and damage timelines;
- repeatability and cumulative-loss accounting;
- setup snapshots and separate single-variable test records.

The public [figures and aggregate evidence](../assets/sim/README.md) contain only selected explanatory outputs. Native binaries, complete replays, raw high-rate CSVs and participant-level exports remain private.
