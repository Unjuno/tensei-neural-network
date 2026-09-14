#!/usr/bin/env python3
from __future__ import annotations
import json,random,sys
from pathlib import Path
NS=(7,9,11,13,15,17);TARGET=128;MAXC=200000

def weights(ps):
 n=len(ps[0]);return [[0 if i==j else sum(p[i]*p[j] for p in ps) for j in range(n)] for i in range(n)]
def majority(ps):return tuple(1 if sum(p[i] for p in ps)>0 else -1 for i in range(len(ps[0])))
def local(s,w,i):return sum(w[i][j]*s[j] for j in range(len(s)))
def eligible(q,w):
 m=[q[i]*local(q,w,i) for i in range(len(q))];return all(x>=0 for x in m) and any(x==0 for x in m),m

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
 summary=[];total=0
 for n in NS:
  rng=random.Random(1100000+n);srng=random.Random(1110000+n)
  cyc=[tuple(list(range(n))[k:]+list(range(n))[:k]) for k in range(n)];rnd=[]
  for _ in range(32):a=list(range(n));srng.shuffle(a);rnd.append(tuple(a))
  schedules=cyc+rnd;gen=el=checked=0
  while el<TARGET and gen<MAXC:
   gen+=1;ps=[tuple(rng.choice((-1,1)) for _ in range(n)) for _ in range(3)]
   if len(set(ps))<3:continue
   q=majority(ps);forbidden=set(ps)|{tuple(-x for x in p) for p in ps}
   if q in forbidden:continue
   w=weights(ps);ok,margins=eligible(q,w)
   if not ok:continue
   split=[i for i in range(n) if not(ps[0][i]==ps[1][i]==ps[2][i])]
   if not split:continue
   el+=1;negs={tuple(-x for x in p) for p in ps}
   for i in split:
    minority=next(k for k,p in enumerate(ps) if p[i]!=q[i]);st=list(q);st[i]*=-1;st=tuple(st)
    for j,o in enumerate(schedules):
     checked+=1;total+=1;f,sw,conv=run(st,w,o)
     if not conv or (f!=q and f!=ps[minority]):
      cls='NONCONVERGED' if not conv else 'STORED_OTHER' if f in ps else 'STORED_NEGATION' if f in negs else 'OTHER_NONSTORED'
      return {'experiment':'EXP-011','result':'COUNTEREXAMPLE_FOUND','summary':summary,'N':n,'generated_candidates':gen,'eligible_index':el,'checked_trajectories':total,'patterns':[list(p) for p in ps],'Q':list(q),'Q_margins':margins,'coordinate':i+1,'minority_index':minority+1,'schedule_kind':'cyclic' if j<n else 'random','schedule_index':j+1,'order':[x+1 for x in o],'final':list(f),'classification':cls,'sweeps':sw}
  if el<TARGET:return {'experiment':'EXP-011','result':'UNCERTAIN','reason':'INSUFFICIENT_ELIGIBLE','summary':summary,'N':n,'generated_candidates':gen,'eligible':el,'checked_trajectories':total}
  summary.append({'N':n,'generated_candidates':gen,'eligible':el,'trajectories':checked})
 return {'experiment':'EXP-011','result':'NO_COUNTEREXAMPLE_IN_SEARCH','summary':summary,'checked_trajectories':total}

def main():
 r=execute();print(json.dumps(r,ensure_ascii=False,indent=2))
 if '--write' in sys.argv:Path(__file__).with_name('results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 if '--check' in sys.argv and r.get('result') not in {'COUNTEREXAMPLE_FOUND','NO_COUNTEREXAMPLE_IN_SEARCH','UNCERTAIN'}:return 1
 return 0
if __name__=='__main__':raise SystemExit(main())
