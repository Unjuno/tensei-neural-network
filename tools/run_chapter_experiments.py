#!/usr/bin/env python3
"""話別コードを再実行し、保存結果と照合する。CIは結果を書き換えない。"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

try:
    from .validate_workflow import result_is_pass
except ImportError:
    from validate_workflow import result_is_pass

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_EXPERIMENTS = ROOT / "experiments/chapters"


def reject_constant(value: str) -> None:
    raise ValueError(f"JSON非有限値: {value}")


def canonical(result: object) -> str:
    # boolと整数、キー欠落、配列の順序差も区別する。
    return json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False, separators=(",", ":"))


def verify_one(root: Path, package: Path, timeout: float = 30.0) -> list[str]:
    try:
        saved_path = package / "results.json"
        saved_bytes = saved_path.read_bytes()
        saved = json.loads(saved_bytes, parse_constant=reject_constant)
        completed = subprocess.run(
            [sys.executable, str(package / "run.py"), "--check"], cwd=root,
            check=False, capture_output=True, text=True, encoding="utf-8", timeout=timeout,
        )
        if completed.returncode:
            return [f"終了コード {completed.returncode}: {completed.stderr[-1000:]}"]
        if saved_path.read_bytes() != saved_bytes:
            return ["--check が保存結果を書き換えました"]
        fresh = json.loads(completed.stdout, parse_constant=reject_constant)
        if not result_is_pass(fresh, package.name) or not result_is_pass(saved, package.name):
            return ["chapter/result/checksが不正、または個別検査が不合格"]
        if canonical(fresh) != canonical(saved):
            return ["再実行結果が保存済みJSONと不一致。自動上書きは禁止"]
        return []
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        return [f"実行・保存結果を検証できません: {exc}"]


def run(root: Path, timeout: float = 30.0) -> int:
    folder = root / "experiments/chapters"
    if not folder.is_dir():
        print("[FAIL] experiments/chapters がありません")
        return 1
    count, failures = 0, []
    for package in sorted(folder.iterdir()):
        if not package.is_dir() or len(package.name) != 3 or not package.name.isdigit():
            continue
        if not (package / "run.py").exists():
            continue  # 非コード検証はverification.mdと意味レビューで扱う。
        count += 1
        errors = verify_one(root, package, timeout)
        if errors:
            failures.append(package.name)
        print(f"[{'FAIL' if errors else 'PASS'}] 第{package.name}話 " + "; ".join(errors))
    if not count:
        print("[SKIP] コード化された検証なし。検証済みという意味ではありません")
    else:
        print(f"[{'FAIL' if failures else 'PASS'}] 再実行と保存結果照合: {count}話")
    return int(bool(failures))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("timeoutは正数")
    return run(args.root.resolve(), args.timeout)


if __name__ == "__main__":
    raise SystemExit(main())
