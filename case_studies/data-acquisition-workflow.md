# Real-track acquisition and trackside review

[Portfolio contents](../README.md)

I build and operate a self-funded motorcycle data workflow, covering riding, telemetry capture, onboard video and analysis. The aim is to obtain useful engineering evidence within a limited equipment budget, using accessible hardware and DIY integration.

![Circuit Tools review on the pit-room laptop](../assets/workflow/p1-trackside-circuit-tools.png)

*Circuit Tools on the pit-room laptop: recorded laps, onboard footage and telemetry available for review at the circuit.*

## The acquisition stack

**RaceChrono Pro** is the logging hub. It connects to GPS, IMU and a chest-strap heart-rate sensor. Vehicle channels arrive through the **vLinker MC+ OBD-II interface over BLE**. A **DJI Osmo Action 5 Pro** records the helmet viewpoint, alongside other onboard camera footage where available.

```mermaid
flowchart LR
    CAN[Vehicle CAN bus] --> OBD[OBD-II connector]
    OBD --> MC[vLinker MC+]
    MC -->|BLE| RC[RaceChrono Pro]
    GPS[GPS] --> RC
    IMU[IMU] --> RC
    HR[Chest-strap heart rate] --> RC
    RC --> EXP[Session exports / VBO]
    EXP --> CT[Circuit Tools 3 / pit-room laptop]
    HELMET[Action 5 Pro / helmet view] --> VIDEO[Video archive / later multi-camera alignment]
    VIDEO --> CT
```

The vehicle side supplies OBD channels such as RPM and throttle. GPS supplies position, speed and lap context; motion and heart-rate channels add information about my riding transitions and heart-rate response. Their individual sampling rates and source definitions remain attached to the exported data.

## Between sessions

During a review break, I use **Circuit Tools 3 on the pit-room laptop** to compare laps, inspect speed and control traces, and revisit the available onboard footage. I combine those observations with riding feedback to choose the focus for the next session: a braking reference, opening sequence, linked-corner line or other specific driving question.

The working loop is **ride → capture → review → choose the next-session focus → ride again**. Review timing depends on the session schedule. For the P1 S04–S07 sequence, the consecutive runs were analysed retrospectively; the general trackside workflow also includes breaks used for review and planning.

## Video and later analysis

Helmet footage shows my view of the approach and visual reference. Other viewpoints provide complementary context. After the track day, I archive the original telemetry and camera files, align the available viewpoints and telemetry clocks, and select the relevant passage for a lap or corner comparison.

The published P1 T2 clip is a completed example of that process: one continuous S04 passage aligned through the VBO video clock, with speed, RPM, throttle, calculated lean and longitudinal G displayed alongside the original sound. Other camera files are aligned separately as each analysis requires them.

## Engineering within the budget

I used RaceChrono, BLE OBD, an action camera and a laptop to keep equipment costs within my budget. I integrated their exports and clocks into lap comparisons, mapped lines and synchronized video for trackside and post-session review.

This approach supports the portfolio's real-track outputs: lap comparison, control-event analysis, mapped lines, aligned video and a concrete next-session plan.

## Archive processing

I retain original RaceChrono exports, available VBO records and camera files by session. Python/NumPy/Matplotlib support the detailed telemetry comparisons; video proxies and aligned excerpts support visual review. Geographic gates provide a common comparison where GPS schemas yield different distance totals. Source-quality checks and channel definitions accompany the selected results.

The [aprilia GPR150 P1 case](p1-gpr150-telemetry.md) and [CBR650R case](hualong-cbr650r.md) apply this workflow to different acquisition conditions.

## Concrete checks that changed the analysis

- **P1 GPS source changes:** source schemas differed between sessions and produced materially different distance totals. Geographic gates supplied a shared comparison; external-GPS precision and satellite fields supported reference-lap selection.
- **P1 source-clock conflict:** some exports retained an old GPS date despite the current session metadata and upload context. Monotonic elapsed/lap timing supported interval analysis while absolute timestamps remained qualified.
- **aprilia GPR150 gear inference:** an ECU speed PID stayed at zero and no direct gear channel was available. I used GPS/RPM ratios and my recorded gear choices, retaining inferred labels where applicable.
- **CBR650R throttle normalization:** scale the recorded OBD endpoints to 0–100% for comparing throttle opening and release across laps.
- **CBR650R degraded GPS:** merged laps and weak position data in S03 were retained for provisional context but excluded from precise cross-session claims.

## Simulator acquisition and recovery

For simulator sessions, I combine accepted lap records, native best-lap files, continuous telemetry and replays.

### Source selection

| Source | Useful evidence | Important constraint |
|---|---|---|
| CM/AC/ACC session results | Accepted lap times, sectors, cuts, tyre labels and session identity | Use with telemetry or replay for vehicle-state analysis |
| Native AC `.tc` | Best-lap speed, normalized pedal inputs and gear | A completed best/last lap can differ from the latest unfinished attempt |
| Replay plus upstream `acreplay-parser` | Session timeline, car positions, controls, wheel channels and damage | Coverage depends on the replay buffer; multiplayer channels can be quantized |
| Direct CSV polling | Packet IDs, time, lap progress, pedals, steering, gear, wheel slip/load/speed, pressure/temperature and assists | Repeated packet IDs and session resets must be checked before counting unique physics samples |
| Live Telemetry | Continuous high-rate vehicle and tyre channels, setup context | Verify car/track metadata and capture coverage |
| Archived server lapstat | Benchmark speed versus distance | Speed-distance benchmark for selecting comparison regions |

### Recovering an event after live logging was unavailable

For the MX-5 Lime Rock race, I combined a shared complete replay with a local tail buffer, official timing and native best-lap data. The 56,969-frame reconstruction restored the lap/traffic/damage timeline. When its brake channel proved binary, the `.tc` reader supplied the continuous accepted-PB input trace.

The binary-reader work locates the native header, accepted lap time and sample records, then exports speed, track progress, pedals and gear to analysis tables and plots. The upstream replay parser is credited separately; my work is the source integration, timing reconciliation and analysis built around it.

### Recording incomplete and invalid attempts

An MX-5 T1 investigation needed an unfinished attempt that fell outside the completed-lap `.tc` record. The alternative export had gaps around the event. I added continuous CSV capture to retain invalid and aborted running for review.

The preserved direct-capture file contains **152,189 polling rows**, four session-time resets and **18.14% adjacent repeated packet IDs**. I use packet and time checks to select continuous windows for analysis.

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

[Figure sources and aggregate results](../assets/sim/README.md).
