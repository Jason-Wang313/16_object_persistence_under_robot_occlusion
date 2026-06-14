# Object Persistence Under Robot Occlusion

Anonymous ICLR-style paper package for paper 16 in the robotics/embodied-intelligence batch.

## Thesis

Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.

## Full-Scale v3 Evidence

The submission-hardening v3 pass replaces the short workshop-scale artifact with an eight-family full-scale evidence suite:

- geometry coverage,
- certificate calibration,
- direct certificate corruption,
- external occluders,
- association and re-identification stress,
- hidden object motion,
- stronger persistence baselines,
- negative-control ablations.

The runner completed with 1,124 seed-row summaries and zero plot failures. Outputs live under `results/full_scale/`.

Headline results:

- Main geometry family: certificate F1 0.950, keep-under-self-occlusion 0.821, stale clear-absence 0.255, survival 1.000.
- Short TTL baseline: F1 0.818 and keep-under-self-occlusion 0.114.
- Long-memory baseline: F1 0.916 and stale clear-absence 0.515.
- Calibration stress at noise 6/inflation 2/latency 3: F1 0.926, certificate precision 0.685, certificate recall 0.844.
- Direct corruption: 50% false-negative certificates reduce keep-under-self-occlusion to 0.322; 50% false-positive certificates raise stale clear-absence to 0.293.
- External occluders remain a boundary condition: external-aware certificate F1 is 0.357 in the labeled external-rate 0.15 setting.
- Random-geometry ablation drops to F1 0.582.

## Reproduce Evidence

Run the compact v2 simulator:

```powershell
python scripts/run_self_occlusion_experiment.py
```

Run the full-scale v3 suite:

```powershell
python experiments/full_scale_occlusion_certificates.py
```

Expected v3 outputs include CSV summaries, generated LaTeX tables, PDF/PNG figures, metadata, and progress logs in `results/full_scale/`.

## Rebuild Manuscript

Compile from `paper/` with:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Official Template Source

The paper writer downloads the official ICLR 2026 template from:

https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip

## Final PDF

The required final PDF path is:

`C:/Users/wangz/Downloads/16.pdf`

Final v3 export:

- Pages: 25.
- Size: 382,537 bytes.
- SHA256: `B74479204FE59A984915A9ECDD763BC796290AE7BE304C4B16CBDEE973C4F0A4`.
- Local `paper/main.pdf`: removed after the canonical copy.
