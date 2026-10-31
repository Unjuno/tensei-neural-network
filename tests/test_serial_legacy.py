import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import serial_publish as pub

class LegacyEventTests(unittest.TestCase):
    def test_registered_exact_old_event_is_resolved(self):
        self.assertTrue(hasattr(pub, 'event_resolved'), 'legacy event adapter is absent')
        body='状態: `PROVISIONAL`\n\n## Resolved consequence\n成立した。\n'
        with patch.dict(pub.LEGACY_RESOLVED_BLOBS, {pub.blob(body.encode()): 'test fixture'}):
            self.assertTrue(pub.event_resolved(body))
            self.assertFalse(pub.event_resolved(body+'改変\n'))

    def test_unknown_provisional_is_not_resolved(self):
        self.assertTrue(hasattr(pub, 'event_resolved'), 'legacy event adapter is absent')
        self.assertFalse(pub.event_resolved('状態: `PROVISIONAL`\n## Resolved consequence\n'))

    def test_pending_and_deceptive_status_are_rejected(self):
        self.assertTrue(hasattr(pub, 'event_resolved'), 'legacy event adapter is absent')
        for state in ('ACTION_LOCKED','UNRESOLVED','RESOLVED_LATER','RESOLVED / PENDING'):
            with self.subTest(state=state):
                self.assertFalse(pub.event_resolved('状態: `'+state+'`\n'))
        for state in ('RESOLVED','RESOLVED / PROVISIONAL'):
            self.assertTrue(pub.event_resolved('状態: `'+state+'`\n'))

if __name__=='__main__':unittest.main()
