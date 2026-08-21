# 物語生成方式の検証

このファイルは、ペルソナ駆動・world resolver・event sourcing・episode projectionによる物語生成方式そのものの検証結果を記録する。

小説本文やCanonの正本ではない。生成方式について何が確認でき、何がまだ確認できていないかを分離するための検証台帳。

## Test-001 別セッションから第1話ドラフトまで再開

実施日: 2026-08-21

対象branch: `work/story-bootstrap`

対象範囲:

- repoから1980年代側の状態を復元
- stale indexがあれば直接event/stateからcurrent headを復元
- PER-005 / PER-006とworldを進める
- 成立済みeventを第1話へNarrativeProjectionする

### 確認できたこと

| 項目 | 判定 | 備考 |
| --- | --- | --- |
| repoだけから状態復元 | PASS | stale indexから巻き戻さずEVT-003を開始headとして復元できた |
| persona情報境界 | PASS | PER-005 / 006へ現代側EXP-004の統計値を直接与えていない |
| world / persona state同期 | PASS | EVT-004までstate / timeline / structureを同期できた |
| personaを必要時だけ追加 | PASS | PER-007を機械的に追加しなかった |
| 小説と研究の分離 | PASS | EVT-003 / 004から重複EXPを自動生成しなかった |
| 一話=一実験の回避 | PASS | 第1話はEVT-001〜004を材料に成立 |
| NarrativeProjection | PASS | event/stateから研究レポート形式ではない第1話ドラフトを作成できた |
| EVT-004の数理的一貫性 | PASS | 記載されたHebbian結合・cue・update orderを再計算し、order α→A、order β→Bを再確認 |
| environment resolverの結果独立性 | INCONCLUSIVE | 下記selection biasを排除できない |

## Test-001で見つかった重要な弱点

EVT-004より前に、作者側・生成側はすでにEXP-004で「等距離cueがupdate orderだけでA/Bへ分岐し得る」ことを知っていた。

しかしEVT-004では、次の結果依存性を持ち得る自由度が、結果を見る前にrepo上で固定された記録がない。

- A / B / Cの具体pattern
- balanced cueの具体値
- order α / βの具体順序
- どの候補例を採用するかというselection rule
- 何回試し、どの結果をevent化するかというstopping / inclusion rule

したがって、EVT-004の計算結果自体は正しいが、**この反例がunbiasedなenvironment resolutionから自然に出たことの証拠にはならない**。

これは人物への未来知識漏洩とは別問題である。

PER-005 / 006がEXP-004の122/200を知らなくても、生成者・resolver側がその結果を知った状態で、反例が出やすい条件を選んだ可能性を排除できない。

### EVT-004の検証上の扱い

- 物語event候補として: 有効
- 数理的な具体例として: 有効
- 第1話ドラフトの材料として: 有効
- 「完成プロットなしでresolverも結果非依存に動いた」ことの証拠として: **INCONCLUSIVE**

EVT-004を削除したり、結果を無効化したりはしない。

## 次回以降の解決前ロック

物語上の結果に複数の自由度があり、生成者が作者側の研究結果・未来候補を既に知っている場合、重要なeventは次の二段階で処理する。

### Phase 1: ACTION_LOCKED

結果を計算・検索・観測する前に、同じ `EVT-xxx` ファイルを `ACTION_LOCKED` としてcommitする。

最低限固定する:

- parent event head / story time
- 各personaが実際に観測している入力
- personaが選んだ行動
- 結果へ影響する具体条件またはその選択規則
- trial集合 / update rule / stopping rule / inclusion rule
- resolverが利用してよい情報源
- personaには見えない作者側研究結果など、action selectionへ使ってはいけない情報
- 結果解決方法

この段階ではoutcomeを書かない。

### Phase 2: RESOLVED

ACTION_LOCKEDのcommit後にenvironment resolverが結果を解決する。

- locked条件を結果を見て変更しない
- 規定したtrialは都合の悪いものも含めて全て扱う
- 望ましい結果が出なければ、その結果をそのまま採用する
- 結果を見て別条件へ差し替えた場合は、そのeventをclean validationとして数えない

## 生成側が既知の研究結果を持っている場合

同じAI/sessionが、personaには見えないEXP結果を既に読んでいること自体はあり得る。

その場合、personaの具体的な実験条件・入力値を選ぶ自由度が結果へ効くなら、次のどちらかを使う。

1. story-visibleな情報だけから導出できるdeterministic selection ruleを事前固定する
2. 結果知識を与えない別contextでaction / parameter selectionを行い、commitしてからresolverへ渡す

例:

- event IDから固定seedを導出する
- 候補を辞書順で最初から使う
- personaが明示したruleで全候補を列挙し、都合のよい例だけを選ばない

「反例が出るものを探す」は、人物がその探索目的を実際に持ち、探索範囲・停止条件を事前に固定している場合を除き、cleanなresolver検証には使わない。

## Resolution provenance

重要eventには、生成方式の検証用に次のprovenanceを記録できる。

