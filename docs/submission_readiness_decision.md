# Submission Readiness Decision

Decision: workshop-only / revise before main-conference submission.

The paper has a clean mechanism: a robot-caused visibility certificate changes the semantics of missed detections. The synthetic evidence shows a useful persistence/staleness tradeoff and the v2 corruption stress makes the calibration boundary explicit.

The paper is not main-conference-ready as a robotics systems result. It still uses 2D synthetic geometry, object IDs, no real association, no real robot calibration, and no external occluder model.

Minimum next evidence for a stronger submission:

- Real robot camera/arm self-occlusion sequences with calibrated link masks.
- Association under clutter and object re-identification after occlusion.
- External occluder labels or a fallback uncertainty model.
- Stress tests for calibration drift, segmentation errors, and robot-state latency.
