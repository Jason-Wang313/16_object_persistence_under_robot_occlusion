# Novelty Decision

## Chosen Thesis
Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.

## Why This Beat The Alternatives
- It changes which mechanism is central: robot kinematics become part of the observation alphabet.
- It breaks a specific false assumption: all missed detections are exchangeable.
- It yields a small formal claim: observations without robot-action visibility are non-identifiable between object absence and self-occlusion.
- It is empirically testable in a runnable simulator that varies self-occlusion duration and object removal.

## Rejected Directions
- Bigger perception backbone: forbidden weak move and does not change missing-evidence semantics.
- New benchmark only: useful but insufficient without a mechanism.
- Add uncertainty/verifier: unless the uncertainty is causally tied to robot geometry, it is post-hoc scoring.
- Active look-around policy: valuable but asks the robot to avoid the central challenge instead of surviving it.
- LLM/planner integration: outside the central perception mechanism and unsupported by the evidence here.

## Required Honest Scope
The current evidence is synthetic and mechanism-level. The paper can claim a clear failure mode, a formal identifiability boundary, and a controlled demonstration. It cannot claim real-robot robustness without additional experiments.
