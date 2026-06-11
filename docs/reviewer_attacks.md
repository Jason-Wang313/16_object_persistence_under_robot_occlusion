# Reviewer Attacks

1. **This is just a tracker with a longer timeout.** Response: no; the certificate freezes deletion only when robot geometry predicts unobservability and deletes normally under clear-view misses.
2. **Semantic SLAM already stores objects persistently.** Response: maps store state, but the paper targets per-action update semantics during robot-caused invisibility.
3. **Amodal perception already reasons about occluded objects.** Response: amodal completion estimates hidden extent; this mechanism decides whether a missing detection is evidence of absence.
4. **The simulator is too simple.** Response: true for deployment claims; the paper should be pitched as a mechanism and failure-mode paper unless real-robot evidence is added.
5. **Robot self-occlusion masks are known in many systems.** Response: knowing the mask is not the same as making it the central persistence update event.
6. **Uncertainty filters can do this.** Response: only if the observation likelihood explicitly conditions on action-caused visibility; generic uncertainty is not enough.
7. **The method depends on accurate kinematics/calibration.** Response: yes; this is a limitation and a natural robustness axis.
8. **External occluders are ignored.** Response: intentionally; the contribution isolates self-occlusion, where the robot has privileged causal knowledge.
9. **Evaluation uses object IDs.** Response: the simulator isolates deletion semantics, not association; real systems would need association or object-slot matching.
10. **No real robot.** Response: paper-readiness should be workshop or revise without hardware validation.
