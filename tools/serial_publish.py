#!/usr/bin/env python3
"""Read reviewed work as data; export one immutable serial episode. Never run source code."""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path, PurePosixPath

REPOSITORY = 'Unjuno/tensei-neural-network'
OUTPUT = 'docs/serial'
EDITORIAL_CHECKS = ('reader_question', 'character_agency', 'exposition_load', 'event_fidelity', 'ending')

class Blocked(ValueError):
    """Fail closed: the material or authorization is not ready for publication."""

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe(root: Path, name: str) -> Path:
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name:
        raise Blocked('unsafe path: '+name)
    out = root / name
    for ancestor in (out, *out.parents):
        if ancestor.is_symlink():
            raise Blocked('symlink is not a publication input: '+name)
        if ancestor == root:
            break
    if not out.resolve().is_relative_to(root.resolve()):
        raise Blocked('path leaves repository: '+name)
    return out

def read(root: Path, name: str) -> bytes:
    p = safe(root, name)
    try:
        if p.stat().st_size > 2_000_000:
            raise Blocked('file exceeds publication limit: '+name)
        return p.read_bytes()
    except OSError as exc:
        raise Blocked('missing input: '+name) from exc

def text(root: Path, name: str) -> str:
    try:
        return read(root,name).decode('utf-8')
    except UnicodeDecodeError as exc:
        raise Blocked('non UTF-8 input: '+name) from exc

def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise Blocked('duplicate JSON key: '+key)
        result[key] = value
    return result

def decode(body: str):
    try:
        return json.loads(body, object_pairs_hook=pairs)
    except json.JSONDecodeError as exc:
        raise Blocked('invalid JSON') from exc

def load(root: Path, name: str):
    return decode(text(root,name))

def status(body: str) -> str | None:
    lines, fence = [], None
    for line in body.splitlines():
        m = re.match(r'^\s*(`{3,}|~{3,})',line)
        if m:
            mark=m[1]
            if fence is None: fence=mark
            elif mark[0]==fence[0] and len(mark)>=len(fence): fence=None
        elif fence is None: lines.append(line)
    declarations = re.findall(r'^状態:[ \t]*(.+?)[ \t]*$', '\n'.join(lines), re.M)
    return declarations[0].strip().strip('`').strip() if len(declarations)==1 else None

# Early records already contain resolved consequences but predate RESOLVED status.
# Exact, reviewed historical objects only; no new PROVISIONAL record is admitted.
LEGACY_RESOLVED_BLOBS = {
    'fb55f9ed79a8ca1a0ce558331ca1c90eae2fcc5e': 'EVT-001',
    '9149057e7637da8cff2d79e9261bf035c7cc501f': 'EVT-002',
    'ff96cd7165b6cf17478412bb66c220fd2ad5350f': 'EVT-003',
    'e0cfeb809bdfb0809c3e51fba973188ec95a121c': 'EVT-004',
}

def event_resolved(body: str) -> bool:
    state = status(body)
    if state in ('RESOLVED', 'RESOLVED / PROVISIONAL'):
        return True
    return state == 'PROVISIONAL' and blob(body.encode('utf8')) in LEGACY_RESOLVED_BLOBS

def adopted(body: str) -> set[str]:
    m = re.search(r'^(?:#{1,6}\s+)?(?:採用event|対象event)\s*[:：]?\s*(.*)$',body,re.M)
    if not m: raise Blocked('missing adopted-event section')
    section = m[1]+'\n'+body[m.end():].split('\n## ',1)[0]
    refs=set(re.findall(r'EVT-\d{3}',section))
    if not refs: raise Blocked('empty adopted-event section')
    return refs

def policy_check(policy: dict) -> None:
    expected={'schema_version':1,'repository':REPOSITORY,'source_branch':'work/story-bootstrap',
              'target_branch':'main','output':OUTPUT,'max_chapters_per_day':1,
              'authorization':'user-request-2026-10-31'}
    if not isinstance(policy,dict) or any(policy.get(k)!=v for k,v in expected.items()):
        raise Blocked('publication authority/scope mismatch')
    if type(policy.get('enabled')) is not bool: raise Blocked('enabled must be boolean')

