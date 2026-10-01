# Simulation figures and evidence provenance

These figures were regenerated on 2026-10-01 from existing local session records. They contain selected derived results; the original binaries, full-rate telemetry and participant-level records are not included.

| Public figure | Original evidence | Derivation |
|---|---|---|
| `lime-rock-performance.png` | 2026-08-05 MX-5 qualifying table and 26-interval race summary | PB-sector difference to pole; reconstructed lap timeline and loss above a 59.31 s planning baseline |
| `lime-rock-pedal-trace.png` | Native AC accepted-best-lap `.tc`, previously decoded to a selected-lap table | Speed, normalized throttle and brake input versus normalized track progress; shaded primary braking window |
| `race-consistency.png` | R5 completed-interval table, R7 reconstructed driver trace, R8 completed-lap table | Screen using all-interval median ± 3 MAD; recompute retained median/MAD and first/last three retained-lap medians |
| `f4-s1-release.png` | 2026-08-31 F4 replay-derived CSV plus CM session `260831-235626` | Match valid lap transitions; select L15/L28 S1 by CM sector duration; plot vector-speed magnitude and normalized replay brake input against elapsed lap time |
| `f4-server-reference.png` | Archived lapstat speed-distance arrays inspected during the F4 preparation session | Plot personal 90.814 s and reference 86.871 s speed traces; highlight 3.30-3.50 km for further examination |
| `silverstone-sectors.png` | CM session `260912-205309` | Select the three valid medium-tyre laps; compare recorded S1/S2/S3 |

`evidence-summary.json` contains curated aggregate tables, selected lap timings and the previously archived public server speed-distance comparison. It excludes raw pedal arrays, wheel traces, replay positions and other participant identities. The practice export inventory counts files, not valid laps. Its inspection date is 2026-10-01.

## Cross-checks

- Lime Rock: three valid qualifying entries out of nine; seven >61 s completed intervals sum to 28.50 s loss above 59.31 s. The separate all-positive-loss total is 30.48 s.
- Three-event completed/retained counts: 26/19, 12/9 and 14/11. Relative MAD values recompute to 0.559%, 0.271% and 1.045%.
- F4: seven valid lap transitions in the inspected replay export match CM recorded times. L15/L28 S1 values are 18.677/18.054 s; the complete L28 remains slower.
- Silverstone: the medium-lap selection recomputes to 133.739, 130.561 and 127.571 s. Soft-lap sectors are kept outside that valid-medium comparison.

The narrative also uses the saved setup records, dated session analyses and original local Codex discussion where a test was proposed. A proposal is labelled as such; a later observation is not turned into a causal setup claim. Upstream `acreplay-parser` 0.3.0 supplies replay decoding, while the surrounding analysis, integration and record keeping are the portfolio work.
