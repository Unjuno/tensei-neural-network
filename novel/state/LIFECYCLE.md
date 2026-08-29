# World State lifecycle

状態: `ACTIVE / PROVISIONAL`

この文書は、`novel/WORLD_POLICY.md` のstate explosion対策を具体化し、entity stateをいつ詳細追跡し、いつ休眠させ、いつ再展開するかを定める。

上位規則は `POLICY.md` と `novel/WORLD_POLICY.md`。矛盾する場合は上位規則を優先する。

## 1. 目的

lazy expansionだけでは、一度詳細化したentityが永続的にactiveになり、長期連載でstate復元コストが増え続ける。

そのためstateには追跡ライフサイクルを持たせる。

```text
UNRESOLVED
   ↓ 必要になった時だけ
ACTIVE
   ↓ 現在因果から外れた
DORMANT
   ↓ 再び因果へ届く
REACTIVATED (= ACTIVE)
```

これは物語世界内でentityが消滅・睡眠したことを意味しない。制作上の**追跡解像度**である。

## 2. ACTIVE

次のいずれかに該当するentity/stateはACTIVEとして扱う。

- current resolution scopeに入る
- active agentが観測・操作する
- 次のevent結果を直接制約する
- provenance / ownership / authority / locationの追跡に現在必要
- unresolved事項の解決が現在eventへ必要

ACTIVE stateは必要な詳細を保持するが、因果へ不要な属性を増やさない。

## 3. DORMANT

次をすべて満たす場合、詳細stateをDORMANTへ落としてよい。

- current resolution scope外である
- 直近eventで直接変化する予定を置いていない
- 現在の観測境界へ直接関与しない
- provenanceを失わずに要約できる
- 再展開時に過去EVT/stateから復元可能である

DORMANT化では過去stateやEVTを削除しない。

最低限、次を残す。

- entity ID
- lifecycle status: `DORMANT`
- last active story time
- last relevant EVT
- last trusted snapshot / checkpoint
- 現在も有効なrelationのうち再展開に必要なもの
- unresolved items
- reactivation trigger

## 4. 再展開

DORMANT entityが再び因果へ届く場合、直接その場で属性を補完しない。

1. last trusted snapshotを読む
2. 休眠期間にそのentityへ届く既知EVT・外生変化を確認する
3. historical / institutional / physical constraintsを適用する
4. unknownは`UNRESOLVED`のまま残す
5. current story timeへstateを再構成する
6. lifecycle statusを`ACTIVE`へ戻す

休眠中の出来事を、本文都合で後付けした既成事実として作らない。

## 5. Checkpoint snapshot

本repoはevent sourcingを基本とするが、復元のために全deltaを無限に再生し続ける必要はない。

checkpointは**圧縮キャッシュ**であり、過去EVTの代替正本ではない。

checkpoint作成を検討する目安:

- 一つのentityについて関連deltaがおおむね10〜20件を超えた
- state fileが読み直しに不向きな大きさになった
- 大きな時代・所属・場所の切替が成立した
- 長期休眠へ移す前に安定した復元点が必要

現段階では件数閾値を機械的な必須条件にはしない。EVT-015〜020程度まで運用実績を集めてから調整する。

checkpointには少なくとも、

- story time
- event head
- authority inputs
- materialized state
- unresolved items
- checkpoint以後に読むべきdelta起点

を記録する。

## 6. 禁止

- DORMANT化を理由に過去履歴を削除する
- DORMANT entityを「存在しない」と扱う
- 再展開時に未来情報を混入する
- checkpointで元EVTのprovenanceを消す
- state fileを短くするためだけに重要な不確実性を捨てる
- 物語上の退場と制作上のDORMANTを同一視する

## 7. 目的指標

この運用の目的は完全simulationではなく、

- current resolution scopeを小さく保つ
- 過去の因果を追跡可能にする
- 必要なentityを正しく再展開できる
- 長期連載でも復元コストを制御する

ことである。