def ci_check(ci: dict, head: str) -> None:
    if not re.fullmatch('[0-9a-f]{40}',head): raise Blocked('full source commit required')
    expected={'head_sha':head,'head_branch':'work/story-bootstrap','status':'completed',
              'conclusion':'success','path':'.github/workflows/story-workflow-validation.yml'}
    if any(ci.get(k)!=v for k,v in expected.items()) or ci.get('repository',{}).get('full_name')!=REPOSITORY:
        raise Blocked('source HEAD has no matching successful CI')
    if type(ci.get('id')) is not int or ci['id']<=0: raise Blocked('missing CI run identifier')

def chapter_check(root: Path, num: str) -> tuple[str, dict, dict]:
    package=f'experiments/chapters/{num}'
    if status(text(root,f'{package}/README.md'))!='PREPUBLICATION_GATE_PASSED':
        raise Blocked('chapter gate not passed: '+num)
    required={f'novel/chapters/{num}.md',f'novel/chapters/{num}-outline.md',
              f'{package}/verification.md',f'{package}/semantic-review.md',f'{package}/terminology.md',
              'POLICY.md','WORKFLOW.md','novel/WORLD_POLICY.md','novel/STYLE_WEBNOVEL.md'}
    for name in ('verification.md','semantic-review.md'):
        if status(text(root,f'{package}/{name}'))!='PASS': raise Blocked(name+' is not PASS')
    terms=text(root,f'{package}/terminology.md')
    if re.search(r'^\|[^\n]*\|\s*`?(?:UNVERIFIED|REPLACE)`?\s*\|',terms,re.M):
        raise Blocked('blocking terminology')
    for event in adopted(text(root,f'novel/chapters/{num}-outline.md')):
        matches=list((root/'novel/events').glob(event+'-*.md'))
        if len(matches)!=1: raise Blocked('missing or duplicated event: '+event)
        name=matches[0].relative_to(root).as_posix(); required.add(name)
        if not event_resolved(text(root,name)):
            raise Blocked('unresolved event: '+event)
    if safe(root,f'{package}/run.py').exists():
        required.update({f'{package}/run.py',f'{package}/results.json'})
        result=load(root,f'{package}/results.json');checks=result.get('checks')
        if result.get('chapter')!=num or result.get('result')!='PASS' or not isinstance(checks,dict) or not checks or any(v is not True for v in checks.values()):
            raise Blocked('experiment did not pass')
    lock=load(root,f'{package}/review-lock.json')
    if lock.get('schema_version')!=1 or lock.get('chapter')!=num or lock.get('algorithm')!='git-blob-sha1':
        raise Blocked('invalid review lock schema')
    files=lock.get('files')
    if not isinstance(files,dict) or not required.issubset(files): raise Blocked('review lock missing dependencies')
    for name, digest in files.items():
        if not isinstance(digest,str) or not re.fullmatch('[0-9a-f]{40}',digest) or blob(read(root,name))!=digest:
            raise Blocked('stale review: '+name)
    body=text(root,f'novel/chapters/{num}.md')
    review=load(root,f'publication/reviews/{num}.json')
    if review.get('schema_version')!=1 or review.get('chapter')!=num or review.get('verdict')!='PASS' or review.get('blocking_issues')!=[]:
        raise Blocked('editorial review incomplete')
    if review.get('review_kind')!='AI_EDITORIAL_NOT_EXTERNAL_READER': raise Blocked('review provenance missing')
    if review.get('chapter_blob')!=blob(body.encode()) or review.get('review_lock_blob')!=blob(read(root,f'{package}/review-lock.json')):
        raise Blocked('editorial review targets an old edition')
    checks=review.get('checks',{})
    if any(not isinstance(checks.get(k),str) or len(checks[k].strip())<8 for k in EDITORIAL_CHECKS):
        raise Blocked('editorial evidence missing')
    if not re.match(r'^# [^\n]+\n',body): raise Blocked('chapter needs one title')
    return body, lock, review

def inline(value: str) -> str:
    value=html.escape(value)
    value=re.sub(r'([一-龯々ァ-ヴー]+)《([^《》\n]+)》',r'<ruby>\1<rp>（</rp><rt>\2</rt><rp>）</rp></ruby>',value)
    return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',value)

