# Full-Scale Experiment Report

## Scope
- Eight experiment families: geometry coverage, certificate calibration, corruption, external occluders, association, hidden motion, stronger baselines, and ablations.
- Total seed-row summaries: 1124.
- Outputs are under `results/full_scale/`.

## Key Findings
- Main 42 degree setting: certificate F1 0.950, short-TTL F1 0.818, certificate stale clear-absence 0.255, long-memory stale clear-absence 0.515.
- Calibration stress at noise 6/inflation 2/latency 3: F1 0.926, certificate precision 0.685, recall 0.844.
- Corruption stress: 50% false positives stale clear-absence 0.293; 50% false negatives keep-under-self-occlusion 0.322.
- External-aware policy at external rate 0.15/long/labeled: F1 0.357.
- High-ambiguity association with 30% swap: certificate F1 0.920.
- Random-geometry ablation F1 0.582.

## Plot Status
- All full-scale figures generated successfully.
