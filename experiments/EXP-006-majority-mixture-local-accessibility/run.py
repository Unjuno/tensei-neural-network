#!/usr/bin/env python3
from __future__ import annotations
import json, random, statistics
from collections import Counter
from pathlib import Path

N=16; TARGET=256; MAX_CANDIDATES=100000; SEED=19830914
ORDERS=[tuple(list(range(N))[k:]+list(range(N))[:k]) for k in range(N)]

def weights(ps):
    return [[0 if i==j else sum(p[i]*p[j] for p in ps) for j in range(N)] for i in range(N)]

def majority(ps):
    return tuple(1 if sum(p[i] for p in ps)>0 else -1 for i in range(N))

def local(s,w,i):
    return sum(w[i][j]*s[j] for j in range(N))

def stable_nonzero(q,w):
    return all((h:=local(q,w,i))!=0 and (1 if h>0 else -1)==q[i] for i in range(N))

def run(st,w,order):
    s=list(st)
    for sweep in range(1,101):
        before=tuple(s)
        for i in order:
            h=local(s,w,i)
            if h>0: s[i]=1
            elif h<0: s[i]=-1
        if tuple(s)==before: return tuple(s),sweep,True
    return tuple(s),100,False

def execute():
    rng=random.Random(SEED); eligible=[]; generated=0
    while len(eligible)<TARGET and generated<MAX_CANDIDATES:
        generated+=1
        ps=[tuple(rng.choice((-1,1)) for _ in range(N)) for _ in range(3)]
        if len(set(ps))<3: continue
        q=majority(ps); forbidden=set(ps)|{tuple(-x for x in p) for p in ps}
        if q in forbidden: continue
        w=weights(ps)
        if not stable_nonzero(q,w): continue
        unanimous=[i for i in range(N) if ps[0][i]==ps[1][i]==ps[2][i]]
        split=[i for i in range(N) if i not in unanimous]
        if unanimous and split: eligible.append((ps,q,w,unanimous,split))
    if len(eligible)<TARGET:
        return {"experiment":"EXP-006","result":"UNCERTAIN","reason":"INSUFFICIENT_ELIGIBLE","generated":generated,"eligible":len(eligible)}

    diffs=[]; ru_values=[]; rs_values=[]; gt=eq=lt=0; nonconv=0
    total_u=q_u=total_s=q_s=0; final_class=Counter(); split_nonq=split_to_minority=0
    coordinate_shapes=Counter()
    for ps,q,w,unanimous,split in eligible:
        coordinate_shapes[(len(unanimous),len(split))]+=1
        tr_u=qr_u=tr_s=qr_s=0
        negs={tuple(-x for x in p) for p in ps}
        for i in range(N):
            st=list(q); st[i]*=-1; st=tuple(st)
            minority=None
            if i in split:
                minority=next(k for k,p in enumerate(ps) if p[i]!=q[i])
            for order in ORDERS:
                final,sweeps,converged=run(st,w,order)
                nonconv += 0 if converged else 1
                if i in unanimous:
                    tr_u+=1; qr_u+= final==q
                else:
                    tr_s+=1; qr_s+= final==q
                    if final!=q:
                        split_nonq+=1
                        split_to_minority += final==ps[minority]
                if final!=q:
                    if final in ps: final_class["stored"]+=1
                    elif final in negs: final_class["stored_negation"]+=1
                    else: final_class["other_nonstored"]+=1
        ru=qr_u/tr_u; rs=qr_s/tr_s
        ru_values.append(ru); rs_values.append(rs); diffs.append(ru-rs)
        gt+=ru>rs; eq+=ru==rs; lt+=ru<rs
        total_u+=tr_u; q_u+=qr_u; total_s+=tr_s; q_s+=qr_s

    support=statistics.median(diffs)>0 and gt>lt and nonconv==0
    return {
      "experiment":"EXP-006","result":"SUPPORT" if support else "NOT_SUPPORT",
      "seed":SEED,"generated_candidates":generated,"eligible_triples":len(eligible),
      "trajectories":total_u+total_s,"nonconverged":nonconv,
      "primary":{
        "mean_ru_minus_rs":statistics.mean(diffs),"median_ru_minus_rs":statistics.median(diffs),
        "ru_gt_rs":gt,"ru_eq_rs":eq,"ru_lt_rs":lt,
        "mean_ru":statistics.mean(ru_values),"mean_rs":statistics.mean(rs_values)
      },
      "pooled":{
        "unanimous_trials":total_u,"unanimous_q_returns":q_u,"unanimous_q_return_fraction":q_u/total_u,
        "split_trials":total_s,"split_q_returns":q_s,"split_q_return_fraction":q_s/total_s
      },
      "secondary":{
        "non_q_final_classes":dict(final_class),"split_non_q_trials":split_nonq,
        "split_non_q_to_minority_stored":split_to_minority,
        "split_non_q_to_minority_fraction":split_to_minority/split_nonq if split_nonq else None,
        "coordinate_shapes":{f"{u}/{s}":c for (u,s),c in sorted(coordinate_shapes.items())}
      }
    }

def main():
    result=execute(); print(json.dumps(result,ensure_ascii=False,indent=2))
    import sys
    if "--write" in sys.argv:
        Path(__file__).with_name("results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return 0
if __name__=="__main__": raise SystemExit(main())