def page(title: str, content: str) -> str:
    return ('<!doctype html>\n<html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; base-uri \'none\'; form-action \'none\'">'
      '<title>'+html.escape(title)+'｜転生したらニューラルネットワークだった件</title>'
      '<style>body{max-width:42em;margin:3em auto;padding:0 1.25em;font-family:serif;line-height:2.1;background:#faf9f6;color:#242424}'
      'p{margin:1.15em 0;white-space:pre-wrap}a{color:#245968}h1{font-size:1.6em;line-height:1.6}small{font-family:sans-serif}hr{border:0;border-top:1px solid #ddd;margin:2.5em 0}</style>'
      '<header><a href="index.html">転生したらニューラルネットワークだった件</a><p><small>連載版 · AI編集・検証済み。実読者評価・Canon受理とは別です。</small></p></header>'
      '<main>'+content+'</main></html>\n')

def render(body: str, num: str) -> str:
    title=body.splitlines()[0][2:];parts=['<h1>'+html.escape(title)+'</h1>']
    for para in re.split(r'\n\s*\n',body.split('\n',1)[1].strip()):
        if para.strip() in ('＊','*','***'): parts.append('<hr>')
        else: parts.append('<p>'+inline(para)+'</p>')
    parts.append('<hr><p><a href="index.html">目次へ</a> · <a href="'+num+'.md">本文Markdown</a></p>')
    return page(title,'\n'.join(parts))

def read_manifest(target: Path) -> dict:
    path=safe(target,OUTPUT+'/manifest.json')
    if not path.exists(): return {'schema_version':1,'releases':[]}
    m=load(target,OUTPUT+'/manifest.json')
    if m.get('schema_version')!=1 or not isinstance(m.get('releases'),list): raise Blocked('invalid publication ledger')
    previous='';days=set()
    for i,r in enumerate(m['releases'],1):
        if r.get('chapter')!=f'{i:03d}': raise Blocked('non-contiguous publication ledger')
        day=r.get('released_on','');dt.date.fromisoformat(day)
        if day in days or day<previous: raise Blocked('duplicate or nonmonotonic release date')
        days.add(day);previous=day
        for suffix in ('html','md'):
            data=read(target,f"{OUTPUT}/{r['chapter']}.{suffix}")
            if sha256(data)!=r.get(suffix+'_sha256'): raise Blocked('published snapshot changed')
    return m

def prepare(source: Path,target: Path,policy: dict,ci: dict,head: str,date: str, delivered: dict | None = None) -> dict:
    policy_check(policy);dt.date.fromisoformat(date)
    if not policy['enabled']: return {'status':'PAUSED','files':{}}
    m=read_manifest(target)
    if delivered is not None:
        if not isinstance(delivered,dict) or delivered.get('schema_version')!=1 or not isinstance(delivered.get('releases'),list):
            raise Blocked('unrecognized live manifest')
        remote=delivered['releases']
        if remote!=m['releases'][:len(remote)]:
            raise Blocked('live release is ahead or diverged; automatic rollback forbidden')
    if m['releases'] and delivered!=m:
        return {'status':'RETRY_DEPLOY','files':{}}
    if m['releases']:
        last=m['releases'][-1]['released_on']
        if last>date: raise Blocked('clock precedes published release')
        if last==date: return {'status':'DAILY_LIMIT','files':{}}
    num=f"{len(m['releases'])+1:03d}"
    if len(num)!=3: raise Blocked('chapter identifier capacity exhausted')
    path=safe(source,f'novel/chapters/{num}.md')
    if not path.exists():
        if any(p.stem.isdigit() and int(p.stem)>int(num) for p in (source/'novel/chapters').glob('*.md')):
            raise Blocked('chapter sequence has a gap')
        return {'status':'NO_READY_CHAPTER','files':{}}
    ci_check(ci,head)
    body,lock,review=chapter_check(source,num); rendered=render(body,num)
    record={'chapter':num,'title':body.splitlines()[0][2:],'released_on':date,'source_sha':head,
      'ci_run':ci['id'],'md_sha256':sha256(body.encode()),'html_sha256':sha256(rendered.encode()),
      'review_lock_blob':blob(read(source,f'experiments/chapters/{num}/review-lock.json')),
      'editorial_review_blob':blob(read(source,f'publication/reviews/{num}.json'))}
    m['releases'].append(record)
    items=''.join('<li><a href="'+r['chapter']+'.html">'+html.escape(r['title'])+'</a></li>' for r in m['releases'])
    index=page('連載目次','<h1>連載目次</h1><ol>'+items+'</ol><p><small>更新は最大1日1話。未検証の回は公開を見送ります。<a href="manifest.json">版と検証の記録</a></small></p>')
    return {'status':'READY','chapter':num,'source_sha':head,'ci_run':ci['id'],'files':{
      f'{OUTPUT}/{num}.md':body,f'{OUTPUT}/{num}.html':rendered,f'{OUTPUT}/index.html':index,
      f'{OUTPUT}/manifest.json':json.dumps(m,ensure_ascii=False,indent=2)+'\n'}}

