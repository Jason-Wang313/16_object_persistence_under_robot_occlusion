# Object Persistence Under Robot Occlusion

Anonymous ICLR-style paper package for paper 16 in the robotics/embodied-intelligence batch.

## Thesis

Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.

## Reproduce Evidence

```powershell
python scripts/run_self_occlusion_experiment.py
```

Outputs:

- `experiments/episode_results.csv`
- `experiments/summary.csv`
- `docs/experiment_summary.md`
- `figures/persistence_tradeoff.pdf` if matplotlib is available

## Rebuild Literature and Paper Artifacts

```powershell
python scripts/build_literature.py
python scripts/run_self_occlusion_experiment.py
python scripts/write_paper.py
```

Compile from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.

## Official Template Source

The paper writer downloads the official ICLR 2026 template from:

https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip

## Final PDF

The required final PDF path is:

`C:/Users/wangz/Downloads/16.pdf`

## Submission-Hardening v2

- Added certificate-noise stress in `experiments/certificate_noise_stress.csv`.
- Added certificate-corruption stress in `experiments/certificate_corruption_stress.csv`.
- At 42 degree self-occlusion, clean certificate stress F1 is 0.975 with keep-under-self-occlusion 0.920 and stale clear-absence 0.143.
- With 50% certificate false negatives, keep-under-self-occlusion falls to 0.674 and F1 falls to 0.930.
- With 50% certificate false positives, stale clear-absence rises to 0.544 and F1 falls to 0.948.
- Decision remains workshop-only until validated with calibrated real robot geometry, real association, and external-occluder handling.
