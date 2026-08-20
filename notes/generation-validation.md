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

## 次の検証課題

EVT-004後の次の重要な結果解決について、ACTION_LOCKED → commit → RESOLVEDを実際に行い、同じ程度に自然な物語を生成できるかを確認する。

成功条件は「面白い結果が出ること」ではない。

**lockedした人物行動と世界条件から、どの結果が出ても受け入れ、その結果から次の状態へ進めること**を確認する。