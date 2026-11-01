"""EVT-005の解決済み候補表記と話別review-lockの鮮度を検証する。

GitHubの公開権限やゲートは変更しない。標準ライブラリのみ。
"""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENT = "novel/events/EVT-005-lock-the-order-family.md"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


class EventStatusConsistency(unittest.TestCase):
    def test_evt005_is_resolved_but_not_canon_accepted(self):
        body = (ROOT / EVENT).read_text(encoding="utf-8")
        state = re.search(r"^状態:\s*`([^`]+)`", body, re.M)
        self.assertIsNotNone(state)
        self.assertEqual(state.group(1), "RESOLVED / PROVISIONAL")
        self.assertIn("Resolution provenance: `LOCKED`", body)
        self.assertIn("Action-lock commit: `59ff6530d202b79834afbe8ffdceee1256437315`", body)
        self.assertIn("## Resolved results", body)
        self.assertIn("## Resolved consequence", body)
        for excerpt in ("r1 ->", "r2 ->", "r3 ->", "r4 ->", "r5 ->", "r6 ->"):
            self.assertIn(excerpt, body)

    def test_all_affected_review_locks_pin_the_exact_event_and_review(self):
        event_sha = git_blob_sha(ROOT / EVENT)
        for chapter in ("002", "003", "004"):
            with self.subTest(chapter=chapter):
                path = ROOT / f"experiments/chapters/{chapter}/review-lock.json"
                lock = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(lock["files"][EVENT], event_sha)
                self.assertEqual(lock["files"][f"experiments/chapters/{chapter}/semantic-review.md"],
                                 git_blob_sha(ROOT / f"experiments/chapters/{chapter}/semantic-review.md"))
                self.assertEqual(lock["files"][f"novel/chapters/{chapter}.md"],
                                 git_blob_sha(ROOT / f"novel/chapters/{chapter}.md"))

    def test_editorial_review_002_pins_new_lock_and_unchanged_body(self):
        review = json.loads((ROOT / "publication/reviews/002.json").read_text(encoding="utf-8"))
        self.assertEqual(review["review_kind"], "AI_EDITORIAL_NOT_EXTERNAL_READER")
        self.assertEqual(review["blocking_issues"], [])
        self.assertEqual(review["verdict"], "PASS")
        self.assertEqual(review["review_lock_blob"],
                         git_blob_sha(ROOT / "experiments/chapters/002/review-lock.json"))
        self.assertEqual(review["chapter_blob"], git_blob_sha(ROOT / "novel/chapters/002.md"))


if __name__ == "__main__":
    unittest.main()
