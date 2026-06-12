#!/usr/bin/env python
"""Synthetic evidence for action-conditioned self-occlusion certificates.

The simulator isolates one mechanism: a robot arm periodically blocks the
camera's line of sight to objects. The comparison asks whether a tracker treats
all missed detections alike or uses robot kinematics to certify that a miss was
caused by self-occlusion.
"""

from __future__ import annotations

import csv
import math
import random
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
FIGURES = ROOT / "figures"
DOCS = ROOT / "docs"
PAPER = ROOT / "paper"
STATUS = ROOT / "child_status.md"


@dataclass
class ObjectState:
    angle_deg: float
    removal_time: int
    first_seen: bool = False


@dataclass
class TrackerState:
    present: bool = False
    misses: int = 0
    ever_seen: bool = False


def ensure_dirs() -> None:
    EXPERIMENTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    PAPER.mkdir(exist_ok=True)


def write_status(stage: str, facts: Iterable[str], failures: Iterable[str] = ()) -> None:
    lines = [
        "# Child Status",
        "",
        f"- Stage: {stage}",
        "- Last command/tool: `python scripts/run_self_occlusion_experiment.py`",
        "- Current facts:",
    ]
    for fact in facts:
        lines.append(f"  - {fact}")
    failures = list(failures)
    lines.append("- Failures:")
    if failures:
        for failure in failures:
            lines.append(f"  - {failure}")
    else:
        lines.append("  - none")
    lines.extend(["- Recovery steps:", "  - none", "- Next: write LaTeX paper and compile.", ""])
    try:
        STATUS.write_text("\n".join(lines), encoding="utf-8")
    except Exception:
        pass


def arm_center(t: int, phase: float, speed: float) -> float:
    return 45.0 * math.sin((2.0 * math.pi * speed * t / 80.0) + phase)


def is_self_occluded(angle: float, t: int, phase: float, width: float, speed: float) -> bool:
    center = arm_center(t, phase, speed)
    return abs(angle - center) <= width / 2.0


