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
- 組織・制度の独立判断: まだ弱い
- 具体的machine / OS / language: 因果上必要になるまで未固定
- 長期entity lifecycle: policyはあるが多数entity運転は未検証

## 今回の新規実験

### EVT-014 / EVT-015

story側でQの一ビット近傍を結果前lockして256 trial。Q=112、M1/M2/M3各48。split flipのescapeはcoordinate-minority stored patternのみ。

### EXP-006

上記を作者側で事前登録一般化テスト。256 eligible N=16 triples / 65,536 trajectories。

primary Hは弱いSUPPORT。secondaryで17,488/17,488 split non-Q trajectoriesがcoordinate-minority stored patternへ到達。

### EXP-007

secondary findingを支持する例集めではなく反例探索へ切り替えた。

N=8,12,16,20,24、640 eligible triples、362,704 trajectories。111,680 non-Q trajectoriesで反例0。

結論は`NO_COUNTEREXAMPLE_IN_SEARCH`でありproofではない。

## 面白い発見

P=3 majority mixture Qについて、split coordinateを一つ反転すると、そのcoordinateのminority stored patternだけが距離4→3へ近づき、他二つは4→5へ遠ざかる。

story掲載例だけでなくEXP-006/007の固定探索でも、Qへ戻らないtrajectoryはすべてこのminority stored patternへ収束した。

現時点の最も価値の高い次課題は、さらにtrial数を増やすことではなく、これを代数的に証明できる条件を探すこと。証明できなければ、どの仮定を崩すと反例が出るかを特定する。

## 外部依存blocker

1. 5人以上の独立実読者
2. Human Review / 公開受理
3. 別主体によるfresh restore / action-selection

これらが未実施のため、長期ロードマップ全体は`OPEN`。
