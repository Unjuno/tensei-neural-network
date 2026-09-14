#!/usr/bin/env python3
from __future__ import annotations
import json, random, sys
from pathlib import Path

NS=(12,16,20,24); TARGET=128; MAX_CANDIDATES=200000

def weights(ps):
    n=len(ps[0]); return [[0 if i==j else sum(p[i]*p[j] for p in ps) for j in range(n)] for i in range(n)]
def majority(ps): return tuple(1 if sum(p[i] for p in ps)>0 else -1 for i in range(len(ps[0])))
def local(s,w,i): return sum(w[i][j]*s[j] for j in range(len(s)))
def stable_nonzero(q,w): return all((h:=local(q,w,i))!=0 and (1 if h>0 else -1)==q[i] for i in range(len(q)))

def run(st,w,order):
    s=list(st)
    for sweep in range(1,101):
        before=tuple(s)
        for i in order:
            h=local(s,w,i)
            if h>0:s[i]=1
            elif h<0:s[i]=-1
        if tuple(s)==before:return tuple(s),sweep,True
    return tuple(s),100,False

def execute():
    checked=0
    for n in NS:
        rng=random.Random(900000+n); srng=random.Random(910000+n)
        cyclic=[tuple(list(range(n))[k:]+list(range(n))[:k]) for k in range(n)]
        random_orders=[]
        for _ in range(32):
            a=list(range(n)); srng.shuffle(a); random_orders.append(tuple(a))
        schedules=cyclic+random_orders
        generated=eligible=0
        while eligible<TARGET and generated<MAX_CANDIDATES:
            generated+=1
            ps=[tuple(rng.choice((-1,1)) for _ in range(n)) for _ in range(5)]
            if len(set(ps))<5:continue
            q=majority(ps); forbidden=set(ps)|{tuple(-x for x in p) for p in ps}
            if q in forbidden:continue
            w=weights(ps)
            if not stable_nonzero(q,w):continue
            split=[i for i in range(n) if not all(p[i]==ps[0][i] for p in ps)]
            if not split:continue
            eligible+=1; negs={tuple(-x for x in p) for p in ps}
            for i in split:
                minority={ps[k] for k,p in enumerate(ps) if p[i]!=q[i]}
                st=list(q);st[i]*=-1;st=tuple(st)
                for j,order in enumerate(schedules):
                    checked+=1; final,sweeps,conv=run(st,w,order)
                    if not conv or (final!=q and final not in minority):
                        cls=("NONCONVERGED" if not conv else "STORED_OUTSIDE_MINORITY" if final in ps else "STORED_NEGATION" if final in negs else "OTHER_NONSTORED")
                        return {"experiment":"EXP-012","result":"COUNTEREXAMPLE_FOUND","N":n,"generated_candidates":generated,"eligible_index":eligible,"checked_trajectories":checked,"patterns":[list(p) for p in ps],"Q":list(q),"coordinate":i+1,"minority_indices":[k+1 for k,p in enumerate(ps) if p[i]!=q[i]],"initial":list(st),"schedule_kind":"cyclic" if j<n else "random","schedule_index":j+1,"order":[x+1 for x in order],"final":list(final),"classification":cls,"sweeps":sweeps,"converged":conv}
        if eligible<TARGET:return {"experiment":"EXP-012","result":"UNCERTAIN","N":n,"generated":generated,"eligible":eligible}
    return {"experiment":"EXP-012","result":"NO_COUNTEREXAMPLE_IN_SEARCH","checked_trajectories":checked}

def main():
    r=execute();print(json.dumps(r,ensure_ascii=False,indent=2))
    if "--write" in sys.argv:Path(__file__).with_name("results.json").write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if "--check" in sys.argv and r.get("result") not in {"COUNTEREXAMPLE_FOUND","NO_COUNTEREXAMPLE_IN_SEARCH"}:return 1
    return 0
if __name__=="__main__":raise SystemExit(main())
