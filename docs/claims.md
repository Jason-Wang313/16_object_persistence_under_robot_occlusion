# Claims

## Supported Claims

1. If a robot perception system receives only a missed-detection event, object absence and robot self-occlusion can produce identical observation histories.
2. A robot-action visibility certificate changes the estimator's event alphabet by distinguishing clear-view absence from robot-certified unobservability.
3. In the full-scale synthetic suite, certificate-gated deletion preserves object tracks through robot self-occlusion better than short TTL policies while producing fewer stale clear-absence tracks than indiscriminate long memory.
4. The main geometry family supports the mechanism: certificate F1 0.950, keep-under-self-occlusion 0.821, stale clear-absence 0.255, and survival 1.000.
5. Calibration is a measurable precision/recall boundary: at noise 6, inflation 2, and latency 3, certificate F1 is 0.926 with precision 0.685 and recall 0.844.
6. Direct certificate corruption exposes asymmetric failures: 50% false negatives reduce keep-under-self-occlusion to 0.322, while 50% false positives raise stale clear-absence to 0.293.
7. Ablations support the action-conditioned geometry claim: random geometry falls to F1 0.582 and no robot action falls to F1 0.514 in the mixed-cause ablation family.

## Partially Supported Claims

1. The mechanism is relevant to manipulation and mobile manipulation, but the evidence remains synthetic.
2. The system can inform active re-observation policy, but no optimized controller or hardware policy is evaluated.
3. Association stress is tested as a summary-level perturbation; the paper does not solve full identity tracking under clutter.
4. Hidden motion is measured through reappearance error, but the method does not predict contact-rich object displacement.

## Unsupported Claims To Avoid

1. Do not claim state-of-the-art real-world robot perception.
2. Do not claim complete object permanence or full physical reasoning.
3. Do not claim the method solves external occluders, deformable objects, transparent objects, or contact-induced displacement.
4. Do not claim the certificate is calibration-free or robust to arbitrary visibility false positives/false negatives.
5. Do not claim long-memory baselines are always worse; in mixed external settings they can score higher F1 by tolerating stale state.

## Formal Claim Status

A proposition and proof sketch are included for non-identifiability under observation-only misses. It supports only the claim that miss streams without robot-action visibility cannot identify object absence versus robot self-occlusion.
