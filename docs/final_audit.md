# Final Audit

Checked: 2026-06-20

1. **Chosen thesis:** Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.
2. **Field assumption broken:** A missed detection is not a single exchangeable event; robot self-occlusion makes some misses non-evidence of absence, while clear-view misses are evidence against persistence.
3. **New central mechanism:** Kinematic visibility certificates gate object deletion by distinguishing clear-view absence from robot-certified unobservability.
4. **Genuine novelty:** The mechanism changes the observation alphabet used by persistent robot perception. It is not a bigger model, benchmark-only contribution, generic uncertainty head, active-learning loop, verifier, module mashup, LLM planner, or RL policy.
5. **Closest hostile prior work:** Online multi-object tracking with missed-frame patience; semantic/object SLAM; amodal perception; 6D pose tracking under partial visibility; active perception. The adversarial synthesis is in `docs/hostile_prior_work.md`.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains exactly 1,000 entries. The earlier sweep performed a 1,000-paper landscape pass, top-300 serious skim, top-230 metadata/abstract deep read, and top-100 hostile prior-work set.
7. **Proof/formal-claim status:** The paper includes a small non-identifiability proposition with proof sketch. It supports only the claim that observation-only miss streams cannot identify object absence versus robot self-occlusion.
8. **Full-scale execution plan:** `docs/full_scale_execution_plan.md` was written before substantive v3 edits and records the target experiments, RAM-light execution strategy, manuscript expansion plan, and acceptance checklist.
9. **Strongest evidence:** The v3 runner completed with stage `complete`, 1,124 seed-row summaries, and 0 plot failures across eight families. Main geometry results: certificate F1 0.950, keep-under-self-occlusion 0.821, stale clear-absence 0.255, survival 1.000; short TTL F1 0.818; long-memory stale clear-absence 0.515.
10. **Boundary evidence:** Calibration noise 6/inflation 2/latency 3 gives F1 0.926 with certificate precision 0.685 and recall 0.844. Direct corruption shows 50% false negatives reduce keep-under-self-occlusion to 0.322; 75% false positives raise stale clear-absence to 0.681. Random geometry drops to F1 0.582.
11. **Biggest weaknesses:** Synthetic evidence, object-ID abstraction, no real robot validation, dependence on calibrated geometry, certificate false positives/false negatives, external-occluder ambiguity, association stress, and no contact-dynamics model.
12. **Readiness judgment:** Final under the current full-scale mechanism-paper standard. Scope must remain honest: this is not a calibrated hardware systems or real-robot state-of-the-art claim.
13. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/16.pdf`.
14. **Downloads PDF verification:** 25 pages, 382,537 bytes, PDF 1.5.
15. **Downloads PDF SHA256:** `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`.
16. **Required text markers found in exported PDF:** v3 marker, `1,124`, `0.950`, `0.818`, `0.255`, `0.926`, `0.322`, and `Artifact-To-Claim`.
17. **VLA-style boxed-link audit:** 46 link annotations on pages `[(2, 40), (4, 3), (5, 3)]`; colors green = 40, red = 6, cyan = 0; all borders `(0, 0, 1)`.
18. **Visual link audit:** pages 2, 4, and 5 rendered after export; green citation/URL boxes and red internal-reference boxes are crisp and aligned.
19. **Local build PDF status:** `paper/main.pdf` removed after the canonical Downloads copy.
20. **GitHub URL:** `https://github.com/Jason-Wang313/16_object_persistence_under_robot_occlusion`.
