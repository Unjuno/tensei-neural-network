#!/usr/bin/env python3
"""Static validator for the fixed story-production workflow."""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
GATE_STATE = "PREPUBLICATION_GATE_PASSED"
CANDIDATE_STATE = "GATE_CANDIDATE"


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
    d = root / "novel/chapters"
    return sorted({p.stem for p in d.glob("[0-9][0-9][0-9].md")}) if d.exists() else []


def require_files(root: Path, out: list[Finding]) -> None:
    required = [
        "POLICY.md", "POLICY_INDEX.md", "WORKFLOW.md", "AGENTS.md",
        "novel/WORLD_POLICY.md", "novel/bootstrap/README.md",
        "novel/state/README.md", "novel/state/LIFECYCLE.md",
        "novel/entities/README.md", "novel/STYLE_WEBNOVEL.md",
        "experiments/README.md", "experiments/chapters/README.md",
        "experiments/chapters/SEMANTIC_REVIEW_TEMPLATE.md",
    ]
    for name in required:
        if not (root / name).exists():
            add(out, "ERROR", "WF001", f"必須ファイルがありません: {name}")


def has_unverified_table_row(body: str) -> bool:
    return bool(re.search(r"^\|[^\n]*\|\s*UNVERIFIED\s*\|[^\n]*$", body, re.MULTILINE))


def status_is_pass(body: str) -> bool:
    return bool(re.search(r"^状態:\s*`?PASS`?\s*$", body, re.MULTILINE))


def chapter_status(body: str) -> str | None:
    m = re.search(r"^状態:\s*`?([^`\n]+)`?\s*$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


def requires_gate_checks(body: str) -> bool:
    return chapter_status(body) in {CANDIDATE_STATE, GATE_STATE}


def check_chapter_packages(root: Path, out: list[Finding]) -> None:
    for num in chapters(root):
        package = root / "experiments/chapters" / num
        readme = package / "README.md"
        verification = package / "verification.md"
        semantic = package / "semantic-review.md"

        if not readme.exists():
            add(out, "ERROR", "WF010", f"第{num}話に話別検証packageがありません: {rel(root, readme)}")
            continue
        if not verification.exists():
            add(out, "ERROR", "WF013", f"第{num}話に必須のverification.mdがありません")

        body = text(readme)
        status = chapter_status(body)
        if requires_gate_checks(body):
            state_label = status or "gate target"
            if not verification.exists() or not status_is_pass(text(verification)):
                add(out, "ERROR", "WF014", f"第{num}話は{state_label}だがMandatory VerificationがPASSではありません")

            if not semantic.exists():
                add(out, "ERROR", "WF018", f"第{num}話は{state_label}だがsemantic-review.mdがありません")
            elif not status_is_pass(text(semantic)):
                add(out, "ERROR", "WF019", f"第{num}話は{state_label}だがsemantic reviewがPASSではありません")

            term = package / "terminology.md"
            if term.exists() and has_unverified_table_row(text(term)):
                add(out, "ERROR", "WF011", f"第{num}話は{state_label}だが未検証用語が残っています")
            elif not term.exists():
                add(out, "WARN", "WF012", f"第{num}話は{state_label}だがterminology.mdがありません。用語が無い話なら許容")

            run_py = package / "run.py"
            if run_py.exists():
                result_path = package / "results.json"
                if not result_path.exists():
                    add(out, "ERROR", "WF015", f"第{num}話はrun.pyを持つがresults.jsonがありません")
                else:
                    try:
                        result = json.loads(text(result_path))
                    except json.JSONDecodeError:
                        add(out, "ERROR", "WF016", f"第{num}話のresults.jsonが有効なJSONではありません")
                    else:
                        if result.get("result") != "PASS":
                            add(out, "ERROR", "WF017", f"第{num}話の保存済み実行結果がPASSではありません")


def event_ids(root: Path) -> set[str]:
    d = root / "novel/events"
    ids: set[str] = set()
    if d.exists():
        for p in d.glob("EVT-[0-9][0-9][0-9]-*.md"):
            m = re.match(r"(EVT-\d{3})-", p.name)
            if m:
                ids.add(m.group(1))
    return ids


def adopted_outline_refs(body: str) -> set[str]:
    m = re.search(r"(?:対象event|採用event):\s*\n\n([^\n]+)", body)
    return set(re.findall(r"EVT-\d{3}", m.group(1))) if m else set()


def check_outline_refs(root: Path, out: list[Finding]) -> None:
    known = event_ids(root)
    d = root / "novel/chapters"
    if not d.exists():
        return
    for outline in d.glob("[0-9][0-9][0-9]-outline.md"):
        refs = adopted_outline_refs(text(outline))
        for missing in sorted(refs - known):
            add(out, "ERROR", "WF020", f"{rel(root, outline)} が存在しない採用eventを参照しています: {missing}")
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
    for name in ["POLICY.md", "novel/WORLD_POLICY.md", "novel/state/LIFECYCLE.md", "experiments/chapters/README.md", "novel/STYLE_WEBNOVEL.md"]:
        if name not in workflow:
            add(out, "ERROR", "WF040", f"WORKFLOW.md が {name} を参照していません")
    if "POLICY.md" not in text(root / "novel/WORLD_POLICY.md"):
        add(out, "ERROR", "WF041", "WORLD_POLICY.md が上位 POLICY.md を参照していません")


def check_obsolete_chapter_terms(root: Path, out: list[Finding]) -> None:
    for term in ["《ローカル・フィールド》", "《フィクスト・ポイント》", "《アシンクロナス・アップデート》"]:
        if term in text(root / "novel/chapters/001.md"):
            add(out, "ERROR", "WF050", f"第001話に廃止した表記が再混入しています: {term}")


def check_chapter_status(root: Path, out: list[Finding]) -> None:
    for num in chapters(root):
        body = text(root / "experiments/chapters" / num / "README.md")
        status = chapter_status(body)
        if status in {"IN_PROGRESS", "NOT READY FOR PUBLICATION"}:
            add(out, "WARN", "WF060", f"第{num}話はまだ公開前gate未完了です")
        if status == "PREPUBLICATION_VERIFIED":
            add(out, "WARN", "WF061", f"第{num}話は旧gate名 PREPUBLICATION_VERIFIED を使っています")


def check_global_glossary(root: Path, out: list[Finding]) -> None:
    for p in [root / "GLOSSARY.md", root / "novel/GLOSSARY.md"]:
        if p.exists():
            add(out, "WARN", "WF070", f"global glossary候補があります。章別検証から先回りしていないか確認: {rel(root, p)}")


CHECKS = [
    require_files,
    check_chapter_packages,
    check_outline_refs,
    check_duplicate_ids,
    check_policy_links,
    check_obsolete_chapter_terms,
    check_chapter_status,
    check_global_glossary,
]


def collect_findings(root: Path) -> list[Finding]:
    out: list[Finding] = []
    for fn in CHECKS:
        fn(root, out)
    return out


def run(root: Path, strict: bool = False) -> int:
    out = collect_findings(root)
    errors = sum(x.level == "ERROR" for x in out)
    warnings = sum(x.level == "WARN" for x in out)
    for x in out:
        print(f"[{x.level}] {x.code} {x.message}")
    if errors or (strict and warnings):
        print(f"[FAIL] static workflow checks: errors={errors} warnings={warnings}")
        return 1
    print(f"[PASS] static workflow checks: errors={errors} warnings={warnings}")
    return 0


def validate(root: Path, strict: bool = False) -> int:
    return run(root, strict)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    return run(args.root.resolve(), args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
