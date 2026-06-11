#!/usr/bin/env python
"""Run the paper-16 build pipeline without requiring shell glue."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Iterable, List


ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "child_status.md"


def write_status(stage: str, facts: Iterable[str], failures: Iterable[str] = ()) -> None:
    lines = [
        "# Child Status",
        "",
        f"- Stage: {stage}",
        "- Last command/tool: `python scripts/build_all.py`",
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
    lines.extend(["- Recovery steps:", "  - See stage-specific docs and rerun the failed script directly.", "- Next: compile and push.", ""])
    try:
        STATUS.write_text("\n".join(lines), encoding="utf-8")
    except Exception:
        pass


def run_script(script: str, timeout: int) -> str:
    path = ROOT / "scripts" / script
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=str(ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    log_path = ROOT / "data"
    log_path.mkdir(exist_ok=True)
    (log_path / f"{script}.log").write_text(proc.stdout or "", encoding="utf-8")
    return f"{script}: exit={proc.returncode}"


def main() -> int:
    write_status("build_all running", ["Starting literature, experiment, and paper-source generation."])
    results: List[str] = []
    failures: List[str] = []
    for script, timeout in [
        ("build_literature.py", 540),
        ("run_self_occlusion_experiment.py", 180),
        ("write_paper.py", 180),
    ]:
        try:
            result = run_script(script, timeout)
            results.append(result)
            if not result.endswith("exit=0"):
                failures.append(result)
        except Exception as exc:
            failures.append(f"{script}: {exc}")
    write_status("build_all complete", results, failures)
    for result in results:
        print(result)
    for failure in failures:
        print("failure=" + failure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

