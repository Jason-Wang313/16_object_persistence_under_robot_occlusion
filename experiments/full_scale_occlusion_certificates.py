import csv
import json
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "full_scale"
DOCS = ROOT / "docs"

MASTER_SEED = 16016


def ensure_dirs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def write_progress(**kwargs: object) -> None:
    payload = {"stage": "running"}
    payload.update(kwargs)
    (OUT / "progress.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def arm_center(t: int, phase: float, speed: float, latency: int = 0) -> float:
    tt = max(0, t - latency)
    return 45.0 * math.sin((2.0 * math.pi * speed * tt / 80.0) + phase)


def is_blocked(angle: float, t: int, phase: float, width: float, speed: float, latency: int = 0) -> bool:
    return abs(angle - arm_center(t, phase, speed, latency)) <= width / 2.0


def init_objects(rng: random.Random, n: int, horizon: int, removal_prob: float) -> List[Dict[str, float]]:
    objs = []
    for i in range(n):
        angle = rng.uniform(-55.0, 55.0)
        if rng.random() < removal_prob:
            removal = rng.randint(max(10, horizon // 4), horizon - 10)
        else:
            removal = horizon + 1
        objs.append({"id": i, "angle": angle, "initial_angle": angle, "removal": removal})
    return objs


def external_blocked(rng: random.Random, rate: float, duration_scale: str, active_until: int, t: int) -> Tuple[bool, int]:
    if t < active_until:
        return True, active_until
    if rng.random() < rate:
        if duration_scale == "short":
            dur = rng.randint(3, 8)
        elif duration_scale == "long":
            dur = rng.randint(15, 35)
        else:
            dur = rng.randint(8, 18)
        return True, t + dur
    return False, active_until


def corrupt_certificate(
    rng: random.Random,
    cert: bool,
    fn_rate: float,
    fp_rate: float,
    mode: str,
    burst_state: Dict[str, int],
    obj_id: int,
    t: int,
) -> bool:
    if mode == "bursty":
        key = f"{obj_id}"
        if burst_state.get(key, 0) > t:
            if cert:
                return False
            return True
        if rng.random() < 0.012:
            burst_state[key] = t + rng.randint(5, 15)
            if cert:
                return False
            return True
    if cert and rng.random() < fn_rate:
        return False
    if (not cert) and rng.random() < fp_rate:
        return True
    return cert


def update_tracker(state: Dict[str, float], detected: bool, certified: bool, policy: str, ttl: float) -> Dict[str, float]:
    s = dict(state)
    if detected:
        s["present"] = 1.0
        s["misses"] = 0.0
        s["score"] = 1.0
        s["ever"] = 1.0
        return s
    if s["ever"] < 0.5:
        return s

    if policy in {"long_memory", "amodal_proxy"}:
        s["misses"] += 0.35 if policy == "amodal_proxy" else 1.0
        if s["misses"] > 30:
            s["present"] = 0.0
        return s
    if policy in {"certificate", "cert_hazard", "visibility_weighted", "oracle_visibility", "cert_external_aware"} and certified:
        if policy == "visibility_weighted":
            s["misses"] += 0.15
        else:
            s["misses"] = max(0.0, s["misses"] - 0.10)
        s["score"] = max(s["score"], 0.80)
        return s
    if policy in {"hazard_filter", "kalman_missing"}:
        s["score"] *= 0.88 if policy == "hazard_filter" else 0.92
        s["present"] = 1.0 if s["score"] >= 0.28 else 0.0
        return s
    if policy == "no_clear_delete":
        s["present"] = 1.0
        return s

    s["misses"] += 1.0
    if s["misses"] > ttl:
        s["present"] = 0.0
    return s


def simulate_episode(
    rng: random.Random,
    policy: str,
    width: float = 42.0,
    speed: float = 1.0,
    n_objects: int = 14,
    horizon: int = 110,
    detection_prob: float = 0.96,
    removal_prob: float = 0.32,
    cert_noise: float = 1.25,
    inflation: float = 2.0,
    latency: int = 0,
    fn_rate: float = 0.0,
    fp_rate: float = 0.0,
    corruption_mode: str = "independent",
    external_rate: float = 0.0,
    external_duration: str = "medium",
    external_labeled: bool = False,
    association_swap: float = 0.0,
    hidden_motion: str = "static",
    motion_model: str = "correct",
) -> Dict[str, float]:
    objs = init_objects(rng, n_objects, horizon, removal_prob)
    phase = rng.uniform(0.0, 2.0 * math.pi)
    trackers = [{"present": 0.0, "misses": 0.0, "score": 0.0, "ever": 0.0, "pred_angle": obj["angle"]} for obj in objs]
    external_until = [0 for _ in objs]
    burst_state: Dict[str, int] = {}

    tp = fp = fn = tn = 0
    id_switches = 0
    cert_tp = cert_fp = cert_fn = 0
    occluded_exists = occluded_kept = 0
    clear_absent = clear_absent_stale = 0
    external_absent = external_absent_stale = 0
    clear_exists = clear_exists_missing = 0
    deletion_events = 0
    stale_duration = 0
    reappear_checks = reappear_error = 0.0
    last_self_occ = [False for _ in objs]
    had_track_before_occ = [False for _ in objs]
    survival_checks = survivals = 0

    for t in range(horizon):
        for i, obj in enumerate(objs):
            exists = t < obj["removal"]
            if exists and hidden_motion in {"drift", "external"} and last_self_occ[i]:
                obj["angle"] += rng.uniform(-0.18, 0.18)
            if exists and hidden_motion == "robot_contact" and last_self_occ[i]:
                obj["angle"] += rng.uniform(-0.35, 0.35)

            true_self = exists and is_blocked(obj["angle"], t, phase, width, speed)
            ext, external_until[i] = external_blocked(rng, external_rate, external_duration, external_until[i], t)
            true_external = exists and ext
            visible = exists and (not true_self) and (not true_external)
            detected = visible and rng.random() < detection_prob
            if detected and rng.random() < association_swap:
                id_switches += 1
                detected = False

            cert_angle = trackers[i]["pred_angle"] + rng.gauss(0.0, cert_noise)
            cert = is_blocked(cert_angle, t, phase, max(0.0, width + inflation), speed, latency)
            cert = corrupt_certificate(rng, cert, fn_rate, fp_rate, corruption_mode, burst_state, i, t)
            if policy == "no_robot_action":
                cert = False
            elif policy == "random_geometry":
                cert = rng.random() < 0.35
            elif policy == "overbroad_certificate":
                cert = cert or rng.random() < 0.45
            elif policy == "underbroad_certificate":
                cert = cert and rng.random() < 0.45
            elif policy == "external_as_self":
                cert = cert or true_external
            elif policy == "oracle_visibility":
                cert = true_self
            elif policy == "cert_external_aware" and external_labeled and true_external:
                cert = False

            if true_self and cert:
                cert_tp += 1
            elif (not true_self) and cert:
                cert_fp += 1
            elif true_self and not cert:
                cert_fn += 1

            before = trackers[i]["present"] > 0.5
            ttl = 3.0
            if policy == "ttl_medium":
                ttl = 8.0
            elif policy == "ttl_short":
                ttl = 3.0
            update_policy = {
                "ttl_short": "ttl",
                "ttl_medium": "ttl",
                "no_robot_action": "ttl",
                "random_geometry": "certificate",
                "overbroad_certificate": "certificate",
                "underbroad_certificate": "certificate",
                "external_as_self": "certificate",
                "oracle_visibility": "oracle_visibility",
            }.get(policy, policy)
            trackers[i] = update_tracker(trackers[i], detected, cert, update_policy, ttl)
            after = trackers[i]["present"] > 0.5
            if detected:
                if motion_model == "correct":
                    trackers[i]["pred_angle"] = obj["angle"]
                else:
                    trackers[i]["pred_angle"] = 0.85 * trackers[i]["pred_angle"] + 0.15 * obj["angle"]
            elif after and motion_model == "correct" and hidden_motion in {"drift", "robot_contact", "external"}:
                trackers[i]["pred_angle"] += 0.05 * (obj["angle"] - trackers[i]["pred_angle"])

            if before and not after:
                deletion_events += 1
            if true_self:
                occluded_exists += 1
                if after:
                    occluded_kept += 1
            if (not exists) and (not true_self):
                clear_absent += 1
                if after:
                    clear_absent_stale += 1
                    stale_duration += 1
            if (not exists) and ext:
                external_absent += 1
                if after:
                    external_absent_stale += 1
            if exists and not true_self and not true_external:
                clear_exists += 1
                if not after:
                    clear_exists_missing += 1

            if true_self and not last_self_occ[i]:
                had_track_before_occ[i] = before
            if (not true_self) and last_self_occ[i] and exists and had_track_before_occ[i]:
                survival_checks += 1
                if after:
                    survivals += 1
                if detected:
                    reappear_checks += 1.0
                    reappear_error += abs(trackers[i]["pred_angle"] - obj["angle"])
                had_track_before_occ[i] = False
            last_self_occ[i] = true_self

            if exists and after:
                tp += 1
            elif exists and not after:
                fn += 1
            elif (not exists) and after:
                fp += 1
            else:
                tn += 1

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2.0 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    cert_precision = cert_tp / (cert_tp + cert_fp) if (cert_tp + cert_fp) else 0.0
    cert_recall = cert_tp / (cert_tp + cert_fn) if (cert_tp + cert_fn) else 0.0
    return {
        "f1": f1,
        "precision": precision,
        "recall": recall,
        "occluded_keep": occluded_kept / occluded_exists if occluded_exists else 0.0,
        "stale_clear_absence": clear_absent_stale / clear_absent if clear_absent else 0.0,
        "external_stale_absence": external_absent_stale / external_absent if external_absent else 0.0,
        "clear_missing": clear_exists_missing / clear_exists if clear_exists else 0.0,
        "survival": survivals / survival_checks if survival_checks else 0.0,
        "deletion_events": float(deletion_events),
        "stale_duration": float(stale_duration),
        "cert_precision": cert_precision,
        "cert_recall": cert_recall,
        "id_switches": float(id_switches),
        "reappear_error": reappear_error / reappear_checks if reappear_checks else 0.0,
    }


def summarize_episodes(episodes: List[Dict[str, float]]) -> Dict[str, float]:
    keys = episodes[0].keys()
    return {k: sum(ep[k] for ep in episodes) / len(episodes) for k in keys}


def run_cell(seed: int, policy: str, episodes: int = 3, **kwargs: object) -> Dict[str, float]:
    rng = random.Random(seed)
    eps = [simulate_episode(rng, policy=policy, **kwargs) for _ in range(episodes)]
    return summarize_episodes(eps)


def write_csv(df: pd.DataFrame, name: str) -> None:
    df.to_csv(OUT / name, index=False, quoting=csv.QUOTE_MINIMAL)


def latex_table(df: pd.DataFrame, cols: List[str], headers: List[str], name: str) -> None:
    lines = [r"\begin{tabular}{" + "l" * len(cols) + "}", r"\toprule", " & ".join(headers) + r" \\", r"\midrule"]
    for _, row in df.iterrows():
        vals = []
        for col in cols:
            val = row[col]
            if isinstance(val, float):
                vals.append(f"{val:.3f}")
            else:
                vals.append(str(val).replace("_", r"\_"))
        lines.append(" & ".join(vals) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    (OUT / name).write_text("\n".join(lines), encoding="utf-8")


def save_bar(df: pd.DataFrame, x: str, y: str, hue: str, title: str, name: str) -> None:
    plt.figure(figsize=(7.2, 3.8))
    labels = list(df[x].astype(str).unique())
    hues = list(df[hue].astype(str).unique())
    xx = list(range(len(labels)))
    width = 0.8 / max(1, len(hues))
    for i, hval in enumerate(hues):
        sub = df[df[hue].astype(str) == hval].copy()
        sub["_x"] = sub[x].astype(str)
        sub = sub.set_index("_x")
        vals = [float(sub.loc[label, y]) if label in sub.index else 0.0 for label in labels]
        plt.bar([v + (i - (len(hues) - 1) / 2) * width for v in xx], vals, width, label=hval.replace("_", " "))
    plt.xticks(xx, labels, rotation=25, ha="right")
    plt.ylim(0, 1.05 if y in {"f1", "occluded_keep", "stale_clear_absence", "cert_precision", "cert_recall"} else None)
    plt.ylabel(y.replace("_", " "))
    plt.title(title)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.pdf")
    plt.savefig(OUT / f"{name}.png", dpi=200)
    plt.close()


def save_line(df: pd.DataFrame, x: str, y: str, hue: str, title: str, name: str) -> None:
    plt.figure(figsize=(7.2, 3.8))
    for hval, sub in df.groupby(hue):
        sub = sub.sort_values(x)
        plt.plot(sub[x], sub[y], marker="o", label=str(hval).replace("_", " "))
    plt.ylim(0, 1.05 if y in {"f1", "occluded_keep", "stale_clear_absence", "cert_precision", "cert_recall"} else None)
    plt.xlabel(x.replace("_", " "))
    plt.ylabel(y.replace("_", " "))
    plt.title(title)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.pdf")
    plt.savefig(OUT / f"{name}.png", dpi=200)
    plt.close()


def family_a() -> pd.DataFrame:
    rows = []
    policies = ["ttl_short", "ttl_medium", "long_memory", "certificate", "visibility_weighted", "hazard_filter", "oracle_visibility"]
    for width in [18.0, 42.0, 60.0]:
        for speed in [0.5, 1.0]:
            for n_objects in [8, 16]:
                for detection_prob in [0.90, 0.98]:
                    for policy in policies:
                        for seed in range(3):
                            stats = run_cell(
                                MASTER_SEED + 1000 + int(width) * 13 + int(speed * 10) + n_objects * 7 + seed,
                                policy,
                                width=width,
                                speed=speed,
                                n_objects=n_objects,
                                detection_prob=detection_prob,
                                removal_prob=0.32,
                            )
                            stats.update({"family": "A_geometry", "width": width, "speed": speed, "n_objects": n_objects, "detection_prob": detection_prob, "policy": policy, "seed": seed})
                            rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_a_geometry_seed.csv")
    summary = df.groupby(["width", "policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_a_geometry_summary.csv")
    table = summary[summary["width"] == 42.0][["policy", "f1", "occluded_keep", "stale_clear_absence", "survival"]].sort_values("f1", ascending=False)
    latex_table(table, ["policy", "f1", "occluded_keep", "stale_clear_absence", "survival"], ["Policy", "F1", "Keep self-occ.", "Stale absent", "Survival"], "table_main_geometry.tex")
    save_bar(table, "policy", "f1", "policy", "Main self-occlusion geometry setting", "figure_main_geometry")
    return df


def family_b() -> pd.DataFrame:
    rows = []
    for noise in [0.0, 3.0, 6.0, 10.0, 16.0]:
        for inflation in [0.0, 2.0, 6.0]:
            for latency in [0, 1, 3, 6]:
                for seed in range(3):
                    stats = run_cell(MASTER_SEED + 2000 + int(noise * 10) + int(inflation * 7) + latency * 3 + seed, "certificate", width=42.0, cert_noise=noise, inflation=inflation, latency=latency)
                    stats.update({"family": "B_calibration", "noise": noise, "inflation": inflation, "latency": latency, "policy": "certificate", "seed": seed})
                    rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_b_calibration_seed.csv")
    summary = df.groupby(["noise", "inflation", "latency", "policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_b_calibration_summary.csv")
    table = summary[(summary["latency"] == 3) & (summary["inflation"].isin([0.0, 2.0, 6.0]))][["noise", "inflation", "f1", "cert_precision", "cert_recall", "stale_clear_absence"]]
    latex_table(table, ["noise", "inflation", "f1", "cert_precision", "cert_recall", "stale_clear_absence"], ["Noise", "Infl.", "F1", "Cert prec.", "Cert rec.", "Stale"], "table_calibration.tex")
    save_line(summary[(summary["inflation"] == 2.0) & (summary["latency"] == 3)], "noise", "f1", "policy", "Certificate calibration noise", "figure_calibration")
    return df


def family_c() -> pd.DataFrame:
    rows = []
    for fn in [0.0, 0.25, 0.50, 0.75]:
        for fp in [0.0, 0.25, 0.50, 0.75]:
            for mode in ["independent", "bursty"]:
                for seed in range(3):
                    stats = run_cell(MASTER_SEED + 3000 + int(fn * 100) + int(fp * 1000) + seed, "certificate", fn_rate=fn, fp_rate=fp, corruption_mode=mode)
                    stats.update({"family": "C_corruption", "false_negative": fn, "false_positive": fp, "mode": mode, "policy": "certificate", "seed": seed})
                    rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_c_corruption_seed.csv")
    summary = df.groupby(["false_negative", "false_positive", "mode", "policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_c_corruption_summary.csv")
    table = summary[(summary["mode"] == "independent") & (((summary["false_negative"] == 0.0) & (summary["false_positive"].isin([0.0, 0.25, 0.50, 0.75]))) | ((summary["false_positive"] == 0.0) & (summary["false_negative"].isin([0.25, 0.50, 0.75]))))][["false_negative", "false_positive", "f1", "occluded_keep", "stale_clear_absence"]]
    latex_table(table, ["false_negative", "false_positive", "f1", "occluded_keep", "stale_clear_absence"], ["FN", "FP", "F1", "Keep", "Stale"], "table_corruption.tex")
    save_line(summary[(summary["mode"] == "independent") & (summary["false_positive"] == 0.0)], "false_negative", "occluded_keep", "policy", "False negatives erase persistence", "figure_corruption")
    return df


def family_d() -> pd.DataFrame:
    rows = []
    for ext_rate in [0.0, 0.15, 0.30]:
        for duration in ["long"]:
            for labeled in [False, True]:
                for policy in ["ttl_short", "long_memory", "certificate", "cert_external_aware"]:
                    for seed in range(3):
                        stats = run_cell(MASTER_SEED + 4000 + int(ext_rate * 1000) + len(duration) * 11 + int(labeled) * 17 + seed, policy, external_rate=ext_rate, external_duration=duration, external_labeled=labeled)
                        stats.update({"family": "D_external", "external_rate": ext_rate, "duration": duration, "external_labeled": labeled, "policy": policy, "seed": seed})
                        rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_d_external_seed.csv")
    summary = df.groupby(["external_rate", "duration", "external_labeled", "policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_d_external_summary.csv")
    table = summary[(summary["duration"] == "long") & (summary["external_labeled"] == True) & (summary["external_rate"].isin([0.0, 0.15, 0.30]))][["external_rate", "policy", "f1", "external_stale_absence", "stale_clear_absence"]]
    latex_table(table, ["external_rate", "policy", "f1", "external_stale_absence", "stale_clear_absence"], ["Ext. rate", "Policy", "F1", "Ext. stale", "Clear stale"], "table_external_occluders.tex")
    save_bar(table, "external_rate", "f1", "policy", "External occluder stress", "figure_external_occluders")
    return df


def family_e() -> pd.DataFrame:
    rows = []
    for swap in [0.0, 0.15, 0.30]:
        for ambiguity in ["low", "high"]:
            for policy in ["oracle_visibility", "certificate", "ttl_short", "long_memory"]:
                for seed in range(3):
                    assoc_swap = swap * (1.7 if ambiguity == "high" and policy != "oracle_visibility" else 1.0)
                    stats = run_cell(MASTER_SEED + 5000 + int(swap * 1000) + len(ambiguity) + seed, policy, association_swap=assoc_swap)
                    stats.update({"family": "E_association", "swap": swap, "ambiguity": ambiguity, "policy": policy, "seed": seed})
                    rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_e_association_seed.csv")
    summary = df.groupby(["swap", "ambiguity", "policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_e_association_summary.csv")
    table = summary[(summary["ambiguity"] == "high")][["swap", "policy", "f1", "id_switches", "survival"]]
    latex_table(table, ["swap", "policy", "f1", "id_switches", "survival"], ["Swap", "Policy", "F1", "ID switches", "Survival"], "table_association.tex")
    save_line(table, "swap", "f1", "policy", "Association ambiguity stress", "figure_association")
    return df


def family_f() -> pd.DataFrame:
    rows = []
    for motion in ["static", "drift", "robot_contact", "external"]:
        for model in ["correct", "wrong"]:
            for policy in ["certificate", "long_memory", "cert_hazard"]:
                for seed in range(3):
                    stats = run_cell(MASTER_SEED + 6000 + len(motion) * 31 + len(model) * 13 + seed, policy, hidden_motion=motion, motion_model=model)
                    stats.update({"family": "F_hidden_motion", "motion": motion, "motion_model": model, "policy": policy, "seed": seed})
                    rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_f_hidden_motion_seed.csv")
    summary = df.groupby(["motion", "motion_model", "policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_f_hidden_motion_summary.csv")
    table = summary[(summary["motion_model"] == "wrong")][["motion", "policy", "f1", "reappear_error", "stale_clear_absence"]]
    latex_table(table, ["motion", "policy", "f1", "reappear_error", "stale_clear_absence"], ["Motion", "Policy", "F1", "Reappear err.", "Stale"], "table_hidden_motion.tex")
    save_bar(table, "motion", "f1", "policy", "Hidden object motion stress", "figure_hidden_motion")
    return df


def family_g() -> pd.DataFrame:
    rows = []
    policies = ["ttl_short", "ttl_medium", "long_memory", "certificate", "hazard_filter", "kalman_missing", "amodal_proxy", "cert_hazard"]
    for policy in policies:
        for seed in range(8):
            stats = run_cell(MASTER_SEED + 7000 + len(policy) * 37 + seed, policy, width=42.0, external_rate=0.08)
            stats.update({"family": "G_baselines", "policy": policy, "seed": seed})
            rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_g_baselines_seed.csv")
    summary = df.groupby(["policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_g_baselines_summary.csv")
    table = summary[["policy", "f1", "occluded_keep", "stale_clear_absence", "clear_missing"]].sort_values("f1", ascending=False)
    latex_table(table, ["policy", "f1", "occluded_keep", "stale_clear_absence", "clear_missing"], ["Policy", "F1", "Keep", "Stale", "Clear miss"], "table_strong_baselines.tex")
    save_bar(table, "policy", "f1", "policy", "Stronger persistence baselines", "figure_strong_baselines")
    return df


def family_h() -> pd.DataFrame:
    rows = []
    policies = ["certificate", "no_robot_action", "random_geometry", "overbroad_certificate", "underbroad_certificate", "no_clear_delete", "external_as_self", "oracle_visibility"]
    for policy in policies:
        for seed in range(8):
            stats = run_cell(MASTER_SEED + 8000 + len(policy) * 41 + seed, policy, external_rate=0.12)
            stats.update({"family": "H_ablation", "policy": policy, "seed": seed})
            rows.append(stats)
    df = pd.DataFrame(rows)
    write_csv(df, "family_h_ablation_seed.csv")
    summary = df.groupby(["policy"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_h_ablation_summary.csv")
    table = summary[["policy", "f1", "occluded_keep", "stale_clear_absence", "cert_precision", "cert_recall"]].sort_values("f1", ascending=False)
    latex_table(table, ["policy", "f1", "occluded_keep", "stale_clear_absence", "cert_precision", "cert_recall"], ["Policy", "F1", "Keep", "Stale", "Cert prec.", "Cert rec."], "table_ablation.tex")
    save_bar(table, "policy", "f1", "policy", "Ablations and negative controls", "figure_ablation")
    return df


def write_runtime_table(counts: Dict[str, int]) -> None:
    rows = pd.DataFrame(
        [
            {"Family": "A geometry", "Seed rows": counts["A"], "Artifact": "geometry summaries", "Stress": "self-occlusion coverage"},
            {"Family": "B calibration", "Seed rows": counts["B"], "Artifact": "calibration summaries", "Stress": "noise/inflation/latency"},
            {"Family": "C corruption", "Seed rows": counts["C"], "Artifact": "corruption summaries", "Stress": "false certs"},
            {"Family": "D external", "Seed rows": counts["D"], "Artifact": "mixed-cause summaries", "Stress": "external occluders"},
            {"Family": "E association", "Seed rows": counts["E"], "Artifact": "ID summaries", "Stress": "association swaps"},
            {"Family": "F hidden motion", "Seed rows": counts["F"], "Artifact": "motion summaries", "Stress": "hidden displacement"},
            {"Family": "G baselines", "Seed rows": counts["G"], "Artifact": "baseline summaries", "Stress": "strong alternatives"},
            {"Family": "H ablation", "Seed rows": counts["H"], "Artifact": "ablation summaries", "Stress": "negative controls"},
        ]
    )
    latex_table(rows, ["Family", "Seed rows", "Artifact", "Stress"], ["Family", "Seed rows", "Artifact", "Stress"], "table_runtime_memory.tex")


def write_claim_table(headline: Dict[str, float]) -> None:
    rows = pd.DataFrame(
        [
            {"Claim": "Self-occlusion is not a generic miss", "Evidence": "Family A", "Result": f"cert F1 {headline['cert_f1']:.3f}"},
            {"Claim": "Calibration has a precision/recall boundary", "Evidence": "Family B", "Result": f"noise 6 F1 {headline['noise6_f1']:.3f}"},
            {"Claim": "False positives preserve stale objects", "Evidence": "Family C", "Result": f"FP50 stale {headline['fp50_stale']:.3f}"},
            {"Claim": "External occluders need separate semantics", "Evidence": "Family D", "Result": f"external aware F1 {headline['external_aware_f1']:.3f}"},
            {"Claim": "Association remains a deployment blocker", "Evidence": "Family E", "Result": f"swap30 F1 {headline['swap30_f1']:.3f}"},
            {"Claim": "Ablations break the mechanism", "Evidence": "Family H", "Result": f"random geom F1 {headline['random_geometry_f1']:.3f}"},
        ]
    )
    latex_table(rows, ["Claim", "Evidence", "Result"], ["Claim", "Evidence", "Result"], "table_claim_evidence.tex")


def collect_headlines(a: pd.DataFrame, b: pd.DataFrame, c: pd.DataFrame, d: pd.DataFrame, e: pd.DataFrame, h: pd.DataFrame) -> Dict[str, float]:
    a_sum = a.groupby(["width", "policy"]).mean(numeric_only=True).reset_index()
    cert = a_sum[(a_sum["width"] == 42.0) & (a_sum["policy"] == "certificate")].iloc[0]
    short = a_sum[(a_sum["width"] == 42.0) & (a_sum["policy"] == "ttl_short")].iloc[0]
    long = a_sum[(a_sum["width"] == 42.0) & (a_sum["policy"] == "long_memory")].iloc[0]
    b_sum = b.groupby(["noise", "inflation", "latency"]).mean(numeric_only=True).reset_index()
    noise6 = b_sum[(b_sum["noise"] == 6.0) & (b_sum["inflation"] == 2.0) & (b_sum["latency"] == 3)].iloc[0]
    c_sum = c.groupby(["false_negative", "false_positive", "mode"]).mean(numeric_only=True).reset_index()
    fp50 = c_sum[(c_sum["false_negative"] == 0.0) & (c_sum["false_positive"] == 0.50) & (c_sum["mode"] == "independent")].iloc[0]
    fn50 = c_sum[(c_sum["false_negative"] == 0.50) & (c_sum["false_positive"] == 0.0) & (c_sum["mode"] == "independent")].iloc[0]
    d_sum = d.groupby(["external_rate", "duration", "external_labeled", "policy"]).mean(numeric_only=True).reset_index()
    extaware = d_sum[(d_sum["external_rate"] == 0.15) & (d_sum["duration"] == "long") & (d_sum["external_labeled"] == True) & (d_sum["policy"] == "cert_external_aware")].iloc[0]
    e_sum = e.groupby(["swap", "ambiguity", "policy"]).mean(numeric_only=True).reset_index()
    swap30 = e_sum[(e_sum["swap"] == 0.30) & (e_sum["ambiguity"] == "high") & (e_sum["policy"] == "certificate")].iloc[0]
    h_sum = h.groupby(["policy"]).mean(numeric_only=True).reset_index()
    randgeom = h_sum[h_sum["policy"] == "random_geometry"].iloc[0]
    return {
        "cert_f1": float(cert["f1"]),
        "short_f1": float(short["f1"]),
        "long_stale": float(long["stale_clear_absence"]),
        "cert_stale": float(cert["stale_clear_absence"]),
        "cert_keep": float(cert["occluded_keep"]),
        "noise6_f1": float(noise6["f1"]),
        "noise6_precision": float(noise6["cert_precision"]),
        "noise6_recall": float(noise6["cert_recall"]),
        "fp50_stale": float(fp50["stale_clear_absence"]),
        "fn50_keep": float(fn50["occluded_keep"]),
        "external_aware_f1": float(extaware["f1"]),
        "swap30_f1": float(swap30["f1"]),
        "random_geometry_f1": float(randgeom["f1"]),
    }


def write_report(headline: Dict[str, float], counts: Dict[str, int]) -> None:
    lines = [
        "# Full-Scale Experiment Report",
        "",
        "## Scope",
        "- Eight experiment families: geometry coverage, certificate calibration, corruption, external occluders, association, hidden motion, stronger baselines, and ablations.",
        f"- Total seed-row summaries: {sum(counts.values())}.",
        "- Outputs are under `results/full_scale/`.",
        "",
        "## Key Findings",
        f"- Main 42 degree setting: certificate F1 {headline['cert_f1']:.3f}, short-TTL F1 {headline['short_f1']:.3f}, certificate stale clear-absence {headline['cert_stale']:.3f}, long-memory stale clear-absence {headline['long_stale']:.3f}.",
        f"- Calibration stress at noise 6/inflation 2/latency 3: F1 {headline['noise6_f1']:.3f}, certificate precision {headline['noise6_precision']:.3f}, recall {headline['noise6_recall']:.3f}.",
        f"- Corruption stress: 50% false positives stale clear-absence {headline['fp50_stale']:.3f}; 50% false negatives keep-under-self-occlusion {headline['fn50_keep']:.3f}.",
        f"- External-aware policy at external rate 0.15/long/labeled: F1 {headline['external_aware_f1']:.3f}.",
        f"- High-ambiguity association with 30% swap: certificate F1 {headline['swap30_f1']:.3f}.",
        f"- Random-geometry ablation F1 {headline['random_geometry_f1']:.3f}.",
        "",
        "## Plot Status",
        "- All full-scale figures generated successfully.",
        "",
    ]
    (DOCS / "experiment_report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    write_progress(stage="running", family="A")
    a = family_a()
    write_progress(stage="running", family="B", family_a_rows=len(a))
    b = family_b()
    write_progress(stage="running", family="C", family_a_rows=len(a), family_b_rows=len(b))
    c = family_c()
    write_progress(stage="running", family="D", family_a_rows=len(a), family_b_rows=len(b), family_c_rows=len(c))
    d = family_d()
    write_progress(stage="running", family="E", family_a_rows=len(a), family_b_rows=len(b), family_c_rows=len(c), family_d_rows=len(d))
    e = family_e()
    write_progress(stage="running", family="F", family_a_rows=len(a), family_b_rows=len(b), family_c_rows=len(c), family_d_rows=len(d), family_e_rows=len(e))
    f = family_f()
    write_progress(stage="running", family="G", family_a_rows=len(a), family_b_rows=len(b), family_c_rows=len(c), family_d_rows=len(d), family_e_rows=len(e), family_f_rows=len(f))
    g = family_g()
    write_progress(stage="running", family="H", family_a_rows=len(a), family_b_rows=len(b), family_c_rows=len(c), family_d_rows=len(d), family_e_rows=len(e), family_f_rows=len(f), family_g_rows=len(g))
    h = family_h()
    counts = {"A": len(a), "B": len(b), "C": len(c), "D": len(d), "E": len(e), "F": len(f), "G": len(g), "H": len(h)}
    headline = collect_headlines(a, b, c, d, e, h)
    metadata = {
        "master_seed": MASTER_SEED,
        "families": [
            "geometry_coverage",
            "certificate_calibration",
            "certificate_corruption",
            "external_occluders",
            "association_reidentification",
            "hidden_motion",
            "strong_baselines",
            "ablation",
        ],
        "headline": headline,
        "seed_rows": counts,
    }
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_runtime_table(counts)
    write_claim_table(headline)
    write_report(headline, counts)
    write_progress(stage="complete", **{f"family_{k.lower()}_rows": v for k, v in counts.items()}, plot_failures=0)
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
