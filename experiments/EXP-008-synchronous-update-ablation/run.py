#!/usr/bin/env python3
from __future__ import annotations
import json, random, sys
from pathlib import Path

NS=(8,12,16,20,24); TARGET=128; MAX_CANDIDATES=100000

def weights(ps):
    n=len(ps[0]); return [[0 if i==j else sum(p[i]*p[j] for p in ps) for j in range(n)] for i in range(n)]

def majority(ps):
    return tuple(1 if sum(p[i] for p in ps)>0 else -1 for i in range(len(ps[0])))

def local(s,w,i): return sum(w[i][j]*s[j] for j in range(len(s)))

def stable_nonzero(q,w):
    return all((h:=local(q,w,i))!=0 and (1 if h>0 else -1)==q[i] for i in range(len(q)))

def sync_step(s,w):
    out=[]
    for i in range(len(s)):
        h=local(s,w,i); out.append(1 if h>0 else -1 if h<0 else s[i])
    return tuple(out)

def sync_run(st,w):
    s=tuple(st); seen={s:0}; seq=[s]
    for t in range(1,101):
        s=sync_step(s,w); seq.append(s)
        if s in seen:
            return s,t,seen[s],t-seen[s],seq
        seen[s]=t
    return s,100,None,None,seq

def execute():
    checked=0
    for n in NS:
        rng=random.Random(800000+n); eligible=generated=0
        while eligible<TARGET and generated<MAX_CANDIDATES:
            generated+=1
            ps=[tuple(rng.choice((-1,1)) for _ in range(n)) for _ in range(3)]
            if len(set(ps))<3: continue
            q=majority(ps); forbidden=set(ps)|{tuple(-x for x in p) for p in ps}
            if q in forbidden: continue
            w=weights(ps)
            if not stable_nonzero(q,w): continue
            split=[i for i in range(n) if not(ps[0][i]==ps[1][i]==ps[2][i])]
            if not split: continue
            eligible+=1
            for i in split:
                checked+=1
                minority=next(k for k,p in enumerate(ps) if p[i]!=q[i])
                st=list(q); st[i]*=-1; st=tuple(st)
                repeat,steps,cycle_start,cycle_length,seq=sync_run(st,w)
                allowed=cycle_length==1 and repeat in (q,ps[minority])
                if not allowed:
                    return {
                        "experiment":"EXP-008","result":"COUNTEREXAMPLE_FOUND","N":n,
                        "generated_candidates":generated,"eligible_index":eligible,"checked_initial_states":checked,
                        "patterns":[list(p) for p in ps],"Q":list(q),"split_coordinate":i+1,
                        "minority_pattern_index":minority+1,"initial":list(st),
                        "trajectory":[list(x) for x in seq],"cycle_start":cycle_start,
                        "cycle_length":cycle_length,"repeat_state":list(repeat)
                    }
        if eligible<TARGET:
            return {"experiment":"EXP-008","result":"UNCERTAIN","N":n,"reason":"INSUFFICIENT_ELIGIBLE","eligible":eligible,"generated":generated}
    return {"experiment":"EXP-008","result":"NO_COUNTEREXAMPLE_IN_SEARCH","checked_initial_states":checked}

def main():
    r=execute(); print(json.dumps(r,ensure_ascii=False,indent=2))
    if "--write" in sys.argv: Path(__file__).with_name("results.json").write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if "--check" in sys.argv and r.get("result") not in {"COUNTEREXAMPLE_FOUND","NO_COUNTEREXAMPLE_IN_SEARCH"}: return 1
    return 0
if __name__=="__main__": raise SystemExit(main())
