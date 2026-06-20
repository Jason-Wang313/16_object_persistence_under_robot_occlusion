# Paper 16 Full-Scale Execution Plan

Paper: Occlusion Certificates for Persistent Object State Under Robot Self-Occlusion
Repository: `16_object_persistence_under_robot_occlusion`
Date: 2026-06-14

## Current Claim

Persistent object state under robot self-occlusion should be updated by action-conditioned robot visibility certificates rather than generic missed-detection patience. A missed detection under robot-certified unobservability should not consume the same deletion budget as a clear-view miss.

## Current State

- Current canonical PDF is 6 pages and stale under the current 25-page standard.
- Existing evidence is a 2D self-occlusion simulator with 1,080 episode rows.
- Existing main result at 42 degree self-occlusion: certificate policy F1 0.973 versus short-TTL F1 0.817; stale clear-absence 0.149 versus long-memory 0.423.
- Existing v2 stress: clean certificate F1 0.975, keep-under-self-occlusion 0.920, stale clear-absence 0.143.
- Existing v2 corruption boundary: 50% certificate false negatives reduce keep-under-self-occlusion to 0.674 and F1 to 0.930; 50% false positives raise stale clear-absence to 0.544 and lower F1 to 0.948.
- Existing readiness decision is workshop-only because there is no calibrated robot geometry, real association, external-occluder handling, moving-object stress, robot-state latency, or real detector failure model.

## Reviewer Attacks To Resolve

1. This is just missed-detection TTL with a hand-coded exception.
2. The simulator is 2D and too clean.
3. Certificate calibration, robot-state latency, and link-mask errors are not studied enough.
4. False positives can preserve stale objects; false negatives can delete real hidden objects.
5. External occluders are not robot self-occlusion and can break the semantics.
6. Object association and re-identification are assumed solved.
7. Objects can move or be displaced while hidden.
8. Long memory, probabilistic filters, map memory, amodal perception, and learned persistence baselines are stronger than the current baselines.
9. The certificate needs conservative geometry but not overbroad geometry; that tradeoff is not fully mapped.
10. Six pages do not provide enough formalization, artifact detail, limitations, and deployment guidance.

## Experimental Expansion

Create a RAM-light v3 runner under `experiments/full_scale_occlusion_certificates.py`. Keep `scripts/run_self_occlusion_experiment.py` as the v2 baseline. Store v3 outputs under `results/full_scale/`. Run families sequentially and update `results/full_scale/progress.json` after each family.

### Family A: Occlusion Geometry Coverage

Purpose: replace the three-width 2D setting with a broader grid over self-occlusion width, arm speed, object count, horizon, and detection quality.

Settings:
- Self-occlusion width: 12, 18, 30, 42, 60 degrees.
- Arm speed: 0.5, 1.0, 1.5.
- Object count: 6, 14, 28.
- Detection probability: 0.88, 0.94, 0.98.
- Removal probability: 0.10, 0.32, 0.55.
- Seeds: enough replicated summaries for stable rates while storing only aggregates.

Baselines:
- Short TTL.
- Medium TTL.
- Long memory.
- Certificate-gated deletion.
- Probabilistic hazard filter.
- Visibility-weighted TTL.
- Oracle visibility.

Metrics:
- F1, precision, recall, keep-under-self-occlusion, stale clear-absence, clear-visible missing, occlusion survival, deletion events, and stale duration.

### Family B: Certificate Calibration Surface

Purpose: map the exact boundary between useful conservative certificates and stale-preserving overbroad certificates.

Settings:
- Geometry noise: 0, 1, 3, 6, 10, 16 degrees.
- Inflation margin: -4, 0, 2, 6, 12 degrees.
- Robot-state latency: 0, 1, 3, 6, 10 frames.
- Link-mask shrink/expand bias.

Metrics:
- Certificate precision/recall against true self-occlusion, track F1, self-occlusion keep rate, stale clear-absence, false clear-miss deletion, and false robot-occlusion preservation.

### Family C: Direct Certificate Corruption

Purpose: deepen v2 false-positive/false-negative corruption into asymmetric and bursty errors.

Settings:
- False negative rate: 0, 0.10, 0.25, 0.50, 0.75.
- False positive rate: 0, 0.10, 0.25, 0.50, 0.75.
- Error mode: independent, bursty, object-specific, angle-specific.

Metrics:
- F1, keep-under-self-occlusion, stale clear-absence, survival, deletion events, and failure attribution.

### Family D: External Occluders And Mixed Causes

Purpose: separate robot self-occlusion from external occlusion and actual removal.

Settings:
- External occluder rate: 0, 0.05, 0.15, 0.30.
- External occluder duration: short, medium, long.
- External occluder labeled or unlabeled.
- Robot self-occlusion overlapping external occlusion.

Metrics:
- Correct preservation under robot occlusion, stale preservation under external/clear absence, uncertainty fallback usage, and false self-occlusion attribution.

### Family E: Association And Re-Identification Stress

Purpose: stop assuming perfect object identities.

Settings:
- Association swap probability.
- Appearance ambiguity.
- Reappearance localization noise.
- Multiple nearby objects.

Baselines:
- ID oracle.
- Nearest-neighbor association.
- Appearance-assisted association.
- Certificate plus association gate.

Metrics:
- IDF1-like identity persistence, object-state F1, switch count, stale identity retention, and recovery after occlusion.

### Family F: Hidden Motion And Contact Displacement

Purpose: test objects that move while hidden.

Settings:
- Static hidden object.
- Passive object drift.
- Robot-contact displacement during occlusion.
- Human/external displacement.
- Motion model correct versus wrong.

