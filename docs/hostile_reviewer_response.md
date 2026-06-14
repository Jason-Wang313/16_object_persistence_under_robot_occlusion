# Hostile Reviewer Response

The strongest criticism is correct: a robot-visibility certificate is only useful if it is calibrated, causal, and separated from external occlusion. The v3 paper does not hide this. It turns the criticism into the evaluation design.

The main geometry family shows the intended mechanism: certificate F1 0.950, short TTL F1 0.818, and long-memory stale clear-absence 0.515. The calibration family measures the certificate boundary directly: at noise 6, inflation 2, and latency 3, F1 is 0.926 with certificate precision 0.685 and recall 0.844.

The corruption family shows the failure modes. With 50% false negatives, keep-under-self-occlusion falls to 0.322. With 50% false positives, stale clear-absence rises to 0.293, and at 75% false positives it rises to 0.681. The external-occluder family then shows that robot-only certificates should not be used as universal object permanence.

The revised claim is therefore not that certificate-gated persistence is a solved tracker. The claim is that missed detections need action-conditioned visibility semantics, that those semantics are experimentally separable from generic memory, and that their precision/recall boundary must be reported as part of any real robot system.
