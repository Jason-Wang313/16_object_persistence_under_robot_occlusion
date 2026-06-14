# Experiment Summary

The v3 suite evaluates whether action-conditioned robot self-occlusion certificates improve persistent object-state updates beyond generic missed-detection patience. It contains eight families and 1,124 seed-row summaries.

## Families

| Family | Rows | Purpose |
| --- | ---: | --- |
| A geometry | 504 | Self-occlusion width, duration, and geometry coverage. |
| B calibration | 180 | Noise, inflation, and robot-state latency. |
| C corruption | 96 | Direct false-negative and false-positive certificates. |
| D external | 72 | External occluders and mixed-cause misses. |
| E association | 72 | Identity swaps and re-identification stress. |
| F hidden motion | 72 | Static, drift, robot-contact, and external hidden motion. |
| G baselines | 64 | Stronger alternatives including hazard and amodal proxy policies. |
| H ablation | 64 | Negative controls for missing, random, underbroad, and overbroad geometry. |

## Main Geometry Results

| Policy | F1 | Keep self-occ. | Stale absent | Survival |
| --- | ---: | ---: | ---: | ---: |
| oracle_visibility | 0.963 | 0.821 | 0.070 | 1.000 |
| visibility_weighted | 0.950 | 0.814 | 0.223 | 0.982 |
| certificate | 0.950 | 0.821 | 0.255 | 1.000 |
| long_memory | 0.916 | 0.739 | 0.515 | 0.986 |
| hazard_filter | 0.860 | 0.332 | 0.135 | 0.936 |
| ttl_medium | 0.854 | 0.297 | 0.118 | 0.936 |
| ttl_short | 0.818 | 0.114 | 0.041 | 0.936 |

Interpretation: short TTL avoids stale state but deletes present objects during self-occlusion. Long memory preserves more objects but produces high stale clear-absence. The certificate targets the cause of the miss and improves the persistence/staleness tradeoff in the self-occlusion mechanism family.

## Calibration Boundary

At noise 6, inflation 2, and latency 3, the certificate policy reaches F1 0.926 with certificate precision 0.685, recall 0.844, and stale clear-absence 0.196. At noise 16 and inflation 2, F1 falls to 0.885. The method must be framed as calibration-dependent.

## Corruption Boundary

| FN | FP | F1 | Keep | Stale |
| ---: | ---: | ---: | ---: | ---: |
| 0.000 | 0.000 | 0.960 | 0.865 | 0.176 |
| 0.500 | 0.000 | 0.856 | 0.322 | 0.072 |
| 0.000 | 0.500 | 0.960 | 0.921 | 0.293 |
| 0.000 | 0.750 | 0.920 | 0.883 | 0.681 |

Interpretation: false negatives destroy the persistence benefit; false positives recreate stale memory. Certificate precision and recall must be reported separately.

## Boundary Results

- External occluders need separate semantics: at external rate 0.15, long memory reaches F1 0.789 but with external stale 0.176 and clear stale 0.167; the external-aware certificate reaches F1 0.357 with much lower stale rates.
- Association remains a blocker: at 30% swap, certificate F1 is 0.920 but ID switches average 413.556.
- Hidden motion is not solved by persistence: robot-contact reappearance error is 0.539 even though certificate F1 is 0.957.
- Strong baselines optimize different losses: in a mixed external setting, long memory reaches F1 0.899 with stale 0.488, while certificate reaches F1 0.723 with stale 0.078.
- Random or missing robot geometry is insufficient: random geometry F1 is 0.582 and no robot action F1 is 0.514.

## Generated Artifacts

Source-of-truth outputs are under `results/full_scale/`: family seed CSVs, family summary CSVs, generated tables, generated figures, `metadata.json`, and `progress.json`.
