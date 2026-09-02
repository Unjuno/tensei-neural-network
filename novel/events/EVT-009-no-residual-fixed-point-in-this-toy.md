# EVT-009 残ったものは、まだ何もない

状態: `RESOLVED / PROVISIONAL`

Resolution provenance: `LOCK_NOT_REQUIRED`

## Story time

`T0-1980S + residual classification after EVT-008`

## Timeline position

- Parent: `EVT-008`
- Previous event: `EVT-008`
- Next event: 未成立

## Resolution scope

今回、高解像度化するのは次だけ。

- PER-005 高橋修一
- PER-006 佐伯玲子
- EVT-007で既に全列挙済みの64-state table
- EVT-008で導出済みのglobal sign-inversion symmetry
- ORG-001内の局所的共同検討環境

新しいnetwork、pattern、update order、計算機、文献、第三者は導入しない。

## World before

EVT-008までに二人は、

- この6-unit toy networkの全64 initial states × 6 cyclic ordersを観測済み
- stable final stateが `A/B/C/-A/-B/-C` の6種類だけであることを観測済み
- `-A/-B/-C` がzero-bias bipolar update ruleのglobal sign-inversion symmetryでA/B/Cと対になることを導出済み
- 今後nonstored stateを扱うなら、符号反転対称性で説明できるstateを先に分離する、という局所目標を持つ

という状態にある。

## Story-visible action selection

PER-006は、新しい例を探す前に、既に全列挙した表から「符号反転で説明できるものを除いた残差」を実際に作るよう求める。

PER-005はEVT-007のstable final setを、

1. stored pattern: `A/B/C`
2. stored-pattern negation: `-A/-B/-C`
3. 上記以外

の三分類へ置き直す。

これは既観測データの決定的な再分類であり、結果を変え得るselection freedomや新規試行を含まない。そのためACTION_LOCKは要求しない。

---

# RESOLUTION

## 1. 既観測final setの再分類

EVT-007で観測済みのunique stable final setは、

```text
F = {A, B, C, -A, -B, -C}
```

である。

stored setを、

```text
S = {A, B, C}
```

とする。

EVT-008で説明済みのstored-pattern negation setは、

```text
-S = {-A, -B, -C}
```

である。

したがって、このtoy networkで今回「その他のstable final」と呼ぶ残差は、

```text
R = F \ (S ∪ -S)
```

であり、

```text
R = ∅
```

となる。

## 2. 何が分かったか

この結果は、一般のHopfield型networkにspurious stateが存在しないことを意味しない。

分かったのは、この特定の6-unit / 3-pattern / zero-bias / 現在のweight rule / 現在のupdate ruleについて、全64 initial statesを既に列挙した範囲では、stable final stateがstored patternとそのglobal sign inversionだけで尽くされていた、ということだけである。

EVT-005で「保存していない戻り先」と見えたDは、EVT-007で `-C` と判明し、EVT-008でその出現を対称性から説明できた。そこから対称性由来のstateを除くと、このtoy networkには調べるべき別種のstable finalが残っていない。

## 3. Persona interaction

高橋は表の余白に、

> 残差、なし。

と書く。

その直後に、

> なら、この模型では次を見られない。

と付け足す。

佐伯は「見つからなかった」を「ない」に言い換えないよう止める。ただし今回は全64 initial statesを列挙済みなので、**この固定されたtoy networkのstate space内**という限定を付ければ、その他のstable finalが存在しないことまで言えると確認する。

二人はここで、観測不足とmodel capacityの不足を分ける。

## Resolved consequence

- このtoy networkのstable final setは `S ∪ -S` で尽くされる
- 対称性で説明できるstateを除いたstable-final residualは空集合
- このnetworkのままmixtureやその他のspurious stable stateを探し続けても、新しいstable finalは出ない
- 「残差がない」はこの有限toy networkについての全列挙結果であり、一般のnetworkについての不存在主張ではない
- 次に別種のnonstored stable structureを調べるなら、network / stored patterns / coding / load等の条件を変える必要がある
- ただし、どの条件をどう変えるかはまだ決めていない

## Persona deltas

### PER-005 高橋修一

Beliefs:

- 現在の6-unit toy networkでは、stored patternとその符号反転を除くstable finalは残らない
- 小さい系を完全列挙したことで、観測を増やすだけでは答えられない問いが明確になった
- 次の問いにはmodel条件の変更が必要だが、結果を見て都合のよい条件を選んではならない

Goals:

- 別種のnonstored stable structureを問うなら、変更する条件と判定基準を結果前に固定する
- まず当時利用可能な理論・文献から、どの構造が既知または予測されているかを確認する
- 必要な計算量が紙上追跡を超える場合にのみ、ORG-001の共用計算資源を具体化する

Memory:

- `R = F \ (S ∪ -S) = ∅`
- 「残差なし」は現在の有限toy networkに限定される

### PER-006 佐伯玲子

Beliefs:

- 「数学的対称性で説明できない残差があるか」というEVT-008後の問いには、このtoy networkでは「ない」と答えられる
- これは一般的不在ではなく、固定したmodelの全状態列挙による局所的不在である
- 次のmodelを選ぶ際には、見たい現象から逆算して都合よく条件を選ぶselection biasを避ける必要がある

Goals:

- 新しいmodel条件へ進む前に、問い・変更変数・停止条件・観測量を明示させる
- 文献上の既知現象と二人自身の新規観測を区別する

Memory:

- stable-final residualが空だったこと
- 全列挙だからこそ、このtoy network内では不存在まで言えること

## Organization / world delta

ORG-001のmission / resources / governanceに変更なし。

共同記録の分類は更新されたが、institutional memoryへの正式登録は未成立。

共用計算資源はまだ具体化しない。今回の再分類は既存表だけで完結したためである。

Fact level:

- local fact: PER-005 / PER-006の共同記録と共有knowledgeとして成立
- institutional fact: 未成立
- public fact: 未成立
- canon fact: 未昇格

## Who observed what

- PER-005 / PER-006: 再分類と残差空集合を共同確認
- ORG-001: 組織として内容を観測・承認したとは扱わない
- 他persona: 未観測
- 現代側persona: 未観測

## Research branch after resolution

新しいQ/H/EXPはまだ作らない。

EVT-009は新しい経験的結果を得る実験ではなく、EVT-007/008で既に成立した物語内データと対称性を再分類したeventである。

ただし次にmodel条件を変更する場合は、現実史上その時点で利用可能なspurious-state / mixture-stateに関する文献確認が物語行動を制約し得る。これは次eventのaction selection前に必要ならresearch branchとして切り出す。

## Structure impact

EVT-008後の問い、

> 数学的対称性で説明できるものを取り除いたあとに、まだ「記憶ではない安定状態」は残るのか。

には、このtoy networkに限って明確な答えが出た。

> 残らない。

そのため次のworld advancementは、同じ表をさらに眺めることでは進まない。

次eventはまだ固定しない。人物が文献へ戻るか、model条件を変更するprotocolを作るか、共用計算資源を必要とするかは、EVT-009後のstateと当時の環境制約から解決する。

## Generation validation

- EVT-008後のpersona goalsから、まず既観測結果の残差分類を選んだ
- 新規networkやparameterを結果都合で選ばなかった
- 全状態列挙済みなので、現在toy内の不存在と一般的不在を分離した
- 新しい結果選択を伴わない決定的再分類なのでACTION_LOCKを要求しなかった
- ORG / SYS / OBJを不要にentity化しなかった
- 現代EXP-003〜005の結果を人物へ漏洩させなかった
- EVT-010以降のplotを成立済みstateとして書き込まなかった
