# Child Status

- Stage: experiment complete
- Last command/tool: `python scripts/run_self_occlusion_experiment.py`
- Current facts:
  - Wrote 1080 episode rows to experiments/episode_results.csv.
  - Wrote experiments/summary.csv, certificate stress CSVs, docs/experiment_summary.md, and paper/experiment_table.tex.
  - If matplotlib was available, wrote figures/persistence_tradeoff.pdf/png.
- Failures:
  - none
- Recovery steps:
  - none
- Next: write LaTeX paper and compile.

## Submission-hardening v2 terminal status

Checked: 2026-06-13 00:32:35 +01:00

- Added certificate-noise stress and direct certificate-corruption stress.
- Clean certificate corruption stress: F1 0.975, keep-under-self-occlusion 0.920, stale clear-absence 0.143.
- 50% false-negative certificates: F1 0.930, keep-under-self-occlusion 0.674, survival 0.983.
- 50% false-positive certificates: F1 0.948, stale clear-absence 0.544.
- Rebuilt the manuscript and copied the canonical v2 PDF to `C:/Users/wangz/Downloads/16.pdf` (169,760 bytes).
- Local `paper/main.pdf` was removed after the canonical copy.
- Terminal decision: workshop-only / revise before main-conference submission.
- No new Desktop copy created during v2 hardening.
