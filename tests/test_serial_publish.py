import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
try:
    import serial_publish as pub
except ImportError:
    pub = None

class SerialPublishTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(pub, 'serial_publish engine is not implemented')
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.src, self.dst = self.root/'source', self.root/'target'
        self.src.mkdir(); self.dst.mkdir()
        self.policy = {'schema_version':1,'enabled':True,'repository':'Unjuno/tensei-neural-network',
          'source_branch':'work/story-bootstrap','target_branch':'main','output':'docs/serial',
          'max_chapters_per_day':1,'authorization':'user-request-2026-10-31'}
        self.sha = 'a'*40
        self.ci = {'head_sha':self.sha,'head_branch':'work/story-bootstrap','status':'completed',
          'conclusion':'success','path':'.github/workflows/story-workflow-validation.yml','id':42,
          'repository':{'full_name':'Unjuno/tensei-neural-network'}}
        self.chapter('001')

    def write(self, name, value):
        p=self.src/name;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False),encoding='utf8')

    def chapter(self, n):
        package=f'experiments/chapters/{n}'
        self.write(f'novel/chapters/{n}.md',f'# 第{int(n)}話　試作\n\n　問いを紙に残す。\n')
        self.write(f'novel/chapters/{n}-outline.md','## 採用event\n\nEVT-001\n')
        self.write('novel/events/EVT-001-example.md','状態: `RESOLVED / PROVISIONAL`\n')
        for p in ('POLICY.md','WORKFLOW.md','novel/WORLD_POLICY.md','novel/STYLE_WEBNOVEL.md'):
            self.write(p,'定義\n')
        self.write(f'{package}/README.md','状態: `PREPUBLICATION_GATE_PASSED`\n')
        for f in ('verification.md','semantic-review.md'):
            self.write(f'{package}/{f}','状態: `PASS`\n')
        self.write(f'{package}/terminology.md','| 表記 | 状態 |\n|素子|PASS|\n')
        self.lock(n)

    def lock(self,n):
        p=f'experiments/chapters/{n}'
        files=[f'novel/chapters/{n}.md',f'novel/chapters/{n}-outline.md',f'{p}/verification.md',
               f'{p}/semantic-review.md',f'{p}/terminology.md','novel/events/EVT-001-example.md',
               'POLICY.md','WORKFLOW.md','novel/WORLD_POLICY.md','novel/STYLE_WEBNOVEL.md']
        self.write(f'{p}/review-lock.json',{'schema_version':1,'chapter':n,'algorithm':'git-blob-sha1',
                    'files':{name:pub.blob((self.src/name).read_bytes()) for name in files}})
        self.reader(n)

    def reader(self,n):
        self.write(f'publication/reviews/{n}.json',{'schema_version':1,'chapter':n,'verdict':'PASS',
          'review_kind':'AI_EDITORIAL_NOT_EXTERNAL_READER','chapter_blob':pub.blob((self.src/f'novel/chapters/{n}.md').read_bytes()),
          'review_lock_blob':pub.blob((self.src/f'experiments/chapters/{n}/review-lock.json').read_bytes()),
          'blocking_issues':[], 'checks':{k:'具体箇所を読み照合した。' for k in pub.EDITORIAL_CHECKS}})

    def plan(self,date='2026-10-31'):
        return pub.prepare(self.src,self.dst,self.policy,self.ci,self.sha,date, delivered=pub.read_manifest(self.dst))

    def apply(self, plan):
        for name,data in plan['files'].items():
            p=self.dst/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data,encoding='utf8')

    def test_happy_path(self):
        p=self.plan();self.assertEqual(p['status'],'READY');self.assertEqual(p['chapter'],'001')
        self.assertTrue(all(x.startswith('docs/serial/') for x in p['files']))

    def test_draft_blocked(self):
        self.write('experiments/chapters/001/README.md','状態: IN_PROGRESS\n')
        with self.assertRaises(pub.Blocked):self.plan()

    def test_stale_lock_blocked(self):
        self.write('novel/chapters/001.md','# 改変\n')
        with self.assertRaises(pub.Blocked):self.plan()

    def test_missing_reader_review_blocked(self):
        (self.src/'publication/reviews/001.json').unlink()
        with self.assertRaises(pub.Blocked):self.plan()

    def test_reader_cannot_inherit_new_lock(self):
        self.write('experiments/chapters/001/semantic-review.md','状態: PASS\n改稿\n')
        old=(self.src/'publication/reviews/001.json').read_text()
        self.lock('001');self.write('publication/reviews/001.json',old)
        with self.assertRaises(pub.Blocked):self.plan()

    def test_unknown_ci_blocked(self):
        self.ci['head_sha']='b'*40
        with self.assertRaises(pub.Blocked):self.plan()

    def test_failed_ci_blocked(self):
        self.ci['conclusion']='failure'
        with self.assertRaises(pub.Blocked):self.plan()

    def test_different_workflow_blocked(self):
        self.ci['path']='.github/workflows/other.yml'
        with self.assertRaises(pub.Blocked):self.plan()

    def test_kill_switch(self):
        self.policy['enabled']=False
        self.assertEqual(self.plan()['status'],'PAUSED')

    def test_no_ready_chapter(self):
        (self.src/'novel/chapters/001.md').unlink()
        self.assertEqual(self.plan()['status'],'NO_READY_CHAPTER')

    def test_no_skipping(self):
        (self.src/'novel/chapters/001.md').unlink();self.chapter('002')
        with self.assertRaises(pub.Blocked):self.plan()

    def test_retry_no_duplicate(self):
        p=self.plan();self.apply(p)
        self.assertEqual(self.plan()['status'],'DAILY_LIMIT')
        self.assertEqual(self.plan('2026-11-01')['status'],'NO_READY_CHAPTER')

    def test_next_chapter_tomorrow(self):
        self.apply(self.plan());self.chapter('002')
        self.assertEqual(self.plan()['status'],'DAILY_LIMIT')
        self.assertEqual(self.plan('2026-11-01')['chapter'],'002')

    def test_released_html_tampering_blocked(self):
        self.apply(self.plan());(self.dst/'docs/serial/001.html').write_text('tamper')
        with self.assertRaises(pub.Blocked):self.plan('2026-11-01')

    def test_unsafe_markdown_is_text(self):
        self.write('novel/chapters/001.md','# 第1話\n\n<script>alert(1)</script>\n\n神経回路網《ニューラル・ネットワーク》\n')
        self.lock('001');h=self.plan()['files']['docs/serial/001.html']
        self.assertNotIn('<script>',h);self.assertIn('&lt;script&gt;',h);self.assertIn('<ruby>',h)

    def test_path_escape_blocked(self):
        self.write('experiments/chapters/001/review-lock.json',{'schema_version':1,'chapter':'001','algorithm':'git-blob-sha1','files':{'../outside':'a'*40}})
        with self.assertRaises(pub.Blocked):self.plan()

    def test_symlink_blocked(self):
        p=self.src/'novel/chapters/001.md';p.unlink();p.symlink_to('/etc/passwd')
        with self.assertRaises(pub.Blocked):self.plan()

    def test_unverified_terminology_blocked(self):
        self.write('experiments/chapters/001/terminology.md','|語| UNVERIFIED |\n');self.lock('001')
        with self.assertRaises(pub.Blocked):self.plan()

    def test_experiment_missing_result_blocked(self):
        self.write('experiments/chapters/001/run.py','print("hi")')
        with self.assertRaises(pub.Blocked):self.plan()

    def test_result_false_check_blocked(self):
        self.write('experiments/chapters/001/run.py','pass')
        self.write('experiments/chapters/001/results.json',{'chapter':'001','result':'PASS','checks':{'bad':False}})
        with self.assertRaises(pub.Blocked):self.plan()

    def test_publication_cannot_change_target(self):
        self.policy['output']='novel'
        with self.assertRaises(pub.Blocked):self.plan()

    def test_future_clock_blocked(self):
        self.apply(self.plan())
        with self.assertRaises(pub.Blocked):self.plan('2026-10-30')

    def test_deployment_retry_blocks_new_episode(self):
        self.apply(self.plan());self.chapter('002')
        p=pub.prepare(self.src,self.dst,self.policy,self.ci,self.sha,'2026-11-01',delivered=None)
        self.assertEqual(p['status'],'RETRY_DEPLOY');self.assertEqual(p['files'],{})

    def test_remote_ahead_must_not_rollback(self):
        self.apply(self.plan());remote=pub.read_manifest(self.dst)
        remote['releases'].append(dict(remote['releases'][0],chapter='002'))
        with self.assertRaises(pub.Blocked):
            pub.prepare(self.src,self.dst,self.policy,self.ci,self.sha,'2026-11-01',delivered=remote)

    def test_remote_divergence_is_not_overwritten(self):
        self.apply(self.plan());remote=pub.read_manifest(self.dst)
        remote['releases'][0]['title']='another release'
        with self.assertRaises(pub.Blocked):
            pub.prepare(self.src,self.dst,self.policy,self.ci,self.sha,'2026-11-01',delivered=remote)

    def test_exact_status_not_quoted_example(self):
        self.write('experiments/chapters/001/README.md','```\n状態: PREPUBLICATION_GATE_PASSED\n```\nまだ未承認\n')
        with self.assertRaises(pub.Blocked):self.plan()

if __name__=='__main__':unittest.main()
