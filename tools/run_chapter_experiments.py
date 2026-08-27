#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_EXPERIMENTS = ROOT / "experiments" / "chapters"


def main() -> int:
    failures: list[str] = []
    executed = 0

    if not CHAPTER_EXPERIMENTS.exists():
        print("[FAIL] experiments/chapters がありません")
        return 1

    for chapter in sorted(CHAPTER_EXPERIMENTS.iterdir()):
        if not chapter.is_dir() or not chapter.name.isdigit() or len(chapter.name) != 3:
            continue
        run_py = chapter / "run.py"
        if not run_py.exists():
            continue

        executed += 1
        print(f"[RUN] chapter {chapter.name}: {run_py.relative_to(ROOT)}")
        completed = subprocess.run(
            [sys.executable, str(run_py), "--check"],
            cwd=ROOT,
            check=False,
        )
        if completed.returncode != 0:
            failures.append(chapter.name)

    if failures:
        print("[FAIL] chapter experiments: " + ", ".join(failures))
        return 1

    print(f"[PASS] executable chapter experiments: {executed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
