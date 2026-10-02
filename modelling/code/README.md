# Selected CBR650R / P1 model implementation

[Worked model](../cbr650r-p1-model.md)

This is a selected subset of my actual implementation, with NumPy as its only dependency:

- `laptime/powertrain.py`: gear-to-rpm conversion, wheel-power interpolation and best-gear power ceiling.
- `laptime/cbr_ggv.py`: named scenario inputs, mass/power scaling, asymmetric drive/brake envelopes and wheel-lift limits.
- `laptime/fixed_line.py`: combined-force ellipse, closed forward/backward feasibility passes and time integration.

Run from this directory:

```sh
python run_fixed_line.py
```

The JSON supplies segment lengths and curvature for the archived 180-station candidate. The script solves **speed on this fixed path** and reports time and speed differences against the archive. [The worked model](../cbr650r-p1-model.md) describes path optimisation and photographed-board extraction.

Verification of this published subset reproduces **45.8689348527 s**, with **0.0 m/s maximum difference** from the archived speed profile and convergence in three passes. This verifies numerical reproduction on the supplied path; the physical assumptions are described in the worked model.
