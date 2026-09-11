#!/usr/bin/env python3
from __future__ import annotations
import json, random, sys
from pathlib import Path

NS=(8,12,16,20,24); TARGET=128

def execute():
    summary={}; total_traj=total_nonq=0
    for N in NS:
        rng=random.Random(700000+N); srng=random.Random(710000+N); base=list(range(N))
        random_orders=[]
        for _ in range(32):
            a=base.copy(); srng.shuffle(a); random_orders.append(tuple(a))
        orders=[tuple(base[k:]+base[:k]) for k in range(N)]+random_orders
        def weights(ps): return [[0 if i==j else sum(p[i]*p[j] for p in ps) for j in range(N)] for i in range(N)]
        def majority(ps): return tuple(1 if sum(p[i] for p in ps)>0 else -1 for i in range(N))
        def local(s,w,i): return sum(w[i][j]*s[j] for j in range(N))
        eligible=[]; generated=0
        while len(eligible)<TARGET and generated<100000:
            generated+=1; ps=[tuple(rng.choice((-1,1)) for _ in range(N)) for _ in range(3)]
            if len(set(ps))<3: continue
            q=majority(ps); forbidden=set(ps)|{tuple(-x for x in p) for p in ps}
            if q in forbidden: continue
            w=weights(ps)
            if not all((h:=local(q,w,i))!=0 and (1 if h>0 else -1)==q[i] for i in range(N)): continue
            split=[i for i in range(N) if not(ps[0][i]==ps[1][i]==ps[2][i])]
            if split: eligible.append((ps,q,w,split))
        if len(eligible)<TARGET:
            return {"experiment":"EXP-007","result":"UNCERTAIN","N":N,"eligible":len(eligible)}
        trajectories=nonq=0
        for eidx,(ps,q,w,split) in enumerate(eligible):
            for i in split:
                minority=next(k for k,p in enumerate(ps) if p[i]!=q[i])
                st=list(q); st[i]*=-1
                for oidx,order in enumerate(orders):
                    s=st.copy(); converged=False
                    for sweep in range(1,101):
                        before=tuple(s)
                        for u in order:
                            h=local(s,w,u)
                            if h>0: s[u]=1
                            elif h<0: s[u]=-1
                        if tuple(s)==before: converged=True; break
                    final=tuple(s); trajectories+=1
                    if final!=q: nonq+=1
                    if (not converged) or (final!=q and final!=ps[minority]):
                        return {"experiment":"EXP-007","result":"COUNTEREXAMPLE_FOUND","N":N,
                                "eligible_index":eidx,"coordinate":i+1,"schedule_index":oidx,
                                "schedule_type":"cyclic" if oidx<N else "random","converged":converged,
                                "sweeps":sweep,"patterns":[list(p) for p in ps],"q":list(q),
                                "minority_index":minority+1,"final":list(final)}
        summary[str(N)]={"generated_candidates":generated,"eligible":TARGET,"trajectories":trajectories,"non_q":nonq}
        total_traj+=trajectories; total_nonq+=nonq
    return {"experiment":"EXP-007","result":"NO_COUNTEREXAMPLE_IN_SEARCH","N_values":list(NS),
            "eligible_per_N":TARGET,"schedule_family":"all cyclic rotations plus 32 fixed random permutations",
            "summary":summary,"total_eligible":TARGET*len(NS),"total_trajectories":total_traj,
            "total_non_q":total_nonq,"counterexamples":0,
            "claim":"Within the preregistered search, every split one-bit trajectory that did not return Q converged to the coordinate-minority stored pattern.",
            "proof_status":"NOT_PROVEN"}

def main():
    result=execute(); print(json.dumps(result,ensure_ascii=False,indent=2)); path=Path(__file__).with_name("results.json")
    if "--write" in sys.argv: path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if "--check" in sys.argv and json.loads(path.read_text(encoding="utf-8"))!=result: return 1
    return 0
if __name__=="__main__": raise SystemExit(main())