def init_objects(rng: random.Random, n_objects: int, horizon: int) -> List[ObjectState]:
    objects = []
    for _ in range(n_objects):
        angle = rng.uniform(-52.0, 52.0)
        if rng.random() < 0.32:
            removal_time = rng.randint(horizon // 3, horizon - 20)
        else:
            removal_time = horizon + 1
        objects.append(ObjectState(angle_deg=angle, removal_time=removal_time))
    return objects


def update_tracker(
    tracker: TrackerState,
    detected: bool,
    certified_occluded: bool,
    policy: str,
    ttl: int,
) -> TrackerState:
    state = TrackerState(tracker.present, tracker.misses, tracker.ever_seen)
    if detected:
        state.present = True
        state.misses = 0
        state.ever_seen = True
        return state
    if not state.ever_seen:
        return state
    if policy == "long_memory":
        state.misses += 1
        if state.misses > 30:
            state.present = False
        return state
    if policy == "certificate" and certified_occluded:
        state.misses = 0
        return state
    state.misses += 1
    if state.misses > ttl:
        state.present = False
    return state


def run_episode(
    rng: random.Random,
    episode: int,
    policy: str,
    ttl: int,
    width: float,
    speed: float,
    horizon: int,
    n_objects: int,
    detection_prob: float,
    certificate_noise: float,
    certificate_false_negative: float = 0.0,
    certificate_false_positive: float = 0.0,
) -> Dict[str, float]:
    objects = init_objects(rng, n_objects, horizon)
    trackers = [TrackerState() for _ in objects]
    phase = rng.uniform(0.0, 2.0 * math.pi)

    tp = fp = fn = tn = 0
    occluded_exists_frames = 0
    occluded_kept_frames = 0
    clear_absent_frames = 0
    clear_absent_stale_frames = 0
    clear_exists_frames = 0
    clear_exists_missing_frames = 0
    deletion_events = 0
    occlusion_survival_checks = 0
    occlusion_survivals = 0

    last_occluded = [False for _ in objects]
    had_track_before_occlusion = [False for _ in objects]

    for t in range(horizon):
        for i, obj in enumerate(objects):
            exists = t < obj.removal_time
            true_occ = exists and is_self_occluded(obj.angle_deg, t, phase, width, speed)
            noisy_angle = obj.angle_deg + rng.gauss(0.0, certificate_noise)
            certified_occ = is_self_occluded(noisy_angle, t, phase, width + 2.0, speed)
            if certificate_false_negative > 0.0 and certified_occ and rng.random() < certificate_false_negative:
                certified_occ = False
            if certificate_false_positive > 0.0 and (not certified_occ) and rng.random() < certificate_false_positive:
                certified_occ = True
            detected = exists and (not true_occ) and (rng.random() < detection_prob)

            before_present = trackers[i].present
            trackers[i] = update_tracker(trackers[i], detected, certified_occ, policy, ttl)
            after_present = trackers[i].present

            if before_present and not after_present:
                deletion_events += 1

            if true_occ:
                occluded_exists_frames += 1
                if after_present:
                    occluded_kept_frames += 1
            if (not exists) and (not true_occ):
                clear_absent_frames += 1
                if after_present:
                    clear_absent_stale_frames += 1
            if exists and (not true_occ):
                clear_exists_frames += 1
                if not after_present:
                    clear_exists_missing_frames += 1

            if true_occ and not last_occluded[i]:
                had_track_before_occlusion[i] = before_present
            if (not true_occ) and last_occluded[i] and exists and had_track_before_occlusion[i]:
                occlusion_survival_checks += 1
                if after_present:
                    occlusion_survivals += 1
                had_track_before_occlusion[i] = False
            last_occluded[i] = true_occ

            if exists and after_present:
                tp += 1
            elif exists and not after_present:
                fn += 1
            elif (not exists) and after_present:
                fp += 1
            else:
                tn += 1

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2.0 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return {
        "episode": episode,
        "policy": policy,
        "ttl": ttl,
        "width_deg": width,
        "speed": speed,
        "detection_prob": detection_prob,
        "certificate_noise": certificate_noise,
        "certificate_false_negative": certificate_false_negative,
        "certificate_false_positive": certificate_false_positive,
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "occluded_keep_rate": occluded_kept_frames / occluded_exists_frames if occluded_exists_frames else 0.0,
        "stale_clear_absence_rate": clear_absent_stale_frames / clear_absent_frames if clear_absent_frames else 0.0,
        "clear_exists_missing_rate": clear_exists_missing_frames / clear_exists_frames if clear_exists_frames else 0.0,
        "occlusion_survival_rate": occlusion_survivals / occlusion_survival_checks if occlusion_survival_checks else 0.0,
        "deletion_events": deletion_events,
    }


def mean(values: List[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def stderr(values: List[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.stdev(values) / math.sqrt(len(values))


def summarize(rows: List[Dict[str, float]]) -> List[Dict[str, str]]:
    groups: Dict[Tuple[str, float], List[Dict[str, float]]] = {}
    for row in rows:
        groups.setdefault((str(row["policy"]), float(row["width_deg"])), []).append(row)
    summary = []
    for (policy, width), items in sorted(groups.items(), key=lambda x: (x[0][1], x[0][0])):
        summary.append(
            {
                "policy": policy,
                "width_deg": f"{width:.1f}",
                "episodes": str(len(items)),
                "f1_mean": f"{mean([float(i['f1']) for i in items]):.3f}",
                "f1_se": f"{stderr([float(i['f1']) for i in items]):.3f}",
                "occluded_keep_rate_mean": f"{mean([float(i['occluded_keep_rate']) for i in items]):.3f}",
                "stale_clear_absence_rate_mean": f"{mean([float(i['stale_clear_absence_rate']) for i in items]):.3f}",
                "clear_exists_missing_rate_mean": f"{mean([float(i['clear_exists_missing_rate']) for i in items]):.3f}",
                "occlusion_survival_rate_mean": f"{mean([float(i['occlusion_survival_rate']) for i in items]):.3f}",
                "deletion_events_mean": f"{mean([float(i['deletion_events']) for i in items]):.2f}",
            }
        )
    return summary


def write_csv(path: Path, rows: List[Dict[str, float]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_summary_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_latex_table(summary: List[Dict[str, str]]) -> None:
    selected = [row for row in summary if row["width_deg"] in {"18.0", "30.0", "42.0"}]
    policy_names = {
        "ttl_short": "Short TTL",
        "long_memory": "Long memory",
        "certificate": "Ours: certificate",
    }
    lines = [
        "\\begin{tabular}{llrrrr}",
        "\\hline",
        "Occlusion width & Policy & F1 & Keep under self-occ. & Stale absent & Survival \\\\",
        "\\hline",
    ]
    for row in selected:
        lines.append(
            f"{row['width_deg']} & {policy_names.get(row['policy'], row['policy'])} & "
            f"{row['f1_mean']} & {row['occluded_keep_rate_mean']} & "
            f"{row['stale_clear_absence_rate_mean']} & {row['occlusion_survival_rate_mean']} \\\\"
        )
    lines.extend(["\\hline", "\\end{tabular}", ""])
    (PAPER / "experiment_table.tex").write_text("\n".join(lines), encoding="utf-8")


def run_certificate_noise_stress(rng: random.Random) -> List[Dict[str, str]]:
    rows: List[Dict[str, float]] = []
    episode = 0
    for noise in [0.0, 1.25, 3.0, 6.0, 10.0, 16.0]:
        for _ in range(120):
            episode += 1
            rows.append(
                run_episode(
                    rng=rng,
                    episode=episode,
                    policy="certificate",
                    ttl=3,
                    width=42.0,
                    speed=1.0,
                    horizon=160,
                    n_objects=14,
                    detection_prob=0.96,
                    certificate_noise=noise,
                )
            )
    groups: Dict[float, List[Dict[str, float]]] = {}
    for row in rows:
        groups.setdefault(float(row["certificate_noise"]), []).append(row)
    stress = []
    for noise, items in sorted(groups.items()):
        stress.append(
            {
                "certificate_noise": f"{noise:.2f}",
                "episodes": str(len(items)),
                "f1_mean": f"{mean([float(i['f1']) for i in items]):.3f}",
                "occluded_keep_rate_mean": f"{mean([float(i['occluded_keep_rate']) for i in items]):.3f}",
                "stale_clear_absence_rate_mean": f"{mean([float(i['stale_clear_absence_rate']) for i in items]):.3f}",
                "clear_exists_missing_rate_mean": f"{mean([float(i['clear_exists_missing_rate']) for i in items]):.3f}",
                "occlusion_survival_rate_mean": f"{mean([float(i['occlusion_survival_rate']) for i in items]):.3f}",
            }
        )
    write_csv(EXPERIMENTS / "certificate_noise_episode_results.csv", rows)
    write_summary_csv(EXPERIMENTS / "certificate_noise_stress.csv", stress)
    write_certificate_noise_table(stress)
    return stress


def run_certificate_corruption_stress(rng: random.Random) -> List[Dict[str, str]]:
    settings = [
        ("clean", 0.0, 0.0),
        ("false_negative_10pct", 0.10, 0.0),
        ("false_negative_25pct", 0.25, 0.0),
        ("false_negative_50pct", 0.50, 0.0),
        ("false_positive_10pct", 0.0, 0.10),
        ("false_positive_25pct", 0.0, 0.25),
        ("false_positive_50pct", 0.0, 0.50),
    ]
    rows: List[Dict[str, float]] = []
    episode = 0
    for label, fn_rate, fp_rate in settings:
        for _ in range(120):
            episode += 1
            row = run_episode(
                rng=rng,
                episode=episode,
                policy="certificate",
                ttl=3,
                width=42.0,
                speed=1.0,
                horizon=160,
                n_objects=14,
                detection_prob=0.96,
                certificate_noise=1.25,
                certificate_false_negative=fn_rate,
                certificate_false_positive=fp_rate,
            )
            row["scenario"] = label
            rows.append(row)
    groups: Dict[str, List[Dict[str, float]]] = {}
    for row in rows:
        groups.setdefault(str(row["scenario"]), []).append(row)
    stress = []
    for label, items in groups.items():
        stress.append(
            {
                "scenario": label,
                "episodes": str(len(items)),
                "f1_mean": f"{mean([float(i['f1']) for i in items]):.3f}",
                "occluded_keep_rate_mean": f"{mean([float(i['occluded_keep_rate']) for i in items]):.3f}",
                "stale_clear_absence_rate_mean": f"{mean([float(i['stale_clear_absence_rate']) for i in items]):.3f}",
                "clear_exists_missing_rate_mean": f"{mean([float(i['clear_exists_missing_rate']) for i in items]):.3f}",
                "occlusion_survival_rate_mean": f"{mean([float(i['occlusion_survival_rate']) for i in items]):.3f}",
            }
        )
    write_csv(EXPERIMENTS / "certificate_corruption_episode_results.csv", rows)
    write_summary_csv(EXPERIMENTS / "certificate_corruption_stress.csv", stress)
    write_certificate_corruption_table(stress)
    return stress


def write_certificate_noise_table(stress: List[Dict[str, str]]) -> None:
    selected = [row for row in stress if row["certificate_noise"] in {"0.00", "1.25", "3.00", "6.00", "10.00", "16.00"}]
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\hline",
        "Certificate noise & F1 & Keep under self-occ. & Stale absent & Survival \\\\",
        "\\hline",
    ]
    for row in selected:
        lines.append(
            f"{row['certificate_noise']} & {row['f1_mean']} & "
            f"{row['occluded_keep_rate_mean']} & {row['stale_clear_absence_rate_mean']} & "
            f"{row['occlusion_survival_rate_mean']} \\\\"
        )
    lines.extend(["\\hline", "\\end{tabular}", ""])
    (EXPERIMENTS / "certificate_noise_table.tex").write_text("\n".join(lines), encoding="utf-8")


def write_certificate_corruption_table(stress: List[Dict[str, str]]) -> None:
    selected = [
        "clean",
        "false_negative_25pct",
        "false_negative_50pct",
        "false_positive_25pct",
        "false_positive_50pct",
    ]
    by_label = {row["scenario"]: row for row in stress}
    labels = {
        "clean": "clean",
        "false_negative_25pct": "25\\% false negative",
        "false_negative_50pct": "50\\% false negative",
        "false_positive_25pct": "25\\% false positive",
        "false_positive_50pct": "50\\% false positive",
    }
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\hline",
        "Certificate corruption & F1 & Keep under self-occ. & Stale absent & Survival \\\\",
        "\\hline",
    ]
    for label in selected:
        row = by_label[label]
        lines.append(
            f"{labels[label]} & {row['f1_mean']} & {row['occluded_keep_rate_mean']} & "
            f"{row['stale_clear_absence_rate_mean']} & {row['occlusion_survival_rate_mean']} \\\\"
        )
    lines.extend(["\\hline", "\\end{tabular}", ""])
    (EXPERIMENTS / "certificate_corruption_table.tex").write_text("\n".join(lines), encoding="utf-8")


def write_markdown_summary(
    summary: List[Dict[str, str]],
    noise_stress: List[Dict[str, str]],
    corruption_stress: List[Dict[str, str]],
) -> None:
    lines = [
        "# Experiment Summary",
        "",
        "The simulator evaluates three deletion policies under robot self-occlusion:",
        "",
        "- `ttl_short`: delete after three consecutive misses.",
        "- `long_memory`: keep tracks through long gaps regardless of visibility cause.",
        "- `certificate`: delete after three clear-view misses, but freeze the deletion counter when robot kinematics certify self-occlusion.",
        "",
        "## Aggregate Results",
        "",
        "| Occlusion width | Policy | F1 | Keep under self-occ. | Stale absent | Clear-visible missing | Survival |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary:
        lines.append(
            f"| {row['width_deg']} | {row['policy']} | {row['f1_mean']} | "
            f"{row['occluded_keep_rate_mean']} | {row['stale_clear_absence_rate_mean']} | "
            f"{row['clear_exists_missing_rate_mean']} | {row['occlusion_survival_rate_mean']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Short TTL has low stale-object rates but loses tracks during long robot self-occlusion. Long memory preserves objects under occlusion but also preserves removed objects in clear view. The certificate policy targets the missing cause: it preserves only when robot geometry predicts unobservability, giving a better persistence/staleness tradeoff in this controlled setting.",
            "",
            "## V2 Certificate-Noise Stress",
            "",
            "The hardening stress reruns the certificate policy at 42 degree self-occlusion while increasing calibration noise in the certificate geometry.",
            "",
            "| Certificate noise | F1 | Keep under self-occ. | Stale absent | Survival |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in noise_stress:
        lines.append(
            f"| {row['certificate_noise']} | {row['f1_mean']} | {row['occluded_keep_rate_mean']} | "
            f"{row['stale_clear_absence_rate_mean']} | {row['occlusion_survival_rate_mean']} |"
        )
    lines.extend(
        [
            "",
            "Interpretation: the certificate advantage depends on calibrated robot geometry. Large certificate noise lowers object-state F1 and occlusion survival, so the method should be framed as a visibility-semantics mechanism, not as a calibration-free tracker.",
            "",
            "## V2 Certificate-Corruption Stress",
            "",
            "This stress directly flips the certificate event at 42 degree self-occlusion. False negatives make real self-occlusions count as clear misses; false positives make clear misses look robot-occluded.",
            "",
            "| Scenario | F1 | Keep under self-occ. | Stale absent | Survival |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in corruption_stress:
        lines.append(
            f"| {row['scenario']} | {row['f1_mean']} | {row['occluded_keep_rate_mean']} | "
            f"{row['stale_clear_absence_rate_mean']} | {row['occlusion_survival_rate_mean']} |"
        )
    lines.extend(
        [
            "",
            "Interpretation: false-negative certificates destroy the persistence benefit, while false positives increase stale-object retention. The method therefore depends on conservative but not overbroad robot-visibility certificates.",
            "",
        ]
    )
    (DOCS / "experiment_summary.md").write_text("\n".join(lines), encoding="utf-8")


def try_write_plot(summary: List[Dict[str, str]]) -> List[str]:
    failures = []
    try:
        import matplotlib.pyplot as plt  # type: ignore
    except Exception as exc:
        failures.append(f"matplotlib unavailable; plot skipped: {exc}")
        return failures
    policies = ["ttl_short", "long_memory", "certificate"]
    labels = {"ttl_short": "Short TTL", "long_memory": "Long memory", "certificate": "Certificate"}
    widths = sorted({float(row["width_deg"]) for row in summary})
    data = {(row["policy"], float(row["width_deg"])): row for row in summary}
    plt.figure(figsize=(6.6, 4.0))
    for policy in policies:
        ys = [float(data[(policy, width)]["f1_mean"]) for width in widths]
        plt.plot(widths, ys, marker="o", linewidth=2.0, label=labels[policy])
    plt.xlabel("Robot self-occlusion width (degrees)")
    plt.ylabel("Object-state F1")
    plt.ylim(0.0, 1.02)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES / "persistence_tradeoff.pdf")
    plt.savefig(FIGURES / "persistence_tradeoff.png", dpi=180)
    plt.close()
    return failures


def main() -> int:
    ensure_dirs()
    write_status("experiment running", ["Starting self-occlusion simulator with fixed seed 1601."])
    rng = random.Random(1601)
    policies = [("ttl_short", 3), ("long_memory", 3), ("certificate", 3)]
    widths = [18.0, 30.0, 42.0]
    rows: List[Dict[str, float]] = []
    episode = 0
    for width in widths:
        for policy, ttl in policies:
            for _ in range(120):
                episode += 1
                rows.append(
                    run_episode(
                        rng=rng,
                        episode=episode,
                        policy=policy,
                        ttl=ttl,
                        width=width,
                        speed=1.0,
                        horizon=160,
                        n_objects=14,
                        detection_prob=0.96,
                        certificate_noise=1.25,
                    )
                )
    summary = summarize(rows)
    write_csv(EXPERIMENTS / "episode_results.csv", rows)
    write_summary_csv(EXPERIMENTS / "summary.csv", summary)
    write_latex_table(summary)
    noise_stress = run_certificate_noise_stress(random.Random(1616))
    corruption_stress = run_certificate_corruption_stress(random.Random(1617))
    write_markdown_summary(summary, noise_stress, corruption_stress)
    failures = try_write_plot(summary)
    write_status(
        "experiment complete",
        [
            f"Wrote {len(rows)} episode rows to experiments/episode_results.csv.",
            "Wrote experiments/summary.csv, certificate stress CSVs, docs/experiment_summary.md, and paper/experiment_table.tex.",
            "If matplotlib was available, wrote figures/persistence_tradeoff.pdf/png.",
        ],
        failures,
    )
    print(f"wrote_episode_rows={len(rows)}")
    if failures:
        print("plot_status=skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
