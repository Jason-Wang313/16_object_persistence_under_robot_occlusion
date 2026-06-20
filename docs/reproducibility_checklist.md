# Reproducibility Checklist

Run from the repository root.

## Compact Simulator

```powershell
python scripts\run_self_occlusion_experiment.py
```

This preserves the older compact simulator and writes artifacts under `experiments/`, `figures/`, and `paper/`.

## Full-Scale v3 Suite

```powershell
python experiments\full_scale_occlusion_certificates.py
```

Expected v3 artifacts:

- `results/full_scale/progress.json`
- `results/full_scale/metadata.json`
- `results/full_scale/family_a_geometry_seed.csv`
- `results/full_scale/family_a_geometry_summary.csv`
- `results/full_scale/family_b_calibration_seed.csv`
- `results/full_scale/family_b_calibration_summary.csv`
- `results/full_scale/family_c_corruption_seed.csv`
- `results/full_scale/family_c_corruption_summary.csv`
- `results/full_scale/family_d_external_seed.csv`
- `results/full_scale/family_d_external_summary.csv`
- `results/full_scale/family_e_association_seed.csv`
- `results/full_scale/family_e_association_summary.csv`
- `results/full_scale/family_f_hidden_motion_seed.csv`
- `results/full_scale/family_f_hidden_motion_summary.csv`
- `results/full_scale/family_g_baselines_seed.csv`
- `results/full_scale/family_g_baselines_summary.csv`
- `results/full_scale/family_h_ablation_seed.csv`
- `results/full_scale/family_h_ablation_summary.csv`
- `results/full_scale/table_*.tex`
- `results/full_scale/figure_*.pdf`
- `results/full_scale/figure_*.png`

The full-scale runner uses deterministic seeds, writes intermediate outputs to disk, and is designed to stay RAM-light by aggregating compact rows rather than retaining episode traces in memory.

## Manuscript Build

```powershell
Set-Location paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Acceptance checks:

- `pdfinfo paper/main.pdf` reports at least 25 pages before final export.
- `main.log` has no fatal LaTeX errors, undefined references, or overfull boxes.
- `pdftotext paper/main.pdf -` finds the v3 marker, 1,124-row claim, main metrics, and artifact-to-claim audit.

## Final Export Verification

- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf`
- Pages: 25
- Size: 382,537 bytes
- SHA256: `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`
- VLA-style boxed-link inventory: 46 annotations on pages `[(2, 40), (4, 3), (5, 3)]`; green = 40, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- Visual render audit: pages 2, 4, and 5 checked after export.
- Local build artifact: `paper/main.pdf` removed after export.
