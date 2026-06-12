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

## V2 Certificate-Noise Stress

The hardening stress reruns the certificate policy at 42 degree self-occlusion while increasing calibration noise in the certificate geometry.

| Certificate noise | F1 | Keep under self-occ. | Stale absent | Survival |
| ---: | ---: | ---: | ---: | ---: |
| 0.00 | 0.973 | 0.909 | 0.144 | 1.000 |
| 1.25 | 0.974 | 0.918 | 0.160 | 1.000 |
| 3.00 | 0.974 | 0.915 | 0.142 | 1.000 |
| 6.00 | 0.973 | 0.917 | 0.158 | 1.000 |
| 10.00 | 0.968 | 0.902 | 0.166 | 0.998 |
| 16.00 | 0.964 | 0.879 | 0.189 | 0.997 |

Interpretation: the certificate advantage depends on calibrated robot geometry. Large certificate noise lowers object-state F1 and occlusion survival, so the method should be framed as a visibility-semantics mechanism, not as a calibration-free tracker.

## V2 Certificate-Corruption Stress

This stress directly flips the certificate event at 42 degree self-occlusion. False negatives make real self-occlusions count as clear misses; false positives make clear misses look robot-occluded.

| Scenario | F1 | Keep under self-occ. | Stale absent | Survival |
| --- | ---: | ---: | ---: | ---: |
| clean | 0.975 | 0.920 | 0.143 | 1.000 |
| false_negative_10pct | 0.973 | 0.910 | 0.144 | 1.000 |
| false_negative_25pct | 0.970 | 0.886 | 0.122 | 0.999 |
| false_negative_50pct | 0.930 | 0.674 | 0.084 | 0.983 |
| false_positive_10pct | 0.970 | 0.905 | 0.174 | 1.000 |
| false_positive_25pct | 0.966 | 0.914 | 0.238 | 1.000 |
| false_positive_50pct | 0.948 | 0.910 | 0.544 | 1.000 |

Interpretation: false-negative certificates destroy the persistence benefit, while false positives increase stale-object retention. The method therefore depends on conservative but not overbroad robot-visibility certificates.
