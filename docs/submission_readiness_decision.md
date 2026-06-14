# Submission Readiness Decision

Decision: final under the current full-scale mechanism-paper standard; not a hardware systems claim.

The v3 paper has a clean central mechanism, a formal non-identifiability proposition, 1,124 seed-row summaries across eight experiment families, generated figures/tables, explicit negative controls, and an artifact-to-claim audit. It is ready to stand as a synthetic mechanism paper about action-conditioned visibility semantics for persistent object state.

The paper should still be scoped carefully. It does not claim real-robot state of the art, solved external occlusion, solved association, solved detector segmentation, or solved contact-rich hidden motion. Those are named as future hardware validation requirements rather than hidden weaknesses.

## Evidence That Supports Readiness

- Main geometry family: certificate F1 0.950 versus short TTL F1 0.818.
- Staleness comparison: certificate stale clear-absence 0.255 versus long-memory stale 0.515.
- Calibration stress: noise 6/inflation 2/latency 3 gives F1 0.926 with certificate precision 0.685 and recall 0.844.
- Corruption stress: 50% false negatives reduce keep-under-self-occlusion to 0.322; 75% false positives raise stale clear-absence to 0.681.
- External-occluder family: demonstrates that robot-only certificates need separate external-cause semantics.
- Association and hidden-motion families: quantify two deployment blockers instead of implying they are solved.
- Ablation family: random geometry F1 0.582 and no robot action F1 0.514.

## Minimum Next Evidence For A Hardware Follow-Up

- Real robot camera/arm self-occlusion sequences with calibrated link masks.
- Detector and segmentation errors under robot body occlusion.
- Association under clutter and object re-identification after occlusion.
- External occluder labels or a fallback uncertainty model.
- Stress tests for calibration drift, robot-state latency, and contact-induced hidden motion.
