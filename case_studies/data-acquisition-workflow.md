# Acquisition and analysis workflow: real track first

I independently ride, log and review the motorcycle sessions. This chapter connects the evidence in the performance cases to the practical work of obtaining usable data. The same source-checking approach also supports my simulator analysis.

## Real-track acquisition

| Source | How it enters the record | What it can support |
|---|---|---|
| RaceChrono Pro and GNSS | Session logging, lap markers, position, speed and GPS-quality fields; external GNSS in the higher-rate programme | Lap timing, geographic comparison, speed trends and selection of trustworthy reference laps |
| IMU / motion channels | Available motion and lean channels retained with their source definition | Compare transitions and motion episodes; distinguish recorded channels from GPS-derived yaw or acceleration |
| OBD-II | Available ECU/PID channels recorded with the session, including RPM and throttle where present | Control-event timing, engine-state context and calibrated signal comparison |
| Onboard cameras | Original footage retained by session; proxy files and selected frames prepared for review | Corner geometry, line, rider movement and a visual check on telemetry interpretations |
| Rider and session notes | Record the intended exercise, gear choice, changing conditions and feedback alongside the export | Interpret a trace in the context of what the rider actually attempted |

The wider programme includes 25 Hz GNSS acquisition, IMU and OBD-II. That does not assign 25 Hz to every channel: GPS source, availability and sampling behaviour are checked per export. The [GPR150](p1-gpr150-telemetry.md) and [CBR650R](hualong-cbr650r.md) cases show different source quality and coverage.

## From a session to a usable review

1. **Capture the run and its purpose.** Ride with the available logger and camera configuration; retain the session context and rider account. A deliberate technique exercise is identified separately from a PB attempt.
2. **Export and archive the originals.** Keep RaceChrono CSV, available VBO/Circuit Tools exports and original camera files under the dated session. Add a readable source manifest and review record; derived tables and video proxies remain separate from originals.
3. **Check identity, clocks and channels.** Inspect creation metadata, elapsed time, lap markers, sampling intervals, missing values, GPS precision/satellites and the actual ECU channels. Keep source-clock conflicts visible instead of silently changing a date.
4. **Select comparable laps and align the comparison.** Remove out/in-laps and interrupted running from pace comparisons while retaining them in the archive. Use geographic gates when GPS schemas produce incompatible distance totals. Keep degraded sessions provisional.
5. **Explain the performance difference.** Generate lap/sector tables and speed/control plots; examine linked corners, entry/minimum/exit behaviour and repeated loss regions. Use rider feedback and aligned footage to assess a proposed explanation.
6. **Write a next-session task and inspect its outcome.** Specify the corner or control sequence to reproduce, or one setting to test. Judge the following run using sector performance and consecutive comparable laps; retain failed tests and alternative explanations.

The working outputs are a session/lap table, selected comparison plots, a short driver debrief, source-quality notes and a next-test instruction. Python/NumPy/Matplotlib process the telemetry; OpenCV supports frame extraction and review; CSV/JSON and the dated report preserve the calculation inputs and outputs.

## Concrete checks that changed the analysis

- **P1 GPS source changes:** source schemas differed between sessions and produced materially different distance totals. Geographic gates supplied a shared comparison; external-GPS precision and satellite fields supported reference-lap selection.
- **P1 source-clock conflict:** some exports retained an old GPS date despite the current session metadata and upload context. Monotonic elapsed/lap timing supported interval analysis while absolute timestamps remained qualified.
- **GPR150 gear inference:** an ECU speed PID stayed at zero and no direct gear channel was available. Gear labels therefore used GPS/RPM ratio plus rider report, with their inferred status retained.
- **CBR650R throttle calibration:** normalize the observed OBD signal over its recorded endpoints. It is a PID signal, not a measurement of torque or a calibrated physical throttle-plate angle.
- **CBR650R degraded GPS:** merged laps and weak position data in S03 were retained for provisional context but excluded from precise cross-session claims.

