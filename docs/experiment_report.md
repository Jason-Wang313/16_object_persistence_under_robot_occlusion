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

## Final Artifact

- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf`
- Pages: 25
- Size: 382,537 bytes
- SHA256: `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`
- VLA-style boxed-link inventory: 46 annotations on pages `[(2, 40), (4, 3), (5, 3)]`; green = 40, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit: rendered pages 2, 4, and 5 after export and confirmed crisp, aligned link boxes.
