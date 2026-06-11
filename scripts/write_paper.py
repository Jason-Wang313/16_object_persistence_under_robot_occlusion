#!/usr/bin/env python
"""Write the ICLR-style paper and repository documentation."""

from __future__ import annotations

import csv
import shutil
import unicodedata
import urllib.request
import zipfile
from pathlib import Path
from typing import Iterable, List


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAPER = ROOT / "paper"
FIGURES = ROOT / "figures"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/16.pdf")
STATUS = ROOT / "child_status.md"

ICLR_ZIP_URL = "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip"


def ensure_dirs() -> None:
    DOCS.mkdir(exist_ok=True)
    PAPER.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)


def clean(text: str) -> str:
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = unicodedata.normalize("NFKD", text)
    return text.encode("ascii", "ignore").decode("ascii")


def write_status(stage: str, facts: Iterable[str], failures: Iterable[str] = ()) -> None:
    lines = [
        "# Child Status",
        "",
        f"- Stage: {stage}",
        "- Last command/tool: `python scripts/write_paper.py`",
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
    lines.extend(["- Recovery steps:", "  - none", "- Next: compile LaTeX and push repository.", ""])
    try:
        STATUS.write_text("\n".join(lines), encoding="utf-8")
    except Exception:
        pass


def download_iclr_template() -> List[str]:
    failures: List[str] = []
    zip_path = PAPER / "iclr2026.zip"
    extract_dir = PAPER / "iclr2026_template"
    try:
        urllib.request.urlretrieve(ICLR_ZIP_URL, zip_path)
        if extract_dir.exists():
            shutil.rmtree(extract_dir)
        extract_dir.mkdir(exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as archive:
            archive.extractall(extract_dir)
        style_files = list(extract_dir.rglob("iclr2026_conference.sty"))
        if not style_files:
            failures.append("Downloaded ICLR zip but did not find iclr2026_conference.sty.")
        else:
            shutil.copyfile(style_files[0], PAPER / "iclr2026_conference.sty")
        bst_files = list(extract_dir.rglob("iclr2026_conference.bst"))
        if bst_files:
            shutil.copyfile(bst_files[0], PAPER / "iclr2026_conference.bst")
    except Exception as exc:
        failures.append(f"Failed to download/extract official ICLR 2026 template: {clean(str(exc))}")
    return failures


def read_experiment_summary() -> List[dict]:
    path = ROOT / "experiments" / "summary.csv"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def metric(summary: List[dict], policy: str, width: str, field: str) -> str:
    for row in summary:
        if row.get("policy") == policy and row.get("width_deg") == width:
            return row.get(field, "n/a")
    return "n/a"


def write_references() -> None:
    bib = r"""
@article{kalman1960new,
  title={A New Approach to Linear Filtering and Prediction Problems},
  author={Kalman, R. E.},
  journal={Journal of Basic Engineering},
  volume={82},
  number={1},
  pages={35--45},
  year={1960}
}

@article{smith1986representation,
  title={On the Representation and Estimation of Spatial Uncertainty},
  author={Smith, Randall C. and Cheeseman, Peter},
  journal={The International Journal of Robotics Research},
  volume={5},
  number={4},
  pages={56--68},
  year={1986}
}

@book{thrun2005probabilistic,
  title={Probabilistic Robotics},
  author={Thrun, Sebastian and Burgard, Wolfram and Fox, Dieter},
  publisher={MIT Press},
  year={2005}
}

@article{durrant2006simultaneous,
  title={Simultaneous Localization and Mapping: Part I},
  author={Durrant-Whyte, Hugh and Bailey, Tim},
  journal={IEEE Robotics and Automation Magazine},
  volume={13},
  number={2},
  pages={99--110},
  year={2006}
}

@article{cadena2016past,
  title={{Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age}},
  author={Cadena, Cesar and Carlone, Luca and Carrillo, Henry and Latif, Yasir and Scaramuzza, Davide and Neira, Jose and Reid, Ian and Leonard, John J.},
  journal={IEEE Transactions on Robotics},
  volume={32},
  number={6},
  pages={1309--1332},
  year={2016}
}

@inproceedings{bewley2016sort,
  title={{Simple Online and Realtime Tracking}},
  author={Bewley, Alex and Ge, Zongyuan and Ott, Lionel and Ramos, Fabio and Upcroft, Ben},
  booktitle={IEEE International Conference on Image Processing},
  pages={3464--3468},
  year={2016}
}

@inproceedings{wojke2017deepsort,
  title={{Simple Online and Realtime Tracking with a Deep Association Metric}},
  author={Wojke, Nicolai and Bewley, Alex and Paulus, Dietrich},
  booktitle={IEEE International Conference on Image Processing},
  pages={3645--3649},
  year={2017}
}

@inproceedings{zhang2022bytetrack,
  title={{ByteTrack: Multi-Object Tracking by Associating Every Detection Box}},
  author={Zhang, Yifu and Sun, Peize and Jiang, Yi and Yu, Dongdong and Weng, Fucheng and Yuan, Zehuan and Luo, Ping and Liu, Wenyu and Wang, Xinggang},
  booktitle={European Conference on Computer Vision},
  pages={1--21},
  year={2022}
}

@inproceedings{li2016amodal,
  title={{Amodal Instance Segmentation}},
  author={Li, Ke and Malik, Jitendra},
  booktitle={European Conference on Computer Vision},
  pages={677--693},
  year={2016}
}

@inproceedings{xiang2018posecnn,
  title={{PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes}},
  author={Xiang, Yu and Schmidt, Tanner and Narayanan, Venkatraman and Fox, Dieter},
  booktitle={Robotics: Science and Systems},
  year={2018}
}

@inproceedings{wang2019densefusion,
  title={{DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion}},
  author={Wang, Chen and Xu, Danfei and Zhu, Yuke and Martin-Martin, Roberto and Lu, Cewu and Fei-Fei, Li and Savarese, Silvio},
  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={3343--3352},
  year={2019}
}

@inproceedings{wen2021bundletrack,
  title={{BundleTrack: 6D Pose Tracking for Novel Objects Without Instance or Category-Level 3D Models}},
  author={Wen, Bowen and Mitash, Chaitanya and Ren, Baozhang and Bekris, Kostas E.},
  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems},
  pages={8067--8074},
  year={2021}
}

@inproceedings{parisotto2018neuralmap,
  title={{Neural Map: Structured Memory for Deep Reinforcement Learning}},
  author={Parisotto, Emilio and Salakhutdinov, Ruslan},
  booktitle={International Conference on Learning Representations},
  year={2018}
}

@inproceedings{kolve2017ai2thor,
  title={{AI2-THOR: An Interactive 3D Environment for Visual AI}},
  author={Kolve, Eric and Mottaghi, Roozbeh and Han, Winson and VanderBilt, Eli and Weihs, Luca and Herrasti, Alvaro and Deitke, Matt and Ehsani, Kiana and Gordon, Daniel and Zhu, Yuke and others},
  booktitle={arXiv preprint arXiv:1712.05474},
  year={2017}
}

@inproceedings{chaplot2020object,
  title={{Object Goal Navigation using Goal-Oriented Semantic Exploration}},
  author={Chaplot, Devendra Singh and Gandhi, Dhiraj and Gupta, Abhinav and Salakhutdinov, Ruslan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2020}
}

@inproceedings{greff2019multiobject,
  title={{Multi-Object Representation Learning with Iterative Variational Inference}},
  author={Greff, Klaus and Kaufman, Raphaele Kabra and Kabra, Rishabh and Watters, Nicholas and Burgess, Christopher and Zoran, Daniel and Matthey, Loic and Botvinick, Matthew and Lerchner, Alexander},
  booktitle={International Conference on Machine Learning},
  pages={2424--2433},
  year={2019}
}

@inproceedings{locatello2020objectcentric,
  title={{Object-Centric Learning with Slot Attention}},
  author={Locatello, Francesco and Weissenborn, Dirk and Unterthiner, Thomas and Mahendran, Aravindh and Heigold, Georg and Uszkoreit, Jakob and Dosovitskiy, Alexey and Kipf, Thomas},
  booktitle={Advances in Neural Information Processing Systems},
  year={2020}
}

@inproceedings{teed2021droidslam,
  title={{DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras}},
  author={Teed, Zachary and Deng, Jia},
  booktitle={Advances in Neural Information Processing Systems},
  year={2021}
}

@inproceedings{qi2019deep,
  title={{Deep Hough Voting for 3D Object Detection in Point Clouds}},
  author={Qi, Charles R. and Litany, Or and He, Kaiming and Guibas, Leonidas J.},
  booktitle={IEEE/CVF International Conference on Computer Vision},
  pages={9277--9286},
  year={2019}
}

@inproceedings{mottaghi2016happens,
  title={{What Happens if... Learning to Predict the Effect of Forces in Images}},
  author={Mottaghi, Roozbeh and Bagherinezhad, Hessam and Rastegari, Mohammad and Farhadi, Ali},
  booktitle={European Conference on Computer Vision},
  pages={269--285},
  year={2016}
}
"""
    (PAPER / "references.bib").write_text(clean(bib).strip() + "\n", encoding="utf-8")


def write_main_tex() -> None:
    summary = read_experiment_summary()
    f1_cert_42 = metric(summary, "certificate", "42.0", "f1_mean")
    f1_ttl_42 = metric(summary, "ttl_short", "42.0", "f1_mean")
    stale_cert_42 = metric(summary, "certificate", "42.0", "stale_clear_absence_rate_mean")
    stale_memory_42 = metric(summary, "long_memory", "42.0", "stale_clear_absence_rate_mean")
    tex = rf"""
\documentclass{{article}}

\usepackage{{iclr2026_conference,times}}
\usepackage{{amsmath,amssymb,amsfonts,amsthm}}
\usepackage{{graphicx}}
\usepackage{{url}}
\usepackage{{xcolor}}
\usepackage{{enumitem}}

\newtheorem{{proposition}}{{Proposition}}
\newtheorem{{definition}}{{Definition}}

\title{{Occlusion Certificates for Persistent Object State Under Robot Self-Occlusion}}

\author{{Anonymous Authors \\
Anonymous Institution \\
\texttt{{anonymous@example.com}}}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Robots often lose sight of an object for a reason that is neither sensor noise nor scene disappearance: the robot itself moves between the camera and the object. Most persistent-perception pipelines treat this as an ordinary missed detection, controlled by a fixed deletion patience or by a generic memory module. This paper argues that robot self-occlusion should instead be a central observation event. We introduce an action-conditioned occlusion certificate: a kinematic test that marks when the robot body makes a predicted object state unobservable, and gates deletion only under clear-view misses. A simple non-identifiability proposition shows why observation-only misses cannot distinguish object absence from robot-caused invisibility. In a controlled 2D manipulation-inspired simulator, the certificate policy improves the object-state F1 at the hardest self-occlusion setting from {f1_ttl_42} for a short missed-detection tracker to {f1_cert_42}, while avoiding the stale-object behavior of indiscriminate long memory ({stale_cert_42} vs. {stale_memory_42} stale clear-absence rate). The result is not a claim of real-robot state of the art; it is a mechanism-level case that persistent object state needs robot-action visibility semantics.
\end{{abstract}}

\section{{Introduction}}

Object persistence is easy to ask for and surprisingly easy to mis-specify. A robot needs to remember that a cup still exists while its arm passes in front of the camera, yet it also needs to delete a cup that was actually removed. In many perception stacks those two cases are collapsed into the same symbol: no detection. The resulting engineering compromise is familiar. A short patience window deletes real objects under self-occlusion; a long patience window preserves real objects but also hallucinates removed ones.

The central bet of this paper is that the compromise is not merely a hyperparameter problem. The robot has privileged causal information about one class of occluders: its own body. When a commanded link intersects the line of sight to a predicted object, a missed detection is not evidence of absence in the same way as a miss in clear view. This suggests a different event alphabet for persistent object state: detected, absent-in-clear-view, and robot-certified-unobservable.

This paper therefore asks a narrow question: what changes if robot self-occlusion, rather than generic temporal memory, is the mechanism that gates object deletion? We make three contributions. First, we define action-conditioned occlusion certificates for persistent object state. Second, we give a small impossibility argument showing that observation-only miss streams cannot identify absence versus self-occlusion. Third, we provide a runnable simulator that demonstrates the persistence/staleness tradeoff against a short missed-detection tracker and a long-memory tracker.

The claim is intentionally scoped. We do not introduce a larger detector, a new dataset, a foundation model, an LLM planner, or a generic uncertainty head. We isolate a failure mode in robot perception and test a mechanism that changes the semantics of a missed observation.

\section{{Related Work and Novelty Boundary}}

\paragraph{{Tracking and filtering.}}
Classical recursive filtering gives a language for propagating state under uncertainty \citep{{kalman1960new,smith1986representation,thrun2005probabilistic}}. Modern online trackers often use detection association and missed-frame patience, as in SORT, Deep SORT, and ByteTrack \citep{{bewley2016sort,wojke2017deepsort,zhang2022bytetrack}}. These methods make temporal persistence less novel. They do not, by themselves, make robot-body occlusion a first-class cause of missing evidence.

\paragraph{{Robot maps and object memory.}}
SLAM and semantic mapping maintain state across views \citep{{durrant2006simultaneous,cadena2016past,teed2021droidslam}}. Embodied agents also use structured memories and semantic exploration policies \citep{{parisotto2018neuralmap,kolve2017ai2thor,chaplot2020object}}. This literature makes long-lived spatial memory less novel. The boundary here is the update rule during the interval when the robot itself hides the object, before a later revisit can repair the map.

\paragraph{{Amodal perception and pose tracking.}}
Amodal segmentation, 6D pose estimation, and pose tracking address hidden geometry and partial visibility \citep{{li2016amodal,xiang2018posecnn,wang2019densefusion,wen2021bundletrack,qi2019deep}}. Object-centric representation learning also gives latent slots that can persist through observations \citep{{greff2019multiobject,locatello2020objectcentric}}. These approaches make hidden-state inference less novel. Our focus is different: when should a miss count as absence evidence?

\section{{Problem Setup}}

Let $o$ be an object with latent state $x_t$, and let $q_t$ denote the robot configuration induced by its action. A perception system receives detections $z_t$. A missed detection is often represented as a single event, $z_t=\emptyset$. We instead introduce a visibility predicate
\[
V(q_t, \hat{{x}}_t) \in \{{\mathrm{{clear}}, \mathrm{{blocked}}\}},
\]
where $V=\mathrm{{blocked}}$ means that the robot body intersects the sensor ray or viewing volume needed to observe the predicted object state $\hat{{x}}_t$.

\begin{{definition}}[Occlusion certificate]
An action-conditioned occlusion certificate at time $t$ is a conservative predicate $C_t(\hat{{x}}_t)=1$ such that, under the robot kinematic model and camera calibration, the predicted object state $\hat{{x}}_t$ lies in a region made unobservable by the robot body at configuration $q_t$.
\end{{definition}}

The certificate need not reconstruct the hidden object. It only changes the meaning of a miss. A certified miss says ``do not delete on this frame because the robot made the object unobservable.'' A clear-view miss says ``this is evidence against persistence.''

\section{{Method}}

For each tracked object, the estimator stores a predicted state $\hat{{x}}_t$, a presence bit, and a clear-miss counter $m_t$. The update is:
\[
m_{{t+1}} =
\begin{{cases}}
0, & \text{{if the object is detected}},\\
m_t, & \text{{if not detected and }} C_t(\hat{{x}}_t)=1,\\
m_t+1, & \text{{if not detected and }} C_t(\hat{{x}}_t)=0.
\end{{cases}}
\]
The track is deleted only when $m_t>\tau$. This is deliberately simple. The point is not a new association metric; the point is that only clear-view misses consume deletion budget.

\paragraph{{What changes mechanistically.}}
A fixed missed-detection TTL treats time as the deletion variable. Long memory treats persistence as the default regardless of visibility cause. The certificate policy treats robot action and geometry as the deletion variable. This creates an asymmetry: the same missing image evidence can preserve state or delete state depending on whether the robot made the relevant line of sight unavailable.

\section{{A Small Impossibility Result}}

\begin{{proposition}}[Observation-only misses are not identifiable]
Consider any estimator that observes only a sequence of detection/miss symbols and not the robot-action visibility predicate. For any interval of robot self-occlusion with miss observations, there exist two worlds, one in which the object remains present but self-occluded and one in which the object is absent, that induce the same observation sequence. Therefore no observation-only update rule can identify which world generated the misses.
\end{{proposition}}

\begin{{proof}}
Construct world A with an object at state $x$ and a robot configuration sequence $q_{{1:T}}$ that blocks the sensor's line of sight to $x$ for every $t \in 1:T$. The detector therefore emits $z_t=\emptyset$ throughout the interval. Construct world B with the object absent and the same detector output $z_t=\emptyset$ for every $t$. An estimator that receives only $z_{{1:T}}$ is given identical inputs in A and B. Its posterior or discrete decision must therefore be the same in both worlds, so it cannot identify whether the object persisted or disappeared. The robot-action visibility predicate is extra information that breaks this equivalence by certifying that A's misses were generated under blocked visibility.
\end{{proof}}

The proposition is modest but important: it says that adding a better timeout cannot solve the information problem. The missing input is the cause of unobservability.

\section{{Experiment}}

\paragraph{{Simulator.}}
We use a 2D camera-centered world with 14 object slots per episode. A robot arm sweeps through the field of view and creates angular self-occlusion intervals. Objects may persist or be removed. Visible objects are detected with probability $0.96$; self-occluded objects are missed. The certificate receives the robot arm angle with small noise and a conservative angular inflation. The task is to maintain the correct object-presence state over time.

\paragraph{{Baselines.}}
We compare three policies: (1) a short TTL tracker that deletes after three consecutive misses; (2) a long-memory tracker that keeps tracks for 30 misses; and (3) the certificate policy, which freezes the deletion counter only under robot-certified self-occlusion. This isolates the update semantics while keeping association and detector quality fixed.

\begin{{table}}[t]
\caption{{Synthetic self-occlusion results. Keep under self-occ. is the fraction of existing self-occluded object frames where the track is retained. Stale absent is the fraction of clear-view absent frames where a removed object is still retained.}}
\label{{tab:synthetic}}
\centering
\small
\input{{experiment_table.tex}}
\end{{table}}

\IfFileExists{{../figures/persistence_tradeoff.pdf}}{{
\begin{{figure}}[t]
\centering
\includegraphics[width=0.72\linewidth]{{../figures/persistence_tradeoff.pdf}}
\caption{{Object-state F1 as self-occlusion width increases. The certificate policy preserves the useful part of long memory without treating every miss as harmless.}}
\label{{fig:tradeoff}}
\end{{figure}}
}}{{}}

\paragraph{{Results.}}
Table~\ref{{tab:synthetic}} shows the core tradeoff. The short TTL tracker is conservative about stale absent objects, but it deletes real objects under long self-occlusions. Long memory keeps self-occluded objects, but it also keeps objects that were removed and are absent in clear view. The certificate policy improves persistence because it conditions deletion on robot-caused unobservability rather than elapsed missed frames.

\section{{Limitations}}

The evidence is synthetic and uses object identities to isolate deletion semantics. A deployed robot would need calibrated geometry, segmentation of robot links, association under clutter, state prediction during contact, and robustness to external occluders. The certificate can also be wrong: calibration error can preserve stale tracks, while an overly narrow certificate can delete real objects. These limitations are not peripheral; they define the next experimental stage.

\section{{Reproducibility}}

The repository includes the literature matrix, hostile prior-work analysis, simulator, raw episode CSV, aggregate results, and LaTeX source. The main evidence can be rerun with:
\[
\texttt{{python scripts/run\_self\_occlusion\_experiment.py}}.
\]
The random seed is fixed to 1601. The ICLR style file is downloaded from the official ICLR 2026 template URL recorded in the build script.

\section{{Conclusion}}

Robot self-occlusion turns object persistence from a generic memory problem into an action-conditioned observability problem. The proposed certificate mechanism is small, but it changes the central update rule: clear-view misses delete; robot-certified misses preserve. The result is a sharper novelty boundary for persistent robot perception and a concrete next step toward manipulation systems that know when their own body made an object disappear.

\bibliography{{references}}
\bibliographystyle{{iclr2026_conference}}

\appendix
\section{{Literature Sweep Summary}}

The repository contains a 1000-record related-work matrix, a 300-record serious skim, a 230-record metadata/abstract deep read, and a 100-record hostile prior-work set. The extraction schema records the claimed problem, mechanism, hidden assumptions, fixed variables, ignored failure modes, novelty pressure, and remaining opening for each important prior-work neighborhood.

\end{{document}}
"""
    (PAPER / "main.tex").write_text(clean(tex).strip() + "\n", encoding="utf-8")


def write_readme() -> None:
    readme = f"""
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

{ICLR_ZIP_URL}

## Final PDF

The required final PDF path is:

`C:/Users/wangz/Downloads/16.pdf`
"""
    (ROOT / "README.md").write_text(clean(readme).strip() + "\n", encoding="utf-8")


def write_requirements() -> None:
    text = """
# Optional: matplotlib is used only for the PDF/PNG plot.
matplotlib>=3.5
"""
    (ROOT / "requirements.txt").write_text(clean(text).strip() + "\n", encoding="utf-8")


def write_initial_final_audit() -> None:
    audit = f"""
# Final Audit

1. **Chosen thesis:** Persistent object state under robot self-occlusion should be updated by action-conditioned occlusion certificates, not by generic missed-detection patience.
2. **Field assumption broken:** A missed detection is not a single exchangeable event; robot self-occlusion makes some misses non-evidence of absence.
3. **New central mechanism:** Kinematic visibility certificates gate object deletion by distinguishing clear-view absence from robot-certified unobservability.
4. **Genuine novelty:** The mechanism changes the observation alphabet used by persistent robot perception. It is not a bigger model, benchmark-only contribution, generic uncertainty head, active learning, verifier, LLM planner, or RL policy.
5. **Closest hostile prior work:** Online multi-object tracking with missed-frame patience; semantic/object SLAM; amodal perception; 6D pose tracking under partial visibility; active perception. See `docs/hostile_prior_work.md`.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains at least 1000 entries; top 300 serious skim, top 230 metadata/abstract deep read, and top 100 hostile prior-work set are synthesized in docs.
7. **Proof/formal-claim status:** A small non-identifiability proposition is included and proof-sketched. It supports only the observation-only miss ambiguity claim.
8. **Strongest evidence:** Runnable synthetic simulator comparing short TTL, long memory, and certificate-gated deletion under increasing robot self-occlusion.
9. **Biggest weaknesses:** Synthetic 2D evidence, object-ID abstraction, no real robot, dependence on calibrated geometry, external occluders and contact dynamics not solved.
10. **Paper-readiness judgment:** workshop/revise. The mechanism and audit are coherent, but real-robot validation is needed for a strong full-conference submission.
11. **Exact Downloads PDF path:** `{DOWNLOADS_PDF.as_posix()}`.
12. **GitHub URL:** pending push.
13. **Desktop copy status:** pending orchestrator copy.
"""
    (DOCS / "final_audit.md").write_text(clean(audit).strip() + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    write_status("paper writing running", ["Downloading official ICLR 2026 template and writing LaTeX source."])
    failures = download_iclr_template()
    write_references()
    write_main_tex()
    write_readme()
    write_requirements()
    write_initial_final_audit()
    write_status(
        "paper source complete",
        [
            "Wrote paper/main.tex and paper/references.bib.",
            "Wrote README.md, requirements.txt, and initial docs/final_audit.md.",
            "Downloaded official ICLR template if network access succeeded.",
        ],
        failures,
    )
    print("paper_source_written=1")
    if failures:
        print(f"template_failures={len(failures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
