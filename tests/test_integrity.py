from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
import test_validate_workflow as fixtures
from tools import validate_workflow as validator
from tools import run_chapter_experiments as runner


class IntegrityGuardTest(unittest.TestCase):
    def make_fixture(self):
        helper = fixtures.WorkflowValidatorTest()
        self.addCleanup(helper.doCleanups)
        return helper.make_fixture()

    def codes(self, root):
        return {item.code for item in validator.collect_findings(root)}

    def test_unknown_missing_duplicate_status_fail_closed(self):
        for body in ("", "状態: PASSED\n", "状態: GATE_CANDIDATE\n状態: IN_PROGRESS\n", "```\n状態: GATE_CANDIDATE\n```\n"):
            with self.subTest(body=body):
                root = self.make_fixture()
                (root / "experiments/chapters/001/README.md").write_text(body)
                self.assertIn("WF062", self.codes(root))

    def test_status_example_does_not_override_draft(self):
        body = "状態: IN_PROGRESS\n```\n状態: GATE_CANDIDATE\n```\n"
        self.assertEqual(validator.chapter_status(body), "IN_PROGRESS")

    def test_conflicting_review_status_is_not_pass(self):
        self.assertFalse(validator.status_is_pass("状態: FAIL\n状態: PASS\n"))

    def test_allow_drafts_is_not_publication(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/README.md").write_text("状態: IN_PROGRESS\n")
        self.assertEqual(validator.run(root, strict=True, allow_drafts=True), 0)
        self.assertEqual(validator.run(root, strict=True), 1)
        (root / "experiments/chapters/001/verification.md").unlink()
        self.assertEqual(validator.run(root, strict=True, allow_drafts=True), 1)

    def test_missing_outline_cannot_be_skipped(self):
        root = self.make_fixture()
        (root / "novel/chapters/001-outline.md").unlink()
        self.assertIn("WF023", self.codes(root))

    def test_inline_heading_and_multiline_adoption(self):
        for body in ("採用event: EVT-001\n禁止: EVT-999\n", "## 採用event\n\n`EVT-001`\n\n## 禁止\nEVT-999\n", "採用event:\n- EVT-001\n- EVT-002\n\n禁止: EVT-999\n"):
            with self.subTest(body=body):
                refs = validator.adopted_outline_refs(body)
                self.assertIn("EVT-001", refs)
                self.assertNotIn("EVT-999", refs)

    def test_action_locked_event_is_not_adoptable(self):
        root = self.make_fixture()
        (root / "novel/events/EVT-001-one.md").write_text("# event\n状態: ACTION_LOCKED / PROVISIONAL\n")
        self.assertIn("WF024", self.codes(root))

    def test_auxiliary_csv_is_not_duplicate_event(self):
        root = self.make_fixture()
        (root / "novel/events/EVT-001-results.csv").write_text("result\n")
        self.assertNotIn("WF030", self.codes(root))

    def test_body_code_review_and_evidence_edits_invalidate_review(self):
        for name in ("novel/chapters/001.md", "novel/events/EVT-001-one.md", "experiments/chapters/001/semantic-review.md", "POLICY.md"):
            with self.subTest(name=name):
                root = self.make_fixture()
                path = root / name
                path.write_text(path.read_text() + "changed\n")
                self.assertIn("WF081", self.codes(root))

    def test_missing_lock_blocks_candidate(self):
        root = self.make_fixture()
        (root / "experiments/chapters/001/review-lock.json").unlink()
        self.assertIn("WF080", self.codes(root))

    def test_omitted_dependency_rejected(self):
        root = self.make_fixture()
        path = root / "experiments/chapters/001/review-lock.json"
        lock = json.loads(path.read_text())
        del lock["files"]["novel/chapters/001.md"]
        path.write_text(json.dumps(lock))
        self.assertIn("WF082", self.codes(root))

    def test_unsafe_path_rejected(self):
        root = self.make_fixture()
        path = root / "experiments/chapters/001/review-lock.json"
        lock = json.loads(path.read_text())
        lock["files"]["../outside.txt"] = "0" * 40
        path.write_text(json.dumps(lock))
        self.assertIn("WF082", self.codes(root))

    def test_malformed_json_schema_rejected(self):
        for payload in ([], None, {"schema_version": 1, "files": []}):
            root = self.make_fixture()
            (root / "experiments/chapters/001/review-lock.json").write_text(json.dumps(payload))
            self.assertIn("WF082", self.codes(root))

    def test_result_must_have_true_checks_and_matching_chapter(self):
        for payload in ([], None, {"chapter": "001", "result": "PASS"}, {"chapter": "002", "result": "PASS", "checks": {"x": True}}, {"chapter": "001", "result": "PASS", "checks": {}}, {"chapter": "001", "result": "PASS", "checks": {"x": False}}, {"chapter": "001", "result": "PASS", "checks": {"x": 1}}):
            with self.subTest(payload=payload):
                self.assertFalse(validator.result_is_pass(payload, "001"))


class RunnerGuardTest(unittest.TestCase):
    def fixture(self, fresh=None, saved=None, code=None):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        package = root / "experiments/chapters/001"
        package.mkdir(parents=True)
        good = {"chapter": "001", "result": "PASS", "checks": {"x": True}, "value": 5}
        fresh = good if fresh is None else fresh
        saved = good if saved is None else saved
        (package / "results.json").write_text(json.dumps(saved))
        (package / "run.py").write_text(code or ("print(" + repr(json.dumps(fresh)) + ")\n"))
        return root, package

    def test_equal_result_passes(self):
        root, package = self.fixture()
        self.assertEqual(runner.verify_one(root, package), [])

    def test_stale_result_fails_even_with_pass_tag(self):
        root, package = self.fixture(fresh={"chapter": "001", "result": "PASS", "checks": {"x": True}, "value": 6})
        self.assertTrue(runner.verify_one(root, package))

    def test_exit_zero_without_evidence_fails(self):
        root, package = self.fixture(code="pass\n")
        self.assertTrue(runner.verify_one(root, package))

    def test_false_check_with_pass_tag_fails(self):
        root, package = self.fixture(fresh={"chapter": "001", "result": "PASS", "checks": {"x": False}})
        self.assertTrue(runner.verify_one(root, package))

    def test_nonzero_exit_fails(self):
        root, package = self.fixture(code="raise SystemExit(2)\n")
        self.assertTrue(runner.verify_one(root, package))

    def test_saved_array_fails_without_crash(self):
        root, package = self.fixture(saved=[])
        self.assertTrue(runner.verify_one(root, package))

    def test_missing_saved_result_fails(self):
        root, package = self.fixture()
        (package / "results.json").unlink()
        self.assertTrue(runner.verify_one(root, package))

    def test_timeout_fails(self):
        root, package = self.fixture(code="import time\ntime.sleep(1)\n")
        self.assertTrue(runner.verify_one(root, package, timeout=0.01))

    def test_check_must_not_overwrite_saved_results(self):
        root, package = self.fixture(code="from pathlib import Path\nPath(__file__).with_name('results.json').write_text('{}')\nprint('{}')\n")
        self.assertTrue(runner.verify_one(root, package))

    def test_boolean_and_integer_are_not_equal_results(self):
        self.assertNotEqual(runner.canonical({"x": True}), runner.canonical({"x": 1}))


if __name__ == "__main__":
    unittest.main()
