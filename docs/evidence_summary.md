# Evidence Summary

Paper16 v3 is supported by a full-scale synthetic mechanism suite, not by hardware validation. The evidence is sufficient for a final mechanism paper under the current batch standard, while the paper explicitly avoids real-robot state-of-the-art claims.

## Source Of Truth

- Runner: `experiments/full_scale_occlusion_certificates.py`
- Output directory: `results/full_scale/`
- Progress: stage `complete`, 1,124 seed-row summaries, 0 plot failures
- Manuscript: `paper/main.tex`, importing generated tables and figures from `results/full_scale/`

## Claim-To-Evidence Map

| Claim | Evidence | Result |
| --- | --- | --- |
| Self-occlusion is not a generic miss. | Family A geometry | Certificate F1 0.950; short TTL F1 0.818. |
| Clear absence and self-occlusion need different updates. | Family A geometry | Certificate stale clear-absence 0.255; long memory stale 0.515. |
| Calibration is a boundary, not a footnote. | Family B calibration | Noise 6/inflation 2/latency 3 gives F1 0.926, precision 0.685, recall 0.844. |
| False-negative certificates delete real hidden objects. | Family C corruption | 50% FN keep-under-self-occlusion 0.322. |
| False-positive certificates preserve stale objects. | Family C corruption | 50% FP stale clear-absence 0.293; 75% FP stale 0.681. |
| External occlusion requires separate semantics. | Family D external | External-aware F1 0.357 at external rate 0.15 with low stale rates; long memory has higher F1 but higher stale. |
| Association is not solved by persistence. | Family E association | 30% swap produces certificate F1 0.920 and 413.556 ID switches. |
| Hidden motion remains a pose-prediction problem. | Family F hidden motion | Robot-contact reappearance error 0.539. |
| Strong baselines expose loss tradeoffs. | Family G baselines | Long memory F1 0.899/stale 0.488; certificate F1 0.723/stale 0.078. |
| Robot geometry is necessary. | Family H ablation | Random geometry F1 0.582; no robot action F1 0.514. |

## Final Scope

The final claim is mechanism-level: action-conditioned robot visibility changes how missed detections should update persistent object state. The paper does not claim calibrated hardware performance, solved external occlusion, solved association, or solved hidden-state dynamics.

## Final PDF

- Path: `C:/Users/wangz/Downloads/16.pdf`
- Pages: 25
- Size: 382,537 bytes
- SHA256: `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`
- VLA-style boxed-link audit: 46 annotations on pages `[(2, 40), (4, 3), (5, 3)]`; green = 40, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit: rendered pages 2, 4, and 5 after export; citation/URL and internal-reference boxes are crisp and aligned.
