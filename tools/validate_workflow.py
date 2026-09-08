#!/usr/bin/env python3
"""工程の構造とレビュー対象版を検査する。内容の真理・公開承認は判定しない。"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
GATE_STATE = "PREPUBLICATION_GATE_PASSED"
CANDIDATE_STATE = "GATE_CANDIDATE"
DRAFT_STATES = {"IN_PROGRESS", "NOT READY FOR PUBLICATION"}
KNOWN_STATES = DRAFT_STATES | {GATE_STATE, CANDIDATE_STATE, "PREPUBLICATION_VERIFIED"}
REQUIRED = [
    "POLICY.md", "POLICY_INDEX.md", "WORKFLOW.md", "AGENTS.md",
    "novel/WORLD_POLICY.md", "novel/bootstrap/README.md", "novel/state/README.md",
    "novel/state/LIFECYCLE.md", "novel/entities/README.md", "novel/STYLE_WEBNOVEL.md",
    "experiments/README.md", "experiments/chapters/README.md",
    "experiments/chapters/SEMANTIC_REVIEW_TEMPLATE.md",
]


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
    return path.relative_to(root).as_posix()


def add(out: list[Finding], level: str, code: str, message: str) -> None:
    out.append(Finding(level, code, message))


def unfenced(body: str) -> str:
    """コード例にある状態宣言を、文書自身の状態と取り違えない。"""
    lines, fence = [], None
    for line in body.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def chapter_status(body: str) -> str | None:
    declarations = re.findall(r"^状態:[ \t]*(.+?)[ \t]*$", unfenced(body), re.MULTILINE)
    if len(declarations) != 1:
        return None
    return declarations[0].strip().strip("`").strip()


def status_is_pass(body: str) -> bool:
    return chapter_status(body) == "PASS"


def requires_gate_checks(body: str) -> bool:
    return chapter_status(body) in {GATE_STATE, CANDIDATE_STATE}


def chapters(root: Path) -> list[str]:
    return sorted(p.stem for p in (root / "novel/chapters").glob("[0-9][0-9][0-9].md"))


def has_unverified_table_row(body: str) -> bool:
    return bool(re.search(r"^\|[^\n]*\|\s*`?(?:UNVERIFIED|REPLACE)`?\s*\|", body, re.MULTILINE))


def adopted_outline_refs(body: str) -> set[str]:
    # 正の採用欄だけを読む。見出し、同一行、改行リストを許容する。
    lines = body.splitlines()
    refs: set[str] = set()
    for index, line in enumerate(lines):
        match = re.fullmatch(r"\s*(?:#{1,6}\s+)?(?:対象event|採用event)\s*[:：]?\s*(.*?)\s*", line)
        if not match:
            continue
        payload = match.group(1)
        if payload:
            refs.update(re.findall(r"EVT-\d{3}", payload))
        for next_line in lines[index + 1:]:
            if not next_line.strip():
                if refs:
                    break
                continue
            if re.fullmatch(r"[\s`*\->,、0-9EVT]+", next_line) and "EVT-" in next_line:
                refs.update(re.findall(r"EVT-\d{3}", next_line))
            else:
                break
        break
    return refs


def event_files(root: Path) -> dict[str, Path]:
    return {p.name[:7]: p for p in (root / "novel/events").glob("EVT-[0-9][0-9][0-9]-*.md")}


def event_ids(root: Path) -> set[str]:
    return set(event_files(root))


def result_is_pass(result: object, chapter: str) -> bool:
    if not isinstance(result, dict) or result.get("chapter") != chapter or result.get("result") != "PASS":
        return False
    checks = result.get("checks")
    return isinstance(checks, dict) and bool(checks) and all(value is True for value in checks.values())


def git_blob_id(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def safe_path(root: Path, name: str) -> Path:
    posix = PurePosixPath(name)
    if not name or posix.is_absolute() or ".." in posix.parts or "\\" in name:
        raise ValueError("リポジトリ外のパス")
    path = root / name
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("リポジトリ外を指すリンク")
    return path


def review_inputs(root: Path, num: str) -> set[str]:
    package = f"experiments/chapters/{num}"
    required = {
        f"novel/chapters/{num}.md", f"novel/chapters/{num}-outline.md",
        f"{package}/verification.md", f"{package}/semantic-review.md", f"{package}/terminology.md",
        "POLICY.md", "WORKFLOW.md", "novel/WORLD_POLICY.md", "novel/STYLE_WEBNOVEL.md",
    }
    events = event_files(root)
    refs = adopted_outline_refs(text(root / f"novel/chapters/{num}-outline.md"))
    for ref in refs:
        if ref not in events:
            raise ValueError(f"未定義event: {ref}")
        required.add(rel(root, events[ref]))
    if (root / package / "run.py").exists():
        required.update({f"{package}/run.py", f"{package}/results.json"})
    return required


def record_review(root: Path, num: str, extra: Iterable[str] = ()) -> None:
    """明示的なレビュー後だけ呼ぶ。PASS化もCIでの自動更新もしない。"""
    if num not in chapters(root):
        raise ValueError("存在しない章")
    package = root / "experiments/chapters" / num
    for name in ("verification.md", "semantic-review.md"):
        if not status_is_pass(text(package / name)):
            raise ValueError(f"{name} のレビューがPASSではない")
    paths = review_inputs(root, num) | set(extra)
    lock = {"schema_version": 1, "chapter": num, "algorithm": "git-blob-sha1",
            "files": {name: git_blob_id(safe_path(root, name)) for name in sorted(paths)}}
    (package / "review-lock.json").write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def check_review_lock(root: Path, num: str, out: list[Finding]) -> None:
    path = root / "experiments/chapters" / num / "review-lock.json"
    if not path.exists():
        add(out, "ERROR", "WF080", f"第{num}話にレビュー対象版の記録がありません")
        return
    try:
        lock = json.loads(text(path))
        if not isinstance(lock, dict) or lock.get("schema_version") != 1 or lock.get("chapter") != num or lock.get("algorithm") != "git-blob-sha1":
            raise ValueError("review-lockのschema不正")
        files = lock.get("files")
        if not isinstance(files, dict) or not review_inputs(root, num).issubset(files):
            raise ValueError("必須の依存ファイルが未記録")
        for name, expected in files.items():
            if not isinstance(name, str) or not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{40}", expected):
                raise ValueError("パスまたはblob IDが不正")
            if git_blob_id(safe_path(root, name)) != expected:
                add(out, "ERROR", "WF081", f"第{num}話は再レビューが必要: {name}")
    except (ValueError, OSError, TypeError) as exc:
        add(out, "ERROR", "WF082", f"第{num}話のreview-lock不正: {exc}")


def require_files(root: Path, out: list[Finding]) -> None:
    for name in REQUIRED:
        if not (root / name).is_file():
            add(out, "ERROR", "WF001", f"必須ファイルがありません: {name}")


def check_chapter_packages(root: Path, out: list[Finding]) -> None:
    for num in chapters(root):
        package = root / "experiments/chapters" / num
        if not (package / "README.md").exists():
            add(out, "ERROR", "WF010", f"第{num}話の検証packageがありません")
            continue
        if not (package / "verification.md").exists():
            add(out, "ERROR", "WF013", f"第{num}話のverification.mdがありません")
        if not requires_gate_checks(text(package / "README.md")):
            continue
        if not status_is_pass(text(package / "verification.md")):
            add(out, "ERROR", "WF014", f"第{num}話の検証がPASSではありません")
        if not (package / "semantic-review.md").exists():
            add(out, "ERROR", "WF018", f"第{num}話のsemantic reviewがありません")
        elif not status_is_pass(text(package / "semantic-review.md")):
            add(out, "ERROR", "WF019", f"第{num}話のsemantic reviewがPASSではありません")
        if not (package / "terminology.md").exists():
            add(out, "WARN", "WF012", f"第{num}話の用語検証記録がありません")
        elif has_unverified_table_row(text(package / "terminology.md")):
            add(out, "ERROR", "WF011", f"第{num}話に未検証・未置換用語があります")
        if (package / "run.py").exists():
            rp = package / "results.json"
            if not rp.exists():
                add(out, "ERROR", "WF015", f"第{num}話の実行結果がありません")
            else:
                try:
                    result = json.loads(text(rp))
                except ValueError:
                    add(out, "ERROR", "WF016", f"第{num}話の結果JSONが不正です")
                else:
                    if not result_is_pass(result, num):
                        add(out, "ERROR", "WF017", f"第{num}話のresult/checks/chapterが不整合です")
        check_review_lock(root, num, out)


def check_outline_refs(root: Path, out: list[Finding]) -> None:
    events = event_files(root)
    for num in chapters(root):
        outline = root / f"novel/chapters/{num}-outline.md"
        if not outline.exists():
            add(out, "ERROR", "WF023", f"第{num}話のoutlineがありません")
            continue
        refs = adopted_outline_refs(text(outline))
        if not refs:
            add(out, "WARN", "WF021", f"第{num}話の採用EVTが空です")
        for ref in refs:
            if ref not in events:
                add(out, "ERROR", "WF020", f"第{num}話の未定義EVT: {ref}")
            elif "ACTION_LOCKED" in (chapter_status(text(events[ref])) or ""):
                add(out, "ERROR", "WF024", f"第{num}話は未解決EVTを採用: {ref}")


def duplicate_numbers(paths: Iterable[Path], pattern: re.Pattern[str]) -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {}
    for path in paths:
        match = pattern.match(path.name)
        if match:
            found.setdefault(match.group(1), []).append(path)
    return {key: value for key, value in found.items() if len(value) > 1}


def check_duplicate_ids(root: Path, out: list[Finding]) -> None:
    for prefix, directory, dirs in [("EVT", "novel/events", False), ("PER", "novel/personas", False),
                                    ("ORG", "novel/organizations", False), ("BOOT", "novel/bootstrap", False), ("EXP", "experiments", True)]:
        folder = root / directory
        if folder.exists():
            items = [p for p in folder.iterdir() if p.is_dir() == dirs]
            for key in duplicate_numbers(items, re.compile(rf"({prefix}-\d{{3}})-.*" + (r"$" if dirs else r"\.md$"))):
                add(out, "ERROR", "WF030", f"重複ID: {key}")


def check_policy_links(root: Path, out: list[Finding]) -> None:
    for name in ["POLICY.md", "novel/WORLD_POLICY.md", "novel/state/LIFECYCLE.md", "experiments/chapters/README.md", "novel/STYLE_WEBNOVEL.md"]:
        if name not in text(root / "WORKFLOW.md"):
            add(out, "ERROR", "WF040", f"WORKFLOW.mdの参照欠落: {name}")
    if "POLICY.md" not in text(root / "novel/WORLD_POLICY.md"):
        add(out, "ERROR", "WF041", "WORLD_POLICY.mdの上位参照欠落")


def check_obsolete_chapter_terms(root: Path, out: list[Finding]) -> None:
    for term in ["《ローカル・フィールド》", "《フィクスト・ポイント》", "《アシンクロナス・アップデート》"]:
        if term in text(root / "novel/chapters/001.md"):
            add(out, "ERROR", "WF050", f"第001話の廃止表記: {term}")


def check_chapter_status(root: Path, out: list[Finding]) -> None:
    for num in chapters(root):
        status = chapter_status(text(root / "experiments/chapters" / num / "README.md"))
        if status not in KNOWN_STATES:
            add(out, "ERROR", "WF062", f"第{num}話の状態が欠落・重複・未定義です")
        elif status in DRAFT_STATES:
            add(out, "WARN", "WF060", f"第{num}話は未完了。公開不可")
        elif status == "PREPUBLICATION_VERIFIED":
            add(out, "WARN", "WF061", f"第{num}話は旧gate名です")


def check_global_glossary(root: Path, out: list[Finding]) -> None:
    for name in ("GLOSSARY.md", "novel/GLOSSARY.md"):
        if (root / name).exists():
            add(out, "WARN", "WF070", f"話別用語検証との分離を確認: {name}")


CHECKS = [require_files, check_chapter_packages, check_outline_refs, check_duplicate_ids,
          check_policy_links, check_obsolete_chapter_terms, check_chapter_status, check_global_glossary]


def collect_findings(root: Path) -> list[Finding]:
    out: list[Finding] = []
    for check in CHECKS:
        check(root, out)
    return out


def run(root: Path, strict: bool = False, allow_drafts: bool = False) -> int:
    findings = collect_findings(root)
    for finding in findings:
        print(f"[{finding.level}] {finding.code} {finding.message}")
    errors = sum(f.level == "ERROR" for f in findings)
    warnings = sum(f.level == "WARN" and not (allow_drafts and f.code == "WF060") for f in findings)
    failed = errors > 0 or (strict and warnings > 0)
    print(f"[{'FAIL' if failed else 'PASS'}] 工程検査 errors={errors} blocking_warnings={warnings}; 公開承認ではありません")
    return int(failed)


def validate(root: Path, strict: bool = False) -> int:
    return run(root, strict)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-drafts", action="store_true", help="開発CI専用。WF060だけを非blockingにする")
    parser.add_argument("--record-review", metavar="NNN", help="明示的レビュー後に対象版を記録。状態は昇格しない")
    parser.add_argument("--evidence", nargs="*", default=[])
    args = parser.parse_args()
    try:
        if args.record_review:
            record_review(args.root.resolve(), args.record_review, args.evidence)
            return 0
        return run(args.root.resolve(), args.strict, args.allow_drafts)
    except (ValueError, OSError, UnicodeError) as exc:
        print(f"[FAIL] {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
