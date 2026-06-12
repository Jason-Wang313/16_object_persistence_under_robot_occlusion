# Claims

## Supported Claims
1. If a robot perception system receives only a missed detection event, object absence and robot self-occlusion can produce identical observation histories.
2. A robot-action visibility certificate changes the estimator's event alphabet by distinguishing clear-view absence from robot-certified unobservability.
3. In the provided synthetic self-occlusion simulator, certificate-gated deletion preserves object tracks through long robot occlusions better than short missed-detection TTLs while producing fewer stale tracks than indiscriminate long memory.
4. V2 corruption stress supports the calibration boundary: 50% certificate false negatives reduce keep-under-self-occlusion from 0.920 to 0.674, and 50% false positives raise stale clear-absence from 0.143 to 0.544.

## Partially Supported Claims
1. The mechanism is likely relevant to manipulation and mobile manipulation, but this run only tests a 2D abstraction.
2. The hostile literature sweep suggests this exact update semantics is under-emphasized, but the sweep is metadata/abstract based rather than full-PDF reading of all 1000 papers.

## Unsupported Claims To Avoid
1. Do not claim state-of-the-art real-world robot perception.
2. Do not claim complete object permanence or full physical reasoning.
3. Do not claim the method solves external occluders, deformable objects, transparent objects, or contact-induced displacement.
4. Do not claim the certificate is calibration-free or robust to arbitrary visibility false positives/false negatives.

## Formal Claim Status
A proposition and proof sketch are included for non-identifiability under observation-only misses. It is a simple impossibility statement, not a broad theorem about all tracking systems.
