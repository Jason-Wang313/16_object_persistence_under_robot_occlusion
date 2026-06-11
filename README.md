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