PUBLIC_BASE = 'https://unjuno.github.io/tensei-neural-network/serial/'

def live_bytes(name: str) -> bytes:
    if not re.fullmatch(r'(?:manifest\.json|[0-9]{3}\.html)',name):
        raise Blocked('invalid live verification filename')
    request=urllib.request.Request(PUBLIC_BASE+name+'?verify='+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d%H%M%S'),
        headers={'Cache-Control':'no-cache','User-Agent':'TenseiSerialVerifier/1.0'})
    with urllib.request.urlopen(request, timeout=20) as response:
        data=response.read(2_000_001)
        if len(data)>2_000_000: raise Blocked('oversized live response')
        return data

def probe_live():
    try: return decode(live_bytes('manifest.json').decode('utf8'))
    except (OSError,ValueError,UnicodeError): return None

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source','target','policy','ci','head','delivered'):p.add_argument('--'+name)
    p.add_argument('--date',default=dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).date().isoformat())
    p.add_argument('--write',action='store_true');p.add_argument('--report',required=True)
    p.add_argument('--probe-live',action='store_true');p.add_argument('--verify-live',action='store_true')
    a=p.parse_args()
    try:
        if a.probe_live:
            Path(a.report).write_text(json.dumps(probe_live(),ensure_ascii=False)+'\n',encoding='utf8');return 0
        if a.verify_live:
            if not a.target: raise Blocked('target is required')
            expected=read_manifest(Path(a.target));observed=probe_live()
            if not expected['releases'] or expected!=observed: raise Blocked('live manifest not yet confirmed')
            last=expected['releases'][-1]
            if sha256(live_bytes(last['chapter']+'.html'))!=last['html_sha256']: raise Blocked('live HTML differs')
            summary={'status':'DEPLOYED','chapter':last['chapter'],'source_sha':last['source_sha'],
                     'url':PUBLIC_BASE+last['chapter']+'.html'}
        else:
            if not all(getattr(a,k) for k in ('source','target','policy','ci','head','delivered')):
                raise Blocked('source, target, policy, ci, head and delivered are required')
            plan=prepare(Path(a.source),Path(a.target),decode(Path(a.policy).read_text()),decode(Path(a.ci).read_text()),
                         a.head,a.date,delivered=decode(Path(a.delivered).read_text()))
            if a.write:
                for name,content in plan['files'].items():
                    dest=safe(Path(a.target),name);dest.parent.mkdir(parents=True,exist_ok=True)
                    dest.write_text(content,encoding='utf8')
            summary={k:v for k,v in plan.items() if k!='files'};summary['paths']=list(plan['files'])
        Path(a.report).write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        print(json.dumps(summary,ensure_ascii=False));return 0
    except (Blocked,ValueError,KeyError,TypeError,OSError) as exc:
        result={'status':'BLOCKED','reason':str(exc)}
        Path(a.report).write_text(json.dumps(result,ensure_ascii=False)+'\n',encoding='utf8')
        print(json.dumps(result,ensure_ascii=False));return 1

if __name__=='__main__':raise SystemExit(main())
