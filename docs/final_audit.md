# Final Audit

1. **Chosen thesis:** Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.
2. **Field assumption broken:** A missed detection is not a single exchangeable event; robot self-occlusion makes some misses non-evidence of absence.
3. **New central mechanism:** Kinematic visibility certificates gate object deletion by distinguishing clear-view absence from robot-certified unobservability.
4. **Genuine novelty:** The mechanism changes the observation alphabet used by persistent robot perception. It is not a bigger model, benchmark-only contribution, generic uncertainty head, active learning, verifier, LLM planner, or RL policy.
5. **Closest hostile prior work:** Online multi-object tracking with missed-frame patience; semantic/object SLAM; amodal perception; 6D pose tracking under partial visibility; active perception. See `docs/hostile_prior_work.md`.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains at least 1000 entries; top 300 serious skim, top 230 metadata/abstract deep read, and top 100 hostile prior-work set are synthesized in docs.
7. **Proof/formal-claim status:** A small non-identifiability proposition is included and proof-sketched. It supports only the observation-only miss ambiguity claim.
8. **Strongest evidence:** Runnable synthetic simulator comparing short TTL, long memory, and certificate-gated deletion under increasing robot self-occlusion.
9. **Biggest weaknesses:** Synthetic 2D evidence, object-ID abstraction, no real robot, dependence on calibrated geometry, external occluders and contact dynamics not solved.
10. **Paper-readiness judgment:** workshop/revise. The mechanism and audit are coherent, but real-robot validation is needed for a strong full-conference submission.
11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/16.pdf`.
12. **GitHub URL:** pending push.
13. **Desktop copy status:** pending orchestrator copy.
