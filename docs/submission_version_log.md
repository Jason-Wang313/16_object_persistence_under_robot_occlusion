# Submission Version Log

## v1

- Generated occlusion-certificate paper with synthetic self-occlusion simulator.
- Main evidence: certificate F1 0.973 at 42 degree self-occlusion versus short TTL 0.817 and long-memory stale clear-absence 0.423.
- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf` (165,836 bytes at parent recovery).

## v2

Checked: 2026-06-13

- Added certificate-noise stress.
- Added direct false-negative/false-positive certificate-corruption stress.
- Added v2 manuscript marker, stress table, and calibration-boundary language.
- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf` (169,760 bytes).

## v3-link-hardening

Checked: 2026-06-20

- Added explicit VLA-style `\hypersetup` policy for boxed PDF links.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf` (25 pages, 382,537 bytes).
- SHA256: `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`.
- Link inventory: 46 annotations on pages `[(2, 40), (4, 3), (5, 3)]`; green = 40, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- Rendered pages 2, 4, and 5 after export and confirmed crisp green citation/URL boxes and red internal-reference boxes.
- Local `paper/main.pdf` removed after the canonical copy.

## v3

Checked: 2026-06-14

- Added a detailed full-scale execution plan before substantive edits.
- Added `experiments/full_scale_occlusion_certificates.py`.
- Ran eight experiment families with 1,124 seed-row summaries and 0 plot failures.
- Added generated v3 CSV summaries, figures, tables, metadata, and progress logs under `results/full_scale/`.
- Rewrote the manuscript around v3 evidence, expanded the appendices, added active re-observation/policy discussion, and compiled locally to 25 pages before final export.
- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf` (25 pages, 382,537 bytes).
- SHA256 before 2026-06-20 link-style hardening: `B74479204FE59A984915A9ECDD763BC796290AE7BE304C4B16CBDEE973C4F0A4`.
- Local `paper/main.pdf` removed after the canonical copy.
