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
        files = {name: "# fixture\n" for name in validator.REQUIRED}
        files.update({
            "WORKFLOW.md": "POLICY.md\nnovel/WORLD_POLICY.md\nnovel/state/LIFECYCLE.md\nexperiments/chapters/README.md\nnovel/STYLE_WEBNOVEL.md\n",
            "novel/WORLD_POLICY.md": "root POLICY.md を優先する\n",
            "novel/events/EVT-001-one.md": "# EVT-001\n状態: RESOLVED / PROVISIONAL\n",
            "novel/chapters/001-outline.md": "採用event:\n\nEVT-001\n\n禁止: EVT-999以降を使わない\n",
            "novel/chapters/001.md": "# chapter 001\n",
            "experiments/chapters/001/README.md": "状態: PREPUBLICATION_GATE_PASSED\n",
            "experiments/chapters/001/verification.md": "状態: `PASS`\n",
            "experiments/chapters/001/semantic-review.md": "状態: `PASS`\n",
            "experiments/chapters/001/terminology.md": "- `UNVERIFIED`: 候補表記。\n| 原概念 | 表記 | 人物発話 | 状態 | 根拠 |\n|---|---|---|---|---|\n| recall | 想起 | 使用可 | APPLIED | source |\n",
        })
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        validator.record_review(root, "001")
        return root

    def codes(self, root: Path) -> set[str]:
        return {f.code for f in validator.collect_findings(root)}

    def test_valid_fixture_passes_strict(self):
        self.assertEqual(validator.run(self.make_fixture(), strict=True), 0)

    def test_gate_candidate_passes_strict_when_ready(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").write_text("状態: GATE_CANDIDATE\n")
        self.assertEqual(validator.run(root, strict=True), 0)

    def test_gate_candidate_uses_full_gate_checks(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").write_text("状態: GATE_CANDIDATE\n")
        (root / "experiments/chapters/001/semantic-review.md").write_text("状態: FAIL\n")
        self.assertIn("WF019", self.codes(root))

    def test_in_progress_still_fails_strict(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").write_text("状態: IN_PROGRESS\n")
        self.assertIn("WF060", self.codes(root))
        self.assertEqual(validator.run(root, strict=True), 1)

    def test_missing_chapter_package_fails(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").unlink()
        self.assertIn("WF010", self.codes(root))

    def test_missing_mandatory_verification_fails(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/verification.md").unlink()
        self.assertIn("WF013", self.codes(root))

    def test_gate_requires_pass_verification(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/verification.md").write_text("状態: FAIL\n")
        self.assertIn("WF014", self.codes(root))

    def test_gate_requires_semantic_review(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/semantic-review.md").unlink()
        self.assertIn("WF018", self.codes(root))

    def test_gate_requires_pass_semantic_review(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/semantic-review.md").write_text("状態: UNCERTAIN\n")
        self.assertIn("WF019", self.codes(root))

    def test_legend_word_unverified_is_not_false_positive(self):
        self.assertNotIn("WF011", self.codes(self.make_fixture()))

    def test_unverified_table_row_fails_gate(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/terminology.md").write_text("| term | 候補 | 未確認 | UNVERIFIED | none |\n")
        self.assertIn("WF011", self.codes(root))

    def test_missing_event_reference_fails(self):
        root = self.make_fixture()
        (root / "novel/chapters/001-outline.md").write_text("採用event:\n\nEVT-999\n")
        self.assertIn("WF020", self.codes(root))

    def test_forbidden_future_event_is_not_dependency(self):
        self.assertNotIn("WF020", self.codes(self.make_fixture()))

    def test_duplicate_event_id_fails(self):
        root = self.make_fixture()
        (root / "novel/events/EVT-001-two.md").write_text("# duplicate\n")
        self.assertIn("WF030", self.codes(root))

    def test_old_gate_name_warns(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").write_text("状態: PREPUBLICATION_VERIFIED\n")
        self.assertIn("WF061", self.codes(root))

    def test_obsolete_term_reintroduction_fails(self):
        root = self.make_fixture()
        (root / "novel/chapters/001.md").write_text("《フィクスト・ポイント》\n")
        self.assertIn("WF050", self.codes(root))


if __name__ == "__main__":
    unittest.main()