## Video alignment and feedback timing

The archive includes a July CBR650R rear-camera review aligned to TrackAddict using the visible local-time overlay: the video began 17.0 s after the telemetry start. This supplied a time mapping for the covered laps; approximately 1 Hz GPS still limited precise apex identification.

For the September GPR150 programme, selected onboard frames and proxy files are already available. Full per-camera lap-to-picture alignment remains unfinished. The recorded next step is to anchor a visible start/finish crossing to the stored lap marker, then check the correspondence at later events before using video to attribute a control action.

The GPR150 S04-S07 runs were completed consecutively without reading the interim analysis. Their progression is a retrospective observation. The review feeds a subsequent exercise; it is not presented as evidence that each of those runs responded to advice between sessions.

## Simulator acquisition and recovery

The simulator extends this workflow with accepted result records, native best-lap binaries, continuous capture and replay recovery. The completed performance cases precede this supporting chapter.

### Source selection

| Source | Useful evidence | Important constraint |
|---|---|---|
| CM/AC/ACC session results | Accepted lap times, sectors, cuts, tyre labels and session identity | Summary timing does not contain a complete high-rate vehicle-state trace |
| Native AC `.tc` | Best-lap speed, normalized pedal inputs and gear | A completed best/last lap can differ from the latest unfinished attempt |
| Replay plus upstream `acreplay-parser` | Session timeline, car positions, controls, wheel channels and damage | Coverage depends on the replay buffer; multiplayer channels can be quantized |
| Direct CSV polling | Packet IDs, time, lap progress, pedals, steering, gear, wheel slip/load/speed, pressure/temperature and assists | Repeated packet IDs and session resets must be checked before counting unique physics samples |
| Live Telemetry | Continuous high-rate vehicle and tyre channels, setup context | Startup metadata can be stale; an empty temporary file is not a completed capture |
| Archived server lapstat | Benchmark speed versus distance | Does not supply the reference driver's control inputs |

### Recovering an event after live logging was unavailable

For the MX-5 Lime Rock race, I combined a shared complete replay with a local tail buffer, official timing and native best-lap data. The 56,969-frame reconstruction restored the lap/traffic/damage timeline. When its brake channel proved binary, the `.tc` reader supplied the continuous accepted-PB input trace. This is a concrete source-recovery workflow rather than an assumption that every recorder saved equivalent data.

The binary-reader work locates the native header, accepted lap time and sample records, then exports speed, track progress, pedals and gear to analysis tables and plots. The upstream replay parser is credited separately; my work is the source integration, timing reconciliation and analysis built around it.

### Recording incomplete and invalid attempts

An earlier MX-5 T1 investigation exposed gaps in lap-based records: the latest unfinished attempt was not the completed lap held in `.tc`, and an alternative lap export had discontinuities around the critical event. The workflow added direct CSV capture so invalid or aborted running would remain inspectable.

A current audit of the preserved direct-capture file finds **152,189 polling rows**, four session-time resets and **18.14% adjacent repeated packet IDs**. I retain packet/time continuity checks instead of presenting polling rows as an equal number of unique physics frames. The current file is an acquisition example; its rows are not assigned wholesale to the earlier failed T1 attempt.

### Preventing silent session contamination

For F4, the 78,431-frame, 30 ms replay export is matched against CM valid-lap transitions. For Silverstone, a later incorrectly labelled telemetry filename is rejected after CM identifies the actual Macau/Evo session. These checks prevent comparing different sessions under the same apparent car/track label.

### Engineering outputs

The resulting analysis stack supports:

- valid-lap and source-coverage tables;
- speed/input traces and brake-event windows;
- four-wheel loading and lockup investigations;
- traffic and damage timelines;
- repeatability and cumulative-loss accounting;
- setup snapshots and separate single-variable test records.

The public [figures and aggregate evidence](../assets/sim/README.md) contain only selected explanatory outputs. Native binaries, complete replays, raw high-rate CSVs and participant-level exports remain private.
