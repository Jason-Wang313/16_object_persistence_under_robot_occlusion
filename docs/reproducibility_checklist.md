# Reproducibility Checklist

Run from the repository root:

```powershell
python scripts\run_self_occlusion_experiment.py
```

Expected artifacts:

- `experiments/episode_results.csv`
- `experiments/summary.csv`
- `experiments/certificate_noise_episode_results.csv`
- `experiments/certificate_noise_stress.csv`
- `experiments/certificate_noise_table.tex`
- `experiments/certificate_corruption_episode_results.csv`
- `experiments/certificate_corruption_stress.csv`
- `experiments/certificate_corruption_table.tex`
- `docs/experiment_summary.md`
- `paper/experiment_table.tex`
- `figures/persistence_tradeoff.pdf`
- `figures/persistence_tradeoff.png`

The script uses fixed Python `random.Random` seeds and does not require network access.
