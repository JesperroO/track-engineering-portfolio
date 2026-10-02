"""Recompute the published P1 fixed-line candidate with the selected QSS code."""
from pathlib import Path
import json
import numpy as np
from laptime.cbr_ggv import build_cbr_ggv, initial_p1_scenarios
from laptime.fixed_line import FixedPath, solve_closed_fixed_line

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/p1-fixed-line.json').read_text())
scenario = next(s for s in initial_p1_scenarios() if s.name == data['scenario'])
envelope = build_cbr_ggv(ROOT / 'data/cbr650r-inputs.json', scenario).envelope
path = FixedPath(np.array(data['element_length_m']), np.array(data['curvature_1_per_m']))
result = solve_closed_fixed_line(path, envelope, 208.0 + scenario.rider_mass_kg)
archived = np.array(data['archived_speed_mps'])
print(json.dumps({
    'scenario': scenario.name,
    'stations': len(result.speed_mps),
    'current_fixed_line_time_s': float(result.time_s.sum()),
    'archived_time_s': data['archived_lap_time_s'],
    'max_speed_difference_mps': float(np.max(np.abs(result.speed_mps - archived))),
    'iterations': result.iterations,
}, indent=2))
