#!/usr/bin/env python3
"""Static workflow validator for the story-generation repository.

This script deliberately checks structure and traceability only.
It does not try to prove historical, scientific, or narrative correctness.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Finding:
    level: str
    code: str
    message: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def add(findings: list[Finding], level: str, code: str, message: str) -> None:
    findings.append(Finding(level, code, message))


def require_files(findings: list[Finding]) -> None:
    required = [
        "POLICY.md",
        "WORKFLOW.md",
        "AGENTS.md",
        "novel/WORLD_POLICY.md",
        "novel/bootstrap/README.md",
        "novel/state/README.md",
        "novel/entities/README.md",
        "novel/STYLE_WEBNOVEL.md",
        "experiments/README.md",
        "experiments/chapters/README.md",
    ]
    for name in required:
        p = ROOT / name
        if not p.exists():
            add(findings, "ERROR", "WF001", f"必須ファイルがありません: {name}")


def chapter_numbers() -> list[str]:
    chapter_dir = ROOT / "novel" / "chapters"
    if not chapter_dir.exists():
        return []
    out: list[str] = []
    for p in chapter_dir.glob("[0-9][0-9][0-9].md"):
        out.append(p.stem)
    return sorted(set(out))


def check_chapter_packages(findings: list[Finding]) -> None:
    for num in chapter_numbers():
        package = ROOT / "experiments" / "chapters" / num
        readme = package / "README.md"
        if not readme.exists():
            add(
                findings,
                "ERROR",
                "WF010",
                f"第{num}話に話別検証packageがありません: {rel(readme)}",
            )
            continue

        package_text = read_text(readme)
        if "PREPUBLICATION_VERIFIED" in package_text:
            term = package / "terminology.md"
            if term.exists():
                term_text = read_text(term)
                if "UNVERIFIED" in term_text:
                    add(
                        findings,
                        "ERROR",
                        "WF011",
                        f"第{num}話はPREPUBLICATION_VERIFIEDだが未検証用語が残っています",
                    )
            else:
                add(
                    findings,
                    "WARN",
                    "WF012",
                    f"第{num}話はPREPUBLICATION_VERIFIEDだがterminology.mdがありません。用語が無い話なら許容",
                )


def existing_event_ids() -> set[str]:
    events = ROOT / "novel" / "events"
    ids: set[str] = set()
    if not events.exists():
        return ids
    for p in events.glob("EVT-[0-9][0-9][0-9]-*.md"):
        m = re.match(r"(EVT-\d{3})-", p.name)
        if m:
            ids.add(m.group(1))
    return ids


def check_outline_event_refs(findings: list[Finding]) -> None:
    known = existing_event_ids()
    for outline in (ROOT / "novel" / "chapters").glob("[0-9][0-9][0-9]-outline.md"):
        text = read_text(outline)
        refs = set(re.findall(r"EVT-\d{3}", text))
        missing = sorted(refs - known)
        for event_id in missing:
            add(
                findings,
                "ERROR",
                "WF020",
                f"{rel(outline)} が存在しないeventを参照しています: {event_id}",
            )
        if not refs:
            add(
                findings,
                "WARN",
                "WF021",
                f"{rel(outline)} に採用EVT参照がありません",
            )


def duplicate_numbers(paths: Iterable[Path], pattern: re.Pattern[str]) -> dict[str, list[Path]]:
    by_id: dict[str, list[Path]] = {}
    for p in paths:
        m = pattern.match(p.name)
        if m:
            by_id.setdefault(m.group(1), []).append(p)
    return {k: v for k, v in by_id.items() if len(v) > 1}


def check_definition_id_duplicates(findings: list[Finding]) -> None:
    checks: list[tuple[str, Path, str, bool]] = [
        ("EVT", ROOT / "novel" / "events", r"(EVT-\d{3})-.*\.md$", False),
        ("PER", ROOT / "novel" / "personas", r"(PER-\d{3})-.*\.md$", False),
        ("ORG", ROOT / "novel" / "organizations", r"(ORG-\d{3})-.*\.md$", False),
        ("BOOT", ROOT / "novel" / "bootstrap", r"(BOOT-\d{3})-.*\.md$", False),
        ("EXP", ROOT / "experiments", r"(EXP-\d{3})-.*$", True),
    ]
    for label, directory, regex, dirs_only in checks:
        if not directory.exists():
            continue
        items = [p for p in directory.iterdir() if p.is_dir() == dirs_only]
        dups = duplicate_numbers(items, re.compile(regex))
        for stable_id, files in sorted(dups.items()):
            add(
                findings,
                "ERROR",
                "WF030",
                f"{label}定義番号が重複しています {stable_id}: " + ", ".join(rel(p) for p in files),
            )


def check_policy_links(findings: list[Finding]) -> None:
    workflow = read_text(ROOT / "WORKFLOW.md")
    required_refs = [
        "POLICY.md",
        "novel/WORLD_POLICY.md",
        "experiments/chapters/README.md",
        "novel/STYLE_WEBNOVEL.md",
    ]
    for ref_name in required_refs:
        if ref_name not in workflow:
            add(findings, "ERROR", "WF040", f"WORKFLOW.mdにpolicy参照がありません: {ref_name}")

    world_policy = read_text(ROOT / "novel" / "WORLD_POLICY.md")
    if "POLICY.md" not in world_policy:
        add(findings, "ERROR", "WF041", "WORLD_POLICY.mdがroot POLICY.mdの優先を明示していません")


def check_obsolete_chapter_terms(findings: list[Finding]) -> None:
    # Terms intentionally removed from chapter 001 after historical terminology verification.
    banned = {
        "《ローカル・フィールド》": "局所場の英語ルビ",
        "《フィクスト・ポイント》": "固定点の英語ルビ",
        "《アシンクロナス・アップデート》": "非同期更新の英語ルビ",
    }
    chapter = ROOT / "novel" / "chapters" / "001.md"
    text = read_text(chapter)
    for token, label in banned.items():
        if token in text:
            add(
                findings,
                "ERROR",
                "WF050",
                f"第1話に検証後廃止した表記が再混入しています: {label} {token}",
            )


def check_chapter_verification_status(findings: list[Finding]) -> None:
    for num in chapter_numbers():
        readme = ROOT / "experiments" / "chapters" / num / "README.md"
        text = read_text(readme)
        if not text:
            continue
        if "NOT READY FOR PUBLICATION" in text or "IN_PROGRESS" in text:
            add(
                findings,
                "WARN",
                "WF060",
                f"第{num}話はまだ公開前検証未完了です",
            )


def check_global_glossary(findings: list[Finding]) -> None:
    # Current policy intentionally keeps terminology in chapter verification packages.
    for name in ("GLOSSARY.md", "novel/GLOSSARY.md"):
        if (ROOT / name).exists():
            add(
                findings,
                "WARN",
                "WF070",
                f"全体Glossaryが存在します。現行方針では話別terminologyを優先してください: {name}",
            )


def run(strict: bool) -> int:
    findings: list[Finding] = []
    require_files(findings)
    check_chapter_packages(findings)
    check_outline_event_refs(findings)
    check_definition_id_duplicates(findings)
    check_policy_links(findings)
    check_obsolete_chapter_terms(findings)
    check_chapter_verification_status(findings)
    check_global_glossary(findings)

    order = {"ERROR": 0, "WARN": 1}
    findings.sort(key=lambda x: (order.get(x.level, 9), x.code, x.message))

    for f in findings:
        print(f"[{f.level}] {f.code} {f.message}")

    errors = sum(1 for f in findings if f.level == "ERROR")
    warnings = sum(1 for f in findings if f.level == "WARN")

    if errors == 0:
        print(f"[PASS] static workflow checks: errors=0 warnings={warnings}")
    else:
        print(f"[FAIL] static workflow checks: errors={errors} warnings={warnings}")

    if errors:
        return 1
    if strict and warnings:
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate fixed story-production workflow")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat warnings as failures",
    )
    args = parser.parse_args()
    return run(strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
