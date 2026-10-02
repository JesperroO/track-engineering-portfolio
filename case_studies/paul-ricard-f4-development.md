# SMP F4 / Paul Ricard: brake release, wheel loading and setup-test control

[Portfolio contents](../README.md)

**Practice on 2026-08-31 and 2026-09-01 · SMP F4 Gen 2 · Paul Ricard WTCC**

This development work combines repeated driving, replay-derived control analysis, Content Manager timing, server-reference speed traces and separate setup variants. The main problem was repeated loss of the rear axle through one S2 transition, which interrupted otherwise usable pace.

## Match the trace to the session

I sampled the replay at **30 ms intervals** and matched its valid-lap transition times against CM session `260831-235626`. Seven valid transitions in the retained export match exactly at the stored millisecond precision.

The matched practice trace supplies controls, speed, four-wheel loading and damage channels.

## Recovering a repeatable four-lap sequence

After a disrupted lap, the session produced four consecutive valid laps:

| CM lap | S1 | S2 | S3 | Lap time |
|---|---:|---:|---:|---:|
| 13 | 18.583 s | 31.703 s | 42.848 s | 93.134 s |
| 14 | 18.713 s | 30.839 s | 41.953 s | 91.505 s |
| 15 | 18.677 s | 31.046 s | 41.580 s | 91.303 s |
| 16 | 18.095 s | 31.361 s | 44.028 s | 93.484 s |

The prior session PB was 92.444 s, with sectors 18.563 / 31.298 / 42.583 s. L15 improved it by 1.141 s; S3 contributed 1.003 s, while S1 was actually 0.114 s slower.

## A faster S1 with earlier release

L28's valid S1 is **18.054 s**, 0.623 s faster than L15's 18.677 s. Rechecking the replay samples gives:

| S1 measure | L15 | L28 |
|---|---:|---:|
| First nonzero brake sample in the main braking event | 7.620 s | 7.290 s |
| Last nonzero brake sample in that event | 9.930 s | 9.300 s |
| Speed near the sector boundary | 146.8 km/h | 153.6 km/h |

![F4 S1 speed and brake input](../assets/sim/f4-s1-release.png)

Times are measured from lap start. L28 releases the brake earlier and reaches the sector boundary 6.8 km/h faster. Its full lap takes **97.227 s**, compared with L15's 91.303 s; I selected the faster S1 sequence as a practice target.

## Wheel load and the troublesome transition

L15 passes the same S2 transition with the right rear dropping to approximately **0.345 kN** while the recorded throttle is near full input. Other laps fail there. I compare that load transition with steering, throttle and replay position to examine the curb approach and the timing of drive demand.

## Setup variants and decision records

### How I turn wheel-load data into a test

![S2 rear-wheel load with synchronized throttle](../assets/sim/f4-rear-load-event.png)

At **29.610 s** on the matched 91.303 s L15, the replay reports **344.75 N right-rear load versus 605 N left-rear**, with **99.2% throttle** and zero recorded brake. The figure retains the surrounding load changes instead of presenting that sample as a whole-sector minimum.

I align wheel loads, throttle, steering and replay position to identify the unload/recontact phase. I examine drive demand during low rear load and compare curb approach and throttle-opening sequence. The next comparison tracks load recovery, repeatability and sector exit speed.

It also motivates the **rear fast-rebound 6 → 5** test below: observe the contact/load recovery and exit stability under comparable inputs. The comparison would track load recovery and exit stability at the same transition. Rear pressure **17 → 16 psi** is a separate candidate, with front pressures unchanged.

The working record separates two variants:

- A: rear fast rebound reduced from 6 to 5, intended to investigate the unload/recontact transition.
- B: rear cold pressure reduced from 17 to 16 psi, with the fronts retained at 17 psi.

The event's adjustable-setting restriction excluded the damping variant from the race setup. The pressure variant remained a candidate. A later B-configuration practice session recorded a valid **91.005 s** lap, but repeated failures at the same S2 location remained. The pressure variant retained usable pace while leaving the transition problem unresolved.

I planned a 25-minute fuel budget of approximately 21 L, using an estimated 1.0–1.1 L per clean lap.

## A second reference beyond personal PB

An archived server `lapstat` comparison contains a personal 90.814 s lap and an 86.871 s reference. Its speed-distance traces reveal a substantial deficit around 3.30-3.50 km in the final braking sequence, even though the repeated S2 failure naturally attracted more attention.

![Archived F4 server speed reference](../assets/sim/f4-server-reference.png)

I use the server speed-distance comparison to select a region, then inspect my local control trace to choose a driving change.

See [aggregate evidence and source notes](../assets/sim/README.md).
