# Novelty Boundary Map

## What Is Not Novel Enough

- Generic tracking-by-detection with a longer missed-detection timeout.
- A larger object detector, pose net, segmentation model, or object-centric world model.
- A benchmark that merely contains occlusions without changing the estimator.
- A generic uncertainty head or verifier that scores tracks after the fact.
- Active perception that moves the camera to look again but does not preserve state while the robot itself hides the object.
- A robot mask used only for pixel filtering without changing the object-state update semantics.

## Narrow Novelty Boundary

The defendable boundary is not "robots need object permanence." The boundary is: robot self-occlusion is an action-caused intervention on observability, so a persistent object-state estimator should update on a different event alphabet: detected, absent-in-clear-view, robot-certified-unobservable, externally occluded, and ambiguous. That changes the central mechanism from missed-frame patience to kinematic visibility certification and cause-labeled evidence.

## Closest Hostile Families

- Multi-object tracking: already handles missed detections, but usually with fixed patience, learned re-identification, or appearance association rather than robot-action visibility causes.
- Semantic/object SLAM: already stores objects persistently, but often treats object absence as map maintenance rather than per-action observability.
- Amodal perception: already reasons about hidden parts, but predicts shape/extent rather than whether a missing detection is evidence of absence.
- Active perception: already moves to reduce occlusion, but the paper's claim concerns preserving state and exposing uncertainty while robot-caused occlusion is happening.
- Manipulation pose tracking: already handles partial visibility, but the core success criterion is pose estimation, not deletion semantics under self-occlusion.

## Positive Novelty Boundary

A contribution is genuine if it makes robot body geometry and action timing the variable that gates persistence updates, proves why observations alone cannot distinguish absence from self-occlusion, demonstrates the tradeoff against short TTL and long-memory baselines, and reports calibration, external-occluder, association, hidden-motion, and ablation boundaries.
