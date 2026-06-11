# Final Audit

1. **Chosen thesis:** Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.
2. **Field assumption broken:** A missed detection is not a single exchangeable event; robot self-occlusion makes some misses non-evidence of absence, while clear-view misses are evidence against persistence.
3. **New central mechanism:** Kinematic visibility certificates gate object deletion by distinguishing clear-view absence from robot-certified unobservability.
4. **Genuine novelty:** The mechanism changes the observation alphabet used by persistent robot perception. It is not a bigger model, benchmark-only contribution, generic uncertainty head, active-learning loop, verifier, module mashup, LLM planner, or RL policy.
5. **Closest hostile prior work:** Online multi-object tracking with missed-frame patience; semantic/object SLAM; amodal perception; 6D pose tracking under partial visibility; active perception. The 100-entry adversarial synthesis is in `docs/hostile_prior_work.md`.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains exactly 1000 entries. The run performed a 1000-paper landscape sweep, top-300 serious skim, top-230 metadata/abstract deep read, and top-100 hostile prior-work set.
7. **Proof/formal-claim status:** The paper includes a small non-identifiability proposition with proof sketch. It supports only the claim that observation-only miss streams cannot identify object absence versus robot self-occlusion.
8. **Strongest evidence:** Runnable synthetic self-occlusion simulator comparing short TTL, long memory, and certificate-gated deletion. At 42 degree self-occlusion, object-state F1 is 0.973 for the certificate policy versus 0.817 for short TTL, while stale clear-absence rate is 0.149 for the certificate policy versus 0.423 for long memory.
9. **Biggest weaknesses:** Synthetic 2D evidence, object-ID abstraction, no real robot validation, dependence on calibrated geometry, no external-occluder solution, and no contact-dynamics model.
10. **Paper-readiness judgment:** workshop/revise. The mechanism and audit are coherent, but hardware or high-fidelity simulation validation is needed for a strong full-conference robotics submission.
11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/16.pdf`.
12. **GitHub URL:** `https://github.com/Jason-Wang313/16_object_persistence_under_robot_occlusion`.
13. **Desktop copy status:** copied by orchestrator to `C:/Users/wangz/OneDrive/Desktop/16.pdf`.


## Orchestrator Desktop Copy

Checked: 2026-06-11 14:35:45 +01:00
Downloads PDF: C:/Users/wangz/Downloads/16.pdf
Desktop PDF: C:/Users/wangz/OneDrive/Desktop/16.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_16_20260611_143544.log
