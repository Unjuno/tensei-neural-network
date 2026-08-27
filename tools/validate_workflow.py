#!/usr/bin/env python3
"""Static validator for the fixed story-production workflow.

Checks structure and traceability only. Historical, scientific, and narrative
correctness still require semantic review.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Finding:
    level: str
    code: str
    message: str


def text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def rel(root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def add(out: list[Finding], level: str, code: str, message: str) -> None:
    out.append(Finding(level, code, message))


def chapters(root: Path) -> list[str]:
    d = root / "novel" / "chapters"
    return sorted({p.stem for p in d.glob("[0-9][0-9][0-9].md")}) if d.exists() else []


def require_files(root: Path, out: list[Finding]) -> None:
    required = [
        "POLICY.md", "POLICY_INDEX.md", "WORKFLOW.md", "AGENTS.md",
        "novel/WORLD_POLICY.md", "novel/bootstrap/README.md",
        "novel/state/README.md", "novel/entities/README.md",
        "novel/STYLE_WEBNOVEL.md", "experiments/README.md",
        "experiments/chapters/README.md",
    ]
    for name in required:
        if not (root / name).exists():
            add(out, "ERROR", "WF001", f"必須ファイルがありません: {name}")


def has_unverified_table_row(body: str) -> bool:
    """Detect UNVERIFIED only when used as a Markdown table cell.

    The word may legitimately appear in the legend explaining possible states.
    """
    return bool(re.search(r"^\|[^\n]*\|\s*UNVERIFIED\s*\|[^\n]*$", body, re.MULTILINE))


def check_chapter_packages(root: Path, out: list[Finding]) -> None:
    for num in chapters(root):
        package = root / "experiments" / "chapters" / num
        readme = package / "README.md"
        if not readme.exists():
            add(out, "ERROR", "WF010", f"第{num}話に話別検証packageがありません: {rel(root, readme)}")
            continue
        body = text(readme)
        if "PREPUBLICATION_VERIFIED" in body:
            term = package / "terminology.md"
            if term.exists():
                if has_unverified_table_row(text(term)):
                    add(out, "ERROR", "WF011", f"第{num}話はPREPUBLICATION_VERIFIEDだが未検証用語が残っています")
            else:
                add(out, "WARN", "WF012", f"第{num}話はPREPUBLICATION_VERIFIEDだがterminology.mdがありません。用語が無い話なら許容")


def event_ids(root: Path) -> set[str]:
    d = root / "novel" / "events"
    ids: set[str] = set()
    if d.exists():
        for p in d.glob("EVT-[0-9][0-9][0-9]-*.md"):
            m = re.match(r"(EVT-\d{3})-", p.name)
            if m:
                ids.add(m.group(1))
    return ids


def check_outline_refs(root: Path, out: list[Finding]) -> None:
    known = event_ids(root)
    d = root / "novel" / "chapters"
    if not d.exists():
        return
    for outline in d.glob("[0-9][0-9][0-9]-outline.md"):
        refs = set(re.findall(r"EVT-\d{3}", text(outline)))
        for missing in sorted(refs - known):
            add(out, "ERROR", "WF020", f"{rel(root, outline)} が存在しないeventを参照しています: {missing}")
        if not refs:
            add(out, "WARN", "WF021", f"{rel(root, outline)} に採用EVT参照がありません")


def duplicate_numbers(paths: Iterable[Path], pattern: re.Pattern[str]) -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {}
    for p in paths:
        m = pattern.match(p.name)
        if m:
            found.setdefault(m.group(1), []).append(p)
    return {k: v for k, v in found.items() if len(v) > 1}


def check_duplicate_ids(root: Path, out: list[Finding]) -> None:
    checks = [
        ("EVT", root / "novel/events", r"(EVT-\d{3})-.*\.md$", False),
        ("PER", root / "novel/personas", r"(PER-\d{3})-.*\.md$", False),
        ("ORG", root / "novel/organizations", r"(ORG-\d{3})-.*\.md$", False),
        ("BOOT", root / "novel/bootstrap", r"(BOOT-\d{3})-.*\.md$", False),
        ("EXP", root / "experiments", r"(EXP-\d{3})-.*$", True),
    ]
    for label, directory, regex, dirs_only in checks:
        if not directory.exists():
            continue
        items = [p for p in directory.iterdir() if p.is_dir() == dirs_only]
        for stable_id, paths in sorted(duplicate_numbers(items, re.compile(regex)).items()):
            add(out, "ERROR", "WF030", f"{label}定義番号が重複しています {stable_id}: " + ", ".join(rel(root, p) for p in paths))


def check_policy_links(root: Path, out: list[Finding]) -> None:
    workflow = text(root / "WORKFLOW.md")
    for name in ["POLICY.md", "novel/WORLD_POLICY.md", "experiments/chapters/README.md", "novel/STYLE_WEBNOVEL.md"]:
        if name not in workflow:
            add(out, "ERROR", "WF040", f"WORKFLOW.mdにpolicy参照がありません: {name}")
    if "POLICY.md" not in text(root / "novel/WORLD_POLICY.md"):
        add(out, "ERROR", "WF041", "WORLD_POLICY.mdがroot POLICY.mdの優先を明示していません")


def check_obsolete_terms(root: Path, out: list[Finding]) -> None:
    banned = {
        "《ローカル・フィールド》": "局所場の英語ルビ",
        "《フィクスト・ポイント》": "固定点の英語ルビ",
        "《アシンクロナス・アップデート》": "非同期更新の英語ルビ",
    }
    body = text(root / "novel/chapters/001.md")
    for token, label in banned.items():
        if token in body:
            add(out, "ERROR", "WF050", f"第1話に検証後廃止した表記が再混入しています: {label} {token}")


def check_verification_status(root: Path, out: list[Finding]) -> None:
    for num in chapters(root):
        body = text(root / "experiments/chapters" / num / "README.md")
        if "NOT READY FOR PUBLICATION" in body or "IN_PROGRESS" in body:
            add(out, "WARN", "WF060", f"第{num}話はまだ公開前検証未完了です")


def check_global_glossary(root: Path, out: list[Finding]) -> None:
    for name in ("GLOSSARY.md", "novel/GLOSSARY.md"):
        if (root / name).exists():
            add(out, "WARN", "WF070", f"全体Glossaryが存在します。現行方針では話別terminologyを優先してください: {name}")


def collect_findings(root: Path) -> list[Finding]:
    out: list[Finding] = []
    require_files(root, out)
    check_chapter_packages(root, out)
    check_outline_refs(root, out)
    check_duplicate_ids(root, out)
    check_policy_links(root, out)
    check_obsolete_terms(root, out)
    check_verification_status(root, out)
    check_global_glossary(root, out)
    order = {"ERROR": 0, "WARN": 1}
    return sorted(out, key=lambda f: (order.get(f.level, 9), f.code, f.message))


def run(root: Path, strict: bool) -> int:
    findings = collect_findings(root)
    for f in findings:
        print(f"[{f.level}] {f.code} {f.message}")
    errors = sum(f.level == "ERROR" for f in findings)
    warnings = sum(f.level == "WARN" for f in findings)
    print(f"[{'PASS' if errors == 0 else 'FAIL'}] static workflow checks: errors={errors} warnings={warnings}")
    return 1 if errors or (strict and warnings) else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate fixed story-production workflow")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="repository root to validate")
    args = parser.parse_args()
    return run(args.root.resolve(), args.strict)


if __name__ == "__main__":
    sys.exit(main())