- `LOCKED`: outcome-sensitiveな選択を解決前に固定し、その後変更していない
- `UNBLINDED`: 結果知識を持つ生成contextで条件選択が行われ、解決前lockがない。物語eventとしては使えるがclean validationには数えない
- `AUTHOR_CONDITIONED`: 人間作者または生成側が望む結果・演出へ向けて条件を意図的に固定した。介入として明記し、創発eventと偽装しない

Test-001のEVT-004は `UNBLINDED` とする。

---

## Test-002 ACTION_LOCKED → resolver → RESOLVEDを実行

実施日: 2026-08-21

対象event: `EVT-005-lock-the-order-family.md`

Action-lock commit:

`59ff6530d202b79834afbe8ffdceee1256437315`

### 検証目的

Test-001で未確認だったenvironment resolverの結果独立性について、少なくとも一つの重要eventを

```text
persona action selection
→ outcome-sensitive conditionsを外部化
→ commit
→ resolver
→ 全結果をそのまま受理
```

の順で処理できるか確認する。

成功条件はA/B分岐や面白い結果が出ることではない。

**lock後にどのoutcomeが出ても条件を差し替えず、その結果をworld/persona stateへ返せること。**

### Action lockで固定したもの

EVT-004で成立済みの6-unit networkをそのまま使い、update orderだけについて、unit番号の自然順序

```text
(1,2,3,4,5,6)
```

の全6 cyclic rotationsを検査集合として固定した。

```text
r1 = (1,2,3,4,5,6)
r2 = (2,3,4,5,6,1)
r3 = (3,4,5,6,1,2)
r4 = (4,5,6,1,2,3)
r5 = (5,6,1,2,3,4)
r6 = (6,1,2,3,4,5)
```

あわせて、

- 同じcueから開始
- 同じHebbian weights
- zero fieldなら現在値保持
- 一つのorderを1 sweepとして反復
- 変化のない1 sweepでstable
- 最大20 sweeps
- 6本すべてを含める
- A/B以外も削除しない

を結果前に固定した。

EXP-004の数値結果、第2話の都合、A/Bを再現したいという期待をaction selectionへ使わないことも明記した。

### Resolution結果

lock後に6本だけをexactに解決した。

```text
r1 -> A
r2 -> D (OTHER_STABLE)
r3 -> B
r4 -> B
r5 -> D
r6 -> D
```

D:

```text
(+1,+1,+1,+1,-1,+1)
```

- A: 1 / 6
- B: 2 / 6
- C: 0 / 6
- OTHER_STABLE: 3 / 6
- NONCONVERGED: 0 / 6

すべて2 sweeps目でstable判定。

DはA/B/Cのどれとも一致せず、Hamming distanceはA=2、B=2、C=6。

### Test-002判定

| 項目 | 判定 | 備考 |
| --- | --- | --- |
| actionをoutcome前に外部化 | PASS | ACTION_LOCKED版をcommit |
| outcome-sensitiveなorder集合の固定 | PASS | 6 cyclic rotationsを先に固定 |
| stopping / inclusion ruleの固定 | PASS | max20、全6本記録 |
| lock後の条件差し替え回避 | PASS | order追加・削除なし |
| 不都合・非期待結果の保持 | PASS | Dを3件すべて保持 |
| world/persona stateへの反映 | PASS | EVT-005とPER-005/006/worldへ同期 |
| cleanなresolver手順の実行 | PASS | EVT-005のResolution provenance=`LOCKED` |

### 解釈上の限界

Test-002のPASSは、

- この6-unit networkが一般的である
- A/B/Dの比率が一般的である
- biological memoryが同じ性質を持つ
- 物語全体に作者バイアスがない

ことを意味しない。

確認できたのは、**一つの重要eventについて、結果前に条件をcommitし、結果を選別せず受け入れる制作手順が実際に機能した**ことだけである。

また、action ruleそのものは同じ生成contextで作られているため、より強い検証をしたい場合は、action selectionを作者側結果から隔離した別contextへ分離するテストが残る。

## 現在の総合評価

- state recovery: PASS
- persona information boundary: PASS
- world/persona同期: PASS
- persona必要時生成: PASS
- 小説/研究分離: PASS
- 一話=一実験回避: PASS
- NarrativeProjection: PASS
- 未確定恒常属性を本文で勝手に固定しない規則: 導入済み
- resolver pre-lock mechanism: **PASS on Test-002**
- action selector自体のcontext isolation: **未検証**

したがって、生成方式はTest-001時点の`PARTIAL PASS`から一段進んだが、完全にbias-freeだとは扱わない。

## 次の検証課題

必要になった次の重要eventで、action / parameter selectionを作者側の研究結果を見ない別contextへ分離するか、story-visible情報から一意に決まるdeterministic ruleだけを使い、selector-levelの独立性を検証する。

その場合も成功条件は「面白い結果」ではなく、**結果を知らずに選んだactionから生じたoutcomeを、そのまま物語へ受け入れられること**とする。