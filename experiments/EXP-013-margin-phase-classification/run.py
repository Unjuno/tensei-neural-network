#!/usr/bin/env python3
from __future__ import annotations
import json,random,sys
from collections import Counter
from pathlib import Path

NS=tuple(range(7,17));TARGET=64;MAXC=100000

def weights(ps):
    n=len(ps[0]);return [[0 if i==j else sum(p[i]*p[j] for p in ps) for j in range(n)] for i in range(n)]
def majority(ps):return tuple(1 if sum(p[i] for p in ps)>0 else -1 for i in range(len(ps[0])))
def local(s,w,i):return sum(w[i][j]*s[j] for j in range(len(s)))
def run(st,w,order):
    s=list(st)
    for sw in range(1,101):
        before=tuple(s)
        for i in order:
            h=local(s,w,i)
            if h>0:s[i]=1
            elif h<0:s[i]=-1
        if tuple(s)==before:return tuple(s),sw,True
    return tuple(s),100,False

def execute():
    summary=[];regime_states=Counter();regime_trials=Counter();finals=Counter();margin_states=Counter();total=0
    for n in NS:
        rng=random.Random(1300000+n);srng=random.Random(1310000+n)
        cyclic=[tuple(list(range(n))[k:]+list(range(n))[:k]) for k in range(n)]
        random_orders=[]
        for _ in range(16):
            a=list(range(n));srng.shuffle(a);random_orders.append(tuple(a))
        schedules=cyclic+random_orders;generated=eligible=ntr=0
        while eligible<TARGET and generated<MAXC:
            generated+=1
            ps=[tuple(rng.choice((-1,1)) for _ in range(n)) for _ in range(3)]
            if len(set(ps))<3:continue
            q=majority(ps);forbidden=set(ps)|{tuple(-x for x in p) for p in ps}
            if q in forbidden:continue
            w=weights(ps);margins=[q[i]*local(q,w,i) for i in range(n)]
            if not all(x>=0 for x in margins):continue
            split=[i for i in range(n) if not(ps[0][i]==ps[1][i]==ps[2][i])]
            if not split:continue
            eligible+=1
            for k in split:
                minority_idx=next(a for a,p in enumerate(ps) if p[k]!=q[k])
                D=[i for i in range(n) if ps[minority_idx][i]!=q[i]]
                a=margins[k]
                if not all(margins[i]==a for i in D):
                    return {'experiment':'EXP-013','result':'COUNTEREXAMPLE_FOUND','reason':'TYPE_MARGIN_NOT_EQUAL','N':n,'coordinate':k+1}
                regime='ZERO' if a==0 else 'MIDDLE' if a<6 else 'HIGH'
                regime_states[regime]+=1;margin_states[str(a)]+=1
                st=list(q);st[k]*=-1;st=tuple(st)
                posmaps=[{unit:pos for pos,unit in enumerate(order)} for order in schedules]
                for order,posmap in zip(schedules,posmaps):
                    total+=1;ntr+=1;regime_trials[regime]+=1
                    if a==0:pred=ps[minority_idx]
                    elif a<6:
                        first=min(D,key=lambda i:posmap[i]);pred=q if first==k else ps[minority_idx]
                    else:pred=q
                    final,sweeps,conv=run(st,w,order)
                    actual='Q' if final==q else 'MINORITY' if final==ps[minority_idx] else 'OTHER'
                    finals[f'{regime}_{actual}']+=1
                    if not conv or final!=pred:
                        return {'experiment':'EXP-013','result':'COUNTEREXAMPLE_FOUND','N':n,'generated_candidates':generated,'eligible_index':eligible,'checked_trajectories':total,'margin':a,'regime':regime,'coordinate':k+1,'D':[i+1 for i in D],'order':[i+1 for i in order],'predicted':'Q' if pred==q else 'MINORITY','actual':actual,'sweeps':sweeps,'converged':conv}
        if eligible<TARGET:
            return {'experiment':'EXP-013','result':'UNCERTAIN','reason':'INSUFFICIENT_ELIGIBLE','N':n,'generated_candidates':generated,'eligible':eligible,'checked_trajectories':total}
        summary.append({'N':n,'generated_candidates':generated,'eligible':eligible,'trajectories':ntr})
    return {'experiment':'EXP-013','result':'PHASE_RULE_MATCHED_SEARCH','summary':summary,'eligible_total':TARGET*len(NS),'checked_trajectories':total,'regime_states':dict(regime_states),'regime_trials':dict(regime_trials),'finals':dict(finals),'margin_state_counts':dict(sorted(margin_states.items(),key=lambda kv:int(kv[0])))}

def main():
    r=execute();print(json.dumps(r,ensure_ascii=False,indent=2))
    if '--write' in sys.argv:Path(__file__).with_name('results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if '--check' in sys.argv and r.get('result') not in {'PHASE_RULE_MATCHED_SEARCH','COUNTEREXAMPLE_FOUND'}:return 1
    return 0
if __name__=='__main__':raise SystemExit(main())
