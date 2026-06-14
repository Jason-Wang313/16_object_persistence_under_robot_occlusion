# Child Status

- Stage: full-scale v3 final artifact exported and verified.
- Last major command/tool: `python experiments/full_scale_occlusion_certificates.py`
- Current facts:
  - Full-scale runner completed with stage `complete`.
  - Wrote 1,124 seed-row summaries across eight experiment families.
  - Generated CSV summaries, LaTeX tables, PDF/PNG figures, `metadata.json`, and `progress.json` under `results/full_scale/`.
  - Manuscript imports v3 generated figures and tables and compiled to 25 pages before export.
  - Canonical final PDF is `C:/Users/wangz/Downloads/16.pdf`, 25 pages, 382,537 bytes, SHA256 `B74479204FE59A984915A9ECDD763BC796290AE7BE304C4B16CBDEE973C4F0A4`.
  - Local `paper/main.pdf` was removed after the canonical copy.
  - Current claim is mechanism-level: robot self-occlusion changes missed-detection semantics; this is not a real-robot state-of-the-art claim.
- Failures:
  - none in the final v3 runner; plot failures were 0.
- Recovery steps:
  - none required.
- Next:
  - Commit, push, and verify upstream match before moving to paper 17.
