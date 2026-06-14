# Novelty Decision

## Chosen Thesis

Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.

## Why This Beat The Alternatives

- It changes the central mechanism: robot kinematics become part of the observation alphabet.
- It breaks a specific false assumption: all missed detections are exchangeable.
- It yields a formal claim: observations without robot-action visibility are non-identifiable between object absence and robot self-occlusion.
- It is empirically testable through controlled variations of geometry, calibration, corruption, external occlusion, association, hidden motion, baselines, and ablations.
- It supports active re-observation policy because the tracker exposes why the robot does not know, rather than only smoothing a presence score.

## Rejected Directions

- Bigger perception backbone: does not change missing-evidence semantics.
- New benchmark only: useful but insufficient without a mechanism.
- Generic uncertainty/verifier: insufficient unless uncertainty is causally tied to robot geometry and action timing.
- Pure active look-around policy: valuable, but it can avoid rather than explain the state-update failure during unavoidable robot-caused occlusion.
- LLM/planner integration: outside the central perception mechanism and unsupported by the evidence here.

## Required Honest Scope

The current evidence is synthetic and mechanism-level. The paper can claim a failure mode, a formal identifiability boundary, a broad controlled demonstration, and a policy interface for active re-observation. It cannot claim real-robot robustness without hardware experiments.
