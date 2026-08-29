from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import validate_workflow as validator


class WorkflowValidatorTest(unittest.TestCase):
    def make_fixture(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)

        files = {
            "POLICY.md": "# policy\n",
            "POLICY_INDEX.md": "# policy index\n",
            "AGENTS.md": "# agents\n",
            "WORKFLOW.md": (
                "POLICY.md\n"
                "novel/WORLD_POLICY.md\n"
                "novel/state/LIFECYCLE.md\n"
                "experiments/chapters/README.md\n"
                "novel/STYLE_WEBNOVEL.md\n"
            ),
            "novel/WORLD_POLICY.md": "root POLICY.md を優先する\n",
            "novel/bootstrap/README.md": "# bootstrap\n",
            "novel/state/README.md": "# state\n",
            "novel/state/LIFECYCLE.md": "# lifecycle\n",
            "novel/entities/README.md": "# entities\n",
            "novel/STYLE_WEBNOVEL.md": "# style\n",
            "experiments/README.md": "# experiments\n",
            "experiments/chapters/README.md": "# chapter verification\n",
            "experiments/chapters/SEMANTIC_REVIEW_TEMPLATE.md": "# template\n",
            "novel/events/EVT-001-one.md": "# EVT-001\n",
            "novel/chapters/001-outline.md": "採用event: EVT-001\n",
            "novel/chapters/001.md": "# chapter 001\n",
            "experiments/chapters/001/README.md": "状態: PREPUBLICATION_GATE_PASSED\n",
            "experiments/chapters/001/verification.md": "状態: `PASS`\n",
            "experiments/chapters/001/semantic-review.md": "状態: `PASS`\n",
            "experiments/chapters/001/terminology.md": (
                "- `UNVERIFIED`: 候補表記。\n"
                "| 原概念 | 表記 | 人物発話 | 状態 | 根拠 |\n"
                "|---|---|---|---|---|\n"
                "| recall | 想起 | 使用可 | APPLIED | source |\n"
            ),
        }
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def codes(self, root: Path) -> set[str]:
        return {f.code for f in validator.collect_findings(root)}

    def test_valid_fixture_passes_strict(self) -> None:
        root = self.make_fixture()
        self.assertEqual(validator.run(root, strict=True), 0)

    def test_missing_chapter_package_fails(self) -> None:
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").unlink()
        self.assertIn("WF010", self.codes(root))

    def test_missing_mandatory_verification_fails(self) -> None:
        root = self.make_fixture()
        (root / "experiments/chapters/001/verification.md").unlink()
        self.assertIn("WF013", self.codes(root))

    def test_gate_requires_pass_verification(self) -> None:
        root = self.make_fixture()
        p = root / "experiments/chapters/001/verification.md"
        p.write_text("状態: `FAIL`\n", encoding="utf-8")
        self.assertIn("WF014", self.codes(root))

    def test_gate_requires_semantic_review(self) -> None:
        root = self.make_fixture()
        (root / "experiments/chapters/001/semantic-review.md").unlink()
        self.assertIn("WF018", self.codes(root))

    def test_gate_requires_pass_semantic_review(self) -> None:
        root = self.make_fixture()
        p = root / "experiments/chapters/001/semantic-review.md"
        p.write_text("状態: `UNCERTAIN`\n", encoding="utf-8")
        self.assertIn("WF019", self.codes(root))

    def test_legend_word_unverified_is_not_false_positive(self) -> None:
        root = self.make_fixture()
        self.assertNotIn("WF011", self.codes(root))

    def test_unverified_table_row_fails_gate(self) -> None:
        root = self.make_fixture()
        p = root / "experiments/chapters/001/terminology.md"
        p.write_text(
            "| 原概念 | 表記 | 人物発話 | 状態 | 根拠 |\n"
            "|---|---|---|---|---|\n"
            "| term | 候補 | 未確認 | UNVERIFIED | none |\n",
            encoding="utf-8",
        )
        self.assertIn("WF011", self.codes(root))

    def test_missing_event_reference_fails(self) -> None:
        root = self.make_fixture()
        p = root / "novel/chapters/001-outline.md"
        p.write_text("採用event: EVT-999\n", encoding="utf-8")
        self.assertIn("WF020", self.codes(root))

    def test_duplicate_event_id_fails(self) -> None:
        root = self.make_fixture()
        p = root / "novel/events/EVT-001-two.md"
        p.write_text("# duplicate\n", encoding="utf-8")
        self.assertIn("WF030", self.codes(root))

    def test_old_gate_name_warns(self) -> None:
        root = self.make_fixture()
        p = root / "experiments/chapters/001/README.md"
        p.write_text("状態: PREPUBLICATION_VERIFIED\n", encoding="utf-8")
        self.assertIn("WF061", self.codes(root))

    def test_obsolete_term_reintroduction_fails(self) -> None:
        root = self.make_fixture()
        p = root / "novel/chapters/001.md"
        p.write_text("固定点《フィクスト・ポイント》\n", encoding="utf-8")
        self.assertIn("WF050", self.codes(root))


if __name__ == "__main__":
    unittest.main()
