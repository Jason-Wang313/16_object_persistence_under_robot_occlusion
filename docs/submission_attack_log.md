# Submission Attack Log

Checked: 2026-06-14

## Hostile Round 1: The certificate depends on calibration

Result: Incorporated.

Action: Added Family B calibration stress over certificate noise, mask inflation, and robot-state latency. The main boundary point at noise 6/inflation 2/latency 3 has F1 0.926, precision 0.685, and recall 0.844.

## Hostile Round 2: False negatives delete real objects

Result: Incorporated.

Action: Added Family C direct certificate corruption. At 50% false negatives, keep-under-self-occlusion drops to 0.322 and F1 drops to 0.856.

## Hostile Round 3: False positives recreate long-memory staleness

Result: Incorporated.

Action: Added false-positive corruption. At 50% false positives, stale clear-absence rises to 0.293; at 75% false positives, stale clear-absence rises to 0.681.

## Hostile Round 4: External occluders are a different hidden-cause class

Result: Incorporated as a boundary result.

Action: Added Family D external occluder stress. At external rate 0.15, long memory has F1 0.789 but high stale rates; external-aware certificates keep stale rates low but have F1 0.357. The manuscript frames this as evidence that external occlusion needs separate semantics.

## Hostile Round 5: Object identity and hidden motion are not solved

Result: Incorporated as limitations with experiments.

Action: Added Family E association stress and Family F hidden-motion stress. At 30% swap, certificate F1 is 0.920 but ID switches average 413.556. Under robot-contact hidden motion, reappearance error is 0.539.

## Hostile Round 6: Strong baselines might win by optimizing a different loss

Result: Incorporated.

Action: Added Family G strong baselines. In the mixed external setting, long memory reaches F1 0.899 with stale 0.488, while certificate reaches F1 0.723 with stale 0.078. The paper reports the tradeoff instead of claiming universal dominance.

## Hostile Round 7: Geometry-free persistence might be enough

Result: Rejected by ablation.

Action: Added Family H ablations. Random geometry falls to F1 0.582 and no robot action falls to F1 0.514.
