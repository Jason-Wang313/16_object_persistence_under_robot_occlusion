# Experiment Rigor Checklist

- Fixed seeds: yes (`1601`, `1616`, `1617`).
- Main episodes: 3 policies x 3 occlusion widths x 120 episodes = 1,080 episodes.
- Certificate-noise stress: 6 noise levels x 120 episodes.
- Certificate-corruption stress: 7 corruption settings x 120 episodes.
- Main raw output: `experiments/episode_results.csv`.
- V2 noise output: `experiments/certificate_noise_stress.csv`.
- V2 corruption output: `experiments/certificate_corruption_stress.csv`.
- Manuscript tables: `paper/experiment_table.tex`, `experiments/certificate_corruption_table.tex`.
- Remaining empirical gap: no real robot, no real association, no calibrated camera/robot geometry, no external occluders.
