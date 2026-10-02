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

The accompanying JSON provides segment lengths and curvature of the archived 180-station candidate; it contains no raw GNSS positions. The script reports the current recomputation alongside archived timing and speed differences. It recomputes **speed on an existing path**; the path optimiser and photographed-board extraction are described in the worked model, rather than claimed to be reproduced by this subset.

Verification of this published subset reproduces **45.8689348527 s**, with **0.0 m/s maximum difference** from the archived speed profile and convergence in three passes. This verifies numerical reproduction on the supplied path; the physical assumptions are described in the worked model.
