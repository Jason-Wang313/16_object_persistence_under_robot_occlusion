# Submission Attack Log

Checked: 2026-06-13 00:29:13 +01:00

## Hostile Round 1: The certificate depends on calibration

Result: Recoverable.

Action: Added Gaussian certificate-noise stress and direct certificate-corruption stress. Large Gaussian noise only mildly degrades the conservative certificate, but direct false-negative/false-positive corruption exposes the real boundary.

## Hostile Round 2: False negatives delete real objects

Result: Claim narrowed.

Action: Added false-negative corruption. At 50% false negatives, keep-under-self-occlusion drops from 0.920 to 0.674 and F1 drops to 0.930.

## Hostile Round 3: False positives recreate long-memory staleness

Result: Claim narrowed.

Action: Added false-positive corruption. At 50% false positives, stale clear-absence rises from 0.143 to 0.544 and F1 drops to 0.948.
