# MX-5 / Lime Rock: qualifying, race execution and pedal analysis

[Portfolio contents](../README.md)

**2026-08-05 · Assetto Corsa · HiPole RCC S31 R5 · Mazda MX-5 Cup · Lime Rock Park, no chicane**

I drove the race and analysed the session afterward. The official finish was P5, with game-side evidence showing P16 at the start and 11 positions gained. The accepted race PB was **57.784 s**. I examined invalid qualifying attempts, race pace and time lost on slow laps.

## Recovering the usable dataset

High-rate live logging was disabled before this race because of observed CPU spikes. The local replay buffer retained only the tail, so I obtained a shared complete replay and used upstream `acreplay-parser` 0.3.0 to reconstruct the full race timeline at 30 ms intervals. I used the other cars' tracks when examining traffic and comparing race pace.

I joined that reconstruction with CM/AC qualifying results, official result snapshots and the native AC `.tc` best-lap file. The result snapshot gives accepted times, the replay supplies the race timeline, and `.tc` preserves continuous normalized brake input for the accepted best lap.

## Qualifying: usable laps before more speed

My qualifying record contains nine lap entries, including the first/out-lap entry: three are valid and six invalid. After excluding the first entry, **3/8 flying attempts were valid**. My qualifying PB was 58.809 s, 1.856 s behind pole.

| Sector | My PB | Pole PB | Gap |
|---|---:|---:|---:|
| S1 | 27.228 s | 26.105 s | +1.123 s |
| S2 | 18.782 s | 18.351 s | +0.431 s |
| S3 | 12.799 s | 12.497 s | +0.302 s |

S1 explains **60.5%** of the qualifying gap. Combining my best valid sectors gives 58.613 s, a 0.196 s theoretical gain. I prioritised more valid attempts and opening-sector practice.

![Qualifying gap and race lap timeline](../assets/sim/lime-rock-performance.png)

## Race: peak pace, ordinary pace and loss budget

The accepted 57.784 s race PB is 1.025 s faster than qualifying. Replay reconstruction gives a best completed interval of 57.840 s; the two sources are retained separately.

A median/MAD screen retains 19 representative intervals out of 26 reconstructed completed intervals, with median 59.070 s and MAD 0.330 s. Separately, the original planning analysis used a 59.31 s baseline to measure slow-lap losses:

- Seven intervals above 61 s accumulated **28.50 s** above that baseline.
- All positive deviations from the baseline summed to **30.48 s**.

I prioritised consistency after calculating the slow-lap losses. The replay placed repeated losses to linked corners and exits, while checking nearby-car positions before attributing a slow lap to traffic.

## Native best-lap braking trace

I parsed the native best-lap record to recover the 57.784 s lap's speed, throttle, brake input and gear trace. The principal braking event spans approximately **7.718%-10.015%** track progress, reaches full normalized brake input and reduces speed from about **189.3 to 134.0 km/h**. A later light application is about 3.84% input.

![Native best-lap pedal trace](../assets/sim/lime-rock-pedal-trace.png)

The shared replay records brake input as 0/255. I used it for brake-on timing and recovered the continuous release shape from the native best-lap file.

## Follow-up work

The review produced specific targets: increase valid flying laps in the ten-minute qualifying window, concentrate practice on S1, and reduce the recurring large-loss laps.

Timing sources: the official result lists 25 laps; AC/replay supplies 26 crossing intervals. Qualifying sectors come from the result table, and the continuous pedal trace comes from the accepted race PB.

See [aggregate evidence and source notes](../assets/sim/README.md).
