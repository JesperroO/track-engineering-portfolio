# Subo case evidence

The visual page uses curated relative telemetry in `evidence.js`. It contains no absolute GNSS coordinates or Unix timestamps. Session clocks identify the five recorded sessions on 6 October 2026.

- 35 retained heart-rate profiles: complete laps after the first lap, excluding final L7/L8 yielding candidates.
- Relative HR subtracts each lap's linear time trend fitted on uniform 0.2-second time samples; spatial display step is 5 m. Session means are shown separately; combined residual profile weights the five sessions equally.
- Speed comparisons use the existing common progress axis. Cumulative time differences at 195/275/325/365/395 m are derived from same-session raw-GPS crossings of fixed geographical planes, not from diagram matching.
- Exported diagrams use selected relative coordinates from the morning reference lap. The venue board is a turn-identification photograph, not a surveyed boundary.
- SVG figures are snapshots of the default interactive views. The six-page PDF presents the default losing comparison and describes the successful counterexample alongside it.

Narrative and limitations: [中文](../../zh/subo-gpr150.md), [English](../../case_studies/subo-gpr150.md). Full telemetry, original rider messages, method revisions and measurement logs remain in the private local track-engineering archive.
