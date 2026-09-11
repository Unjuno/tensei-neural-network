# 現在の状態

更新: 2026-09-12
このファイルは索引。直接のEVT・state・検証結果を優先する。

## 作業と公開の境界

- branch: `work/story-bootstrap`
- story head: `EVT-015`
- 現代側event head: none
- main / PR / docs / 公開には触れていない
- 第1〜4話: `PREPUBLICATION_GATE_PASSED`
- 独立実読者試読 / Human Review: 未実施

## Story state

active: PER-005 高橋修一 / PER-006 佐伯玲子 / ORG-001。

`world.md`等の古いsnapshotへ戻らず、EVT-008〜015と対応deltaをoverlayする。

EVT-014:

- Q one-bit neighbors 16 × cyclic orders 16 = 256 locked trials
- Q=112, M1=M2=M3=48, nonconverged=0
- unanimous positionsのflipは全orderでQへ復帰
- split positionsはorder-dependent
- Qへ戻らないtrialはcoordinate-minority stored patternへだけ到達

EVT-015:

- split flip: minority memory distance 4→3 / overlap 8→10、他二つdistance 4→5 / overlap 8→6
- unanimous flip: 三つともdistance 4→5 / overlap 8→6

人物Knowledgeはここまで。第5話は未成立。

## Author research — storyへ自動漏洩禁止

EXP-006:

- 256 eligible N=16/P=3 triples
- 65,536 trajectories
- primary Hは弱いSUPPORT
- secondary: split non-Q 17,488/17,488がcoordinate-minority stored patternへ到達

EXP-007:

- preregistered counterexample search
- N=8,12,16,20,24
- 640 eligible triples / 362,704 trajectories
- non-Q 111,680 / counterexample 0

その後、`research/reports/EXP-007.md`で解析した。

**記載した仮定内ではcoordinate-minority escapeを証明できた。**

proof assumptions:

- P=3 componentwise-majority Q
- Qはstored patternsと異なり、nonzero-margin stable
- symmetric Hebbian weights / zero self coupling
- asynchronous one-unit update
- zero field保持

Gauge後の4 coordinate types U/A/B/Cを使うと、split A-typeを1bit反転したtrajectoryではU/B/CはQ stabilityにより反転不能。A-typeのmixed stateもfixed pointになれず、Hopfield energy下降からfinalはQまたはstored pattern Aだけになる。

これは作者側proofであり、PER-005/PER-006は知らない。

## Roadmap

自律的に実施可能だった項目:

- 既存4話の整合・再現・workflow integrity
- reader-loss編集simulationと改稿
- EVT-015までのworld advancement
- story observation → preregistered author experiment → falsification search → analytic proof

外部主体が必要でOPEN:

1. 5人以上の独立実読者試読
2. Human Review / 公開受理
3. 別主体によるfresh restore / action-selection評価

同一AI内simulationでこれらをPASS扱いしない。

詳細: `notes/roadmap-progress-2026-09-12.md`。

## 次の優先

Story側はEVT-015現在stateだけから進める。作者側proofを人物へ注入しない。

人物が256 trialを実行した過程を章へ投影する必要が生じる場合は、1984〜85年の共用計算機・OS・言語を一次/機関史料で具体化する。

Author research側は同じ定理のtrialを増やさず、P>3 / synchronous update / zero-field rule変更等、どの仮定で破れるかを必要に応じて調べる。

## 残る未確定

研究所の所在地・部門・職位・設立細部、具体年月日、共用計算機・OS・言語、人物の生活史、研究所の将来、現代側最初のevent、第5話以降。

## 検証系

chapter verificationに加え、EXP-006/007の保存結果をCIで再計算照合する。Human ReviewはCIとは別。
