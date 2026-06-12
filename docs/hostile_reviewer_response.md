# Hostile Reviewer Response

The strongest criticism is correct: the method is only useful if the robot-visibility certificate is conservative and calibrated. The v2 paper now measures both sides of that failure.

At 42 degree self-occlusion, the clean certificate corruption stress has F1 0.975, keep-under-self-occlusion 0.920, and stale clear-absence 0.143. With 50% false negatives, keep-under-self-occlusion falls to 0.674. With 50% false positives, stale clear-absence rises to 0.544.

The revised claim is therefore not that certificate-gated persistence is a solved tracker. The claim is that missed detections need action-conditioned visibility semantics, and that the certificate must be validated as part of the perception system.
