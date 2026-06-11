# Paper 16 Plan: Object Persistence Under Robot Occlusion

## Objective
Produce a complete, runnable, anonymous ICLR-style robotics paper package for `16_object_persistence_under_robot_occlusion`, including broad literature artifacts, a defensible novelty decision, runnable evidence, compiled PDF at `C:/Users/wangz/Downloads/16.pdf`, public GitHub push, and final audit.

## Safety and Execution Rules
- Use short, non-interactive PowerShell commands with explicit timeouts for long work.
- Avoid fragile inline Python/PowerShell for complex logic; write helper scripts and run them.
- Keep `child_status.md` compact and current; status update failures are nonfatal.
- Reuse any useful existing artifacts if present.
- For LaTeX, prefer direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` with generous timeout.
- Document failures and recovery steps instead of aborting.

## Stages
1. Initialize folders and status.
2. Inspect existing repo state and tool availability safely.
3. Retrieve or synthesize a 1000-paper robotics/perception/occlusion landscape from bibliographic APIs and local search terms.
4. Build:
   - `docs/related_work_matrix.csv` with at least 1000 entries
   - `docs/literature_map.md`
   - `docs/hostile_prior_work.md`
   - `docs/novelty_boundary_map.md`
   - `docs/novelty_decision.md`
   - `docs/claims.md`
   - `docs/reviewer_attacks.md`
5. Perform serious skim/deep read/hostile prior synthesis:
   - 1000-paper landscape sweep
   - 300-paper serious skim
   - 200-250-paper deep read
   - 100-paper hostile prior-work set
6. Select the strongest paper direction only after novelty analysis.
7. Implement runnable evidence for the chosen thesis.
8. Write an anonymous ICLR-style paper using the latest official ICLR template available at runtime.
9. Sanitize bibliography/text and compile the PDF.
10. Save final PDF only to `C:/Users/wangz/Downloads/16.pdf`.
11. Create/push public GitHub repo `16_object_persistence_under_robot_occlusion`, or document failure.
12. Write `docs/final_audit.md` with all required answers.

## Initial Research Hypothesis To Test, Not Assume
Self-occlusion by the robot may deserve to be the central challenge in persistent object state. The literature sweep must decide whether this remains strongest or whether another robotics/embodied-intelligence mechanism is more novel.

