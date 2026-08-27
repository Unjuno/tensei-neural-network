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
            "AGENTS.md": "# agents\n",
            "WORKFLOW.md": (
                "POLICY.md\n"
                "novel/WORLD_POLICY.md\n"
                "experiments/chapters/README.md\n"
                "novel/STYLE_WEBNOVEL.md\n"
            ),
            "novel/WORLD_POLICY.md": "root POLICY.md を優先する\n",
            "novel/bootstrap/README.md": "# bootstrap\n",
            "novel/state/README.md": "# state\n",
            "novel/entities/README.md": "# entities\n",
            "novel/STYLE_WEBNOVEL.md": "# style\n",
            "experiments/README.md": "# experiments\n",
            "experiments/chapters/README.md": "# chapter verification\n",
            "novel/events/EVT-001-one.md": "# EVT-001\n",
            "novel/chapters/001-outline.md": "採用event: EVT-001\n",
            "novel/chapters/001.md": "# chapter 001\n",
            "experiments/chapters/001/README.md": "状態: PREPUBLICATION_VERIFIED\n",
            "experiments/chapters/001/terminology.md": "状態: APPLIED\n",
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
        package = root / "experiments" / "chapters" / "001" / "README.md"
        package.unlink()
        self.assertIn("WF010", self.codes(root))
        self.assertEqual(validator.run(root, strict=False), 1)

    def test_verified_chapter_with_unverified_term_fails(self) -> None:
        root = self.make_fixture()
        term = root / "experiments" / "chapters" / "001" / "terminology.md"
        term.write_text("UNVERIFIED\n", encoding="utf-8")
        self.assertIn("WF011", self.codes(root))

    def test_missing_event_reference_fails(self) -> None:
        root = self.make_fixture()
        outline = root / "novel" / "chapters" / "001-outline.md"
        outline.write_text("採用event: EVT-999\n", encoding="utf-8")
        self.assertIn("WF020", self.codes(root))

    def test_duplicate_event_id_fails(self) -> None:
        root = self.make_fixture()
        duplicate = root / "novel" / "events" / "EVT-001-two.md"
        duplicate.write_text("# duplicate\n", encoding="utf-8")
        self.assertIn("WF030", self.codes(root))

    def test_obsolete_term_reintroduction_fails(self) -> None:
        root = self.make_fixture()
        chapter = root / "novel" / "chapters" / "001.md"
        chapter.write_text("固定点《フィクスト・ポイント》\n", encoding="utf-8")
        self.assertIn("WF050", self.codes(root))


if __name__ == "__main__":
    unittest.main()
