# Experiment Summary

The simulator evaluates three deletion policies under robot self-occlusion:

- `ttl_short`: delete after three consecutive misses.
- `long_memory`: keep tracks through long gaps regardless of visibility cause.
- `certificate`: delete after three clear-view misses, but freeze the deletion counter when robot kinematics certify self-occlusion.

## Aggregate Results

| Occlusion width | Policy | F1 | Keep under self-occ. | Stale absent | Clear-visible missing | Survival |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 18.0 | certificate | 0.990 | 0.958 | 0.085 | 0.000 | 1.000 |
| 18.0 | long_memory | 0.962 | 0.959 | 0.462 | 0.000 | 1.000 |
| 18.0 | ttl_short | 0.938 | 0.363 | 0.042 | 0.001 | 0.961 |
| 30.0 | certificate | 0.984 | 0.940 | 0.098 | 0.000 | 1.000 |
| 30.0 | long_memory | 0.961 | 0.929 | 0.450 | 0.000 | 0.998 |
| 30.0 | ttl_short | 0.878 | 0.213 | 0.036 | 0.001 | 0.958 |
| 42.0 | certificate | 0.973 | 0.908 | 0.149 | 0.000 | 1.000 |
| 42.0 | long_memory | 0.951 | 0.882 | 0.423 | 0.001 | 0.992 |
| 42.0 | ttl_short | 0.817 | 0.150 | 0.034 | 0.002 | 0.958 |

## Interpretation

Short TTL has low stale-object rates but loses tracks during long robot self-occlusion. Long memory preserves objects under occlusion but also preserves removed objects in clear view. The certificate policy targets the missing cause: it preserves only when robot geometry predicts unobservability, giving a better persistence/staleness tradeoff in this controlled setting.
