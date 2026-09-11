# ロードマップ進捗 — 2026-09-12

基準: `notes/assessment-and-roadmap.md`。

## 結論

自律的に検証できる短期項目はかなり進んだ。一方、ロードマップ全体を「解決済み」にすることはできない。独立実読者、Human Review、別主体による独立restore/action-selectionは外部主体を必要とするためである。これらを同一AIのsimulationで代替してPASS扱いしない。

## 短期

### 既存4話の証拠と文章

状態: `PASS WITH EXTERNAL READER BLOCKER`

- chapter verification再実行可能
- review-lockで本文と証拠の対象版を追跡
- 読者ロス編集simulation実施
- 第2〜4話を改稿後に再gate
- CIでchapter experiments / workflow integrityを検査

未完: 独立実読者による理解・人物関心評価。

### Restore

状態: `PARTIAL PASS`

repo内のdirect EVT / state delta / STATUS / timeline / structureをEVT-015まで同期。古いsnapshotへ巻き戻さない規則は明文化済み。

未完: 別主体が何も知らない状態から同じhead・active entities・未確定事項を復元できるかの独立評価。

## 中期

状態: `BLOCKED ON EXTERNAL READERS`

5人以上の小規模試読は未実施。AIによるreader-loss auditは質問設計と編集仮説の準備であり、読者データではない。

## 制作基盤

状態: `PARTIAL`

- 数理event / chapter verification: 実運転済み
- story observation → author research branch: EVT-014/015 → EXP-006/007で実運転
- empirical finding → preregistered falsification → analytic proof: 今回初めて一周した
- 組織・制度の独立判断: まだ弱い
- 具体的machine / OS / language: 因果上必要になるまで未固定
- 長期entity lifecycle: policyはあるが多数entity運転は未検証

## 今回の新規実験

### EVT-014 / EVT-015

story側でQの一ビット近傍を結果前lockして256 trial。Q=112、M1/M2/M3各48。split flipのescapeはcoordinate-minority stored patternのみ。

### EXP-006

事前登録一般化テスト。256 eligible N=16 triples / 65,536 trajectories。

primary Hは弱いSUPPORT。secondaryで17,488/17,488 split non-Q trajectoriesがcoordinate-minority stored patternへ到達。

### EXP-007

secondary findingの反例探索。N=8,12,16,20,24、640 eligible triples、362,704 trajectories。111,680 non-Q trajectoriesで反例0。

実験単体の結論は`NO_COUNTEREXAMPLE_IN_SEARCH`。

## 面白い発見と解析解決

EXP-007後、trial数を増やさず代数へ戻った。

`research/reports/EXP-007.md`で、次の仮定下にcoordinate-minority escapeを証明した。

- P=3
- Qはcomponentwise-majorityでstored patternsと異なる
- Qはnonzero-margin stable
- symmetric Hebbian weights / zero self coupling
- asynchronous one-unit update
- zero fieldは保持

Qでgauge変換するとcoordinateはU/A/B/Cの4typeになる。A-typeを1bit反転したtrajectoryではQ stabilityからU/B/Cのfieldが常に正で、A-type以外は反転できない。A-typeに正負が混在するstateはpositive/negative unitのfieldが6だけずれるためfixed pointになれない。Hopfield energyは実flipごとにstrictly減少するので、finalはQまたはA-type全反転、すなわちcoordinate-minority stored patternだけになる。

したがってEXP-006/007の経験的規則は、**記載した仮定内では解析的に解決した**。

次は同じ現象のtrialを増やすのではなく、仮定を一つずつ外したときどこで破れるか、またはstory側人物が自分の具体例からどこまで独立に導けるかが候補。ただし作者側proofを人物へ注入しない。

## 外部依存blocker

1. 5人以上の独立実読者
2. Human Review / 公開受理
3. 別主体によるfresh restore / action-selection

これらが未実施のため、長期ロードマップ全体は`OPEN`。
