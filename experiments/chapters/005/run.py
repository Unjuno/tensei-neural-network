#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path

M1=(1,1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1)
M2=(1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,1)
M3=(1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1)
Q =(1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1)
PS=(M1,M2,M3);N=16
ORDERS=[tuple(list(range(N))[k:]+list(range(N))[:k]) for k in range(N)]

def weights():return [[0 if i==j else sum(p[i]*p[j] for p in PS) for j in range(N)] for i in range(N)]
W=weights()
def local(s,i):return sum(W[i][j]*s[j] for j in range(N))

def minority_for(k):return next(p for p in PS if p[k]!=Q[k])
def label(s):
 if s==Q:return 'Q'
 if s==M1:return 'M1'
 if s==M2:return 'M2'
 if s==M3:return 'M3'
 return 'OTHER'

def run(k,order,trace=False):
 s=list(Q);s[k]*=-1;first=None;flips=0
 for sweep in range(1,101):
  before=tuple(s)
  for pos,i in enumerate(order,1):
   h=local(s,i);new=1 if h>0 else -1 if h<0 else s[i]
   if new!=s[i]:
    old=s[i];s[i]=new;flips+=1
    if first is None:first=(i,old,new,h,pos,sweep)
  if tuple(s)==before:return tuple(s),first,flips,sweep,True
 return tuple(s),first,flips,100,False

def gap_count(D,k):
 d=sorted(D);idx=d.index(k);prev=d[idx-1]
 return k-prev if k>prev else N-prev+k

def execute():
 unanimous=[i for i in range(N) if M1[i]==M2[i]==M3[i]]
 split=[i for i in range(N) if i not in unanimous]
 aggregate=Counter();by_k={};first_cross=Counter();flip_count=Counter();unstable_ok=True;gap_ok=True;unexpected=0
 for k in range(N):
  counts=Counter()
  for order in ORDERS:
   final,first,flips,sweeps,conv=run(k,order)
   lab=label(final);counts[lab]+=1;aggregate[lab]+=1
   if not conv or lab=='OTHER':unexpected+=1
   if k in split:
    minority=minority_for(k);expected='MINORITY' if final==minority else lab
    cat='REPAIR_K_FIRST' if first and first[0]==k and first[2]==Q[k] else 'OTHER_FLIP_FIRST' if first and first[0]!=k else 'OTHER'
    first_cross[(cat,expected)]+=1;flip_count[(cat,flips)]+=1
  by_k[str(k+1)]={x:counts.get(x,0) for x in ('Q','M1','M2','M3')}
  if k in split:
   minority=minority_for(k);D={i for i in range(N) if minority[i]!=Q[i]}
   s=list(Q);s[k]*=-1;s=tuple(s)
   unstable={i for i in range(N) if (h:=local(s,i))!=0 and (1 if h>0 else -1)!=s[i]}
   unstable_ok &= unstable==D
   gap_ok &= counts['Q']==gap_count(D,k)
 checks={
  'aggregate_112_48_48_48':dict(aggregate)=={'Q':112,'M3':48,'M2':48,'M1':48},
  'unanimous_four_all_return_Q':all(by_k[str(k+1)]['Q']==16 for k in unanimous),
  'split_first_flip_complete_separation':first_cross[('REPAIR_K_FIRST','Q')]==48 and first_cross[('OTHER_FLIP_FIRST','MINORITY')]==144 and sum(first_cross.values())==192,
  'repair_trials_have_one_flip':flip_count[('REPAIR_K_FIRST',1)]==48,
  'minority_trials_have_three_flips':flip_count[('OTHER_FLIP_FIRST',3)]==144,
  'initial_unstable_set_equals_difference_set':unstable_ok,
  'cyclic_gap_counts_match_Q_counts':gap_ok,
  'no_unexpected_final_or_nonconvergence':unexpected==0,
 }
 return {'chapter':'005','checks':checks,'aggregate':{k:aggregate.get(k,0) for k in ('Q','M1','M2','M3','OTHER')},'by_flipped_position':by_k,'first_flip':{'repair_to_Q':first_cross[('REPAIR_K_FIRST','Q')],'other_to_minority':first_cross[('OTHER_FLIP_FIRST','MINORITY')]},'flip_counts':{'repair_branch_total_flips_1':flip_count[('REPAIR_K_FIRST',1)],'minority_branch_total_flips_3':flip_count[('OTHER_FLIP_FIRST',3)]},'result':'PASS' if all(checks.values()) else 'FAIL'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args();r=execute();print(json.dumps(r,ensure_ascii=False,indent=2))
 if a.write:Path(__file__).with_name('results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return 1 if a.check and r['result']!='PASS' else 0
if __name__=='__main__':raise SystemExit(main())