Metrics:
- Presence F1, position error after reappearance, stale state after displacement, deletion/keep accuracy, and prediction uncertainty.

### Family G: Stronger Persistence Baselines

Purpose: compare against stronger alternatives than short TTL and long memory.

Baselines:
- Bayesian hazard filter.
- Kalman-style missed-observation filter.
- Visibility-weighted survival filter.
- Amodal-memory proxy.
- Learned persistence proxy from episode features.
- Certificate plus hazard fallback.

Metrics:
- F1, calibration, stale clear-absence, occlusion keep, survival, and compute/runtime.

### Family H: Ablations And Negative Controls

Purpose: isolate the certificate semantics.

Ablations:
- No robot action.
- Robot action but no geometry.
- Geometry with random arm state.
- Certificate without clear-view deletion.
- Overbroad certificate.
- Underbroad certificate.
- External occluders treated as robot occlusion.
- Oracle visibility certificate.

Metrics:
- Claim-specific deltas, false preservation, false deletion, stale duration, and survival.

## Figures And Tables

Required figures:
- Main geometry-coverage tradeoff.
- Calibration noise/inflation heatmap.
- Corruption false-positive/false-negative surface.
- External occluder mixed-cause comparison.
- Association stress curve.
- Hidden-motion/reappearance error curve.
- Strong baseline comparison.
- Ablation waterfall.

Required tables:
- Main method comparison.
- Calibration surface table.
- Corruption table.
- External occluder table.
- Association table.
- Hidden motion table.
- Strong baseline table.
- Ablation table.
- Runtime/RAM-light table.
- Claim-to-evidence table.

## Manuscript Expansion

Target structure:
- Abstract with v3 full-scale numbers and honest boundary.
- Introduction framing missed detections as semantically different events under robot action.
- Related work boundary against tracking, SLAM, object memory, amodal perception, pose tracking, and robot occlusion reasoning.
- Formal definitions: latent object state, clear-view miss, robot-certified unobservability, external occlusion, deletion budget, stale track, and false certificate.
- Method: certificate-gated deletion, visibility-weighted TTL, hazard fallback, association gate, and oracle comparison.
- Theory: observation-only non-identifiability, certificate soundness/completeness boundary, false-positive/false-negative effects, mixed-cause ambiguity.
- Experiments across Families A-H.
- Failure analysis: overbroad certificates, underbroad certificates, latency, external occluders, association swaps, hidden motion, stale duration.
- Limitations: synthetic evidence, no real camera/arm calibration, no detector segmentation, no real association, no real external occluder labels, no contact-rich object displacement.
- Appendices: proof details, parameter grids, artifact schema, baseline fairness, deployment protocol, calibration checklist, reviewer self-attacks, and final audit.

Page strategy:
- Minimum internal threshold is 25 pages.
- Length must come from real content: richer experiments, generated tables/figures, proofs, stronger baselines, diagnostics, negative controls, limitations, and reproducibility details.

## RAM-Light Execution Strategy

- Use compact Python simulation with per-episode aggregate counters.
- Store episode summaries and seed summaries, not full frame/object trajectories.
- Run families sequentially and write progress JSON.
- Use CSV, JSON, and compact Matplotlib figures.
- Keep object counts and horizons moderate but sweep many mechanisms.
- Avoid multiprocessing and large in-memory frame archives.

## Documentation Updates

Update after the full-scale pass:
- `README.md`
- `child_status.md`
- `docs/claims.md`
- `docs/evidence_summary.md` if created, otherwise `docs/experiment_summary.md`
- `docs/experiment_rigor_checklist.md`
- `docs/reproducibility_checklist.md`
- `docs/reviewer_attacks.md`
- `docs/hostile_reviewer_response.md`
- `docs/submission_attack_log.md`
- `docs/submission_version_log.md`
- `docs/final_audit.md`
- `docs/submission_readiness_decision.md`
- `docs/novelty_decision.md`
- `docs/novelty_boundary_map.md`

## Acceptance Checklist

Paper 16 is not final until all are true:
- Full-scale runner completes and writes `results/full_scale/progress.json` with stage `complete`.
- Edited Python files pass `python -m py_compile`.
- Figures and tables are regenerated from v3 summaries.
- Manuscript compiles with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Final PDF has at least 25 pages.
- Claims match generated CSVs/tables.
- Limitations explicitly include synthetic evidence, no real robot calibration, no real detector segmentation, no real association, no real external occluder labels, and no contact-rich hidden displacement validation.
- Canonical PDF is copied to `C:/Users/wangz/Downloads/16.pdf` only after final verification.
- No new Desktop PDF copy is created.
- Local `paper/main.pdf` is removed after final copy.
- Commit is pushed.
- Worktree is clean and `HEAD` matches upstream before moving to Paper 17.

## VLA-Style Link Hardening Addendum

Date: 2026-06-20

After the v3 export, the PDF link presentation was hardened to match the visible
VLA-v4 role model without changing manuscript content or experiment results.
The manuscript now explicitly sets green citation/URL boxes, red
internal-reference boxes, and one-point PDF borders through `hyperref`.

Post-export audit for `C:/Users/wangz/Downloads/16.pdf`:

- Pages: 25
- Size: 382,537 bytes
- SHA256: `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`
- Link annotations: 46 total on pages `[(2, 40), (4, 3), (5, 3)]`
- Colors: green = 40, red = 6, cyan = 0
- Borders: `(0, 0, 1)` for every link annotation
- Visual audit: rendered pages 2, 4, and 5; link boxes are crisp and aligned.
