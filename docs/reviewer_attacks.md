# Reviewer Attacks

1. **This is just a tracker with a longer timeout.** Response: no; the certificate freezes deletion only when robot geometry predicts unobservability and deletes normally under clear-view misses. Family A compares certificate, short TTL, medium TTL, long memory, hazard filtering, visibility weighting, and oracle visibility.
2. **Semantic SLAM already stores objects persistently.** Response: maps store state, but the paper targets per-action update semantics during robot-caused invisibility.
3. **Amodal perception already reasons about occluded objects.** Response: amodal completion estimates hidden extent; this mechanism decides whether a missing detection is evidence of absence. The strong-baseline family includes an amodal proxy and still exposes stale-state tradeoffs.
4. **The simulator is synthetic.** Response: correct. The final claim is a mechanism claim supported by a broad synthetic suite, not a calibrated hardware systems claim.
5. **Robot self-occlusion masks are known in many systems.** Response: knowing the mask is not the same as making it the central persistence update event or reporting certificate precision/recall as a deletion-semantics boundary.
6. **Uncertainty filters can do this.** Response: only if the observation likelihood explicitly conditions on action-caused visibility. Family G includes hazard-style baselines and shows the tradeoff.
7. **The method depends on accurate kinematics/calibration.** Response: yes; Family B reports the precision/recall boundary. At noise 6/inflation 2/latency 3, F1 is 0.926 with precision 0.685 and recall 0.844.
8. **False certificates break the method.** Response: yes, and Family C quantifies both sides. 50% false negatives reduce keep-under-self-occlusion to 0.322; 75% false positives raise stale clear-absence to 0.681.
9. **External occluders are ignored.** Response: they are now an explicit boundary family. External occluders require separate semantics; long memory can score higher F1 by preserving stale state.
10. **Evaluation uses object IDs.** Response: association is a named limitation. Family E adds swap stress and reports 413.556 ID switches at 30% swap.
11. **Hidden objects may move.** Response: Family F reports hidden-motion and robot-contact reappearance error; the certificate says a miss is uninformative about absence, not that the old pose is perfect.
12. **No real robot.** Response: correct. Hardware validation is the next evidence layer, not a claim made by this paper.
