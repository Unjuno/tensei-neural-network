# WORLD_POLICY validation — EVT-008

## 対象

`novel/WORLD_POLICY.md` をEVT-007後のworld advancementへ初めて明示適用した。

対象event: `EVT-008-sign-inversion-symmetry.md`

## 判定

`PARTIAL PASS`

## 確認できたこと

### 1. Resolution scope

PASS。

現在の局所問題はzero-bias bipolar toy networkの符号反転対称性だったため、PER-005 / PER-006、既存network、ORG-001の研究環境だけを高解像度化した。

### 2. Lazy expansion

PASS。

階層モデルを導入したからという理由だけで、共用計算機をSYS/OBJ化したり、紙・ノート・親会社を独立entity化しなかった。

### 3. Constraint propagation / knowledge propagation分離

PASS。

ORG-001は研究行為を可能にする制度環境として作用したが、共同記録の内容を組織knowledgeへ自動共有しなかった。

### 4. Persona observation boundary

PASS。

PER-005 / PER-006はEVT-007までの観測と当時利用可能な数学だけから行動した。現代EXP-003〜005の結果は使用していない。

### 5. Action / resolution分離

PASS。

導出対象、三つのlocal-field case、energy check、停止条件をcommit `f02d78ddbec2b166fb4e1a346f6cf0e969cb8fc5` で先に固定し、その後に解決した。

### 6. Fact level

PASS。

導出はPER-005 / PER-006間のlocal factとして成立。ORG-001のinstitutional fact、public fact、canon factへ自動昇格させていない。

### 7. 新persona / entityの抑制

PASS。

新personaなし。新ORG/OBJ/SYSなし。

### 8. 未来プロット非依存

PASS。

第2話の結末・切れ目・驚きをaction selectionへ使っていない。EVT-007で成立したgoalから局所問題を一段だけ進めた。

## 残る問題

### State storage

`novel/state/personas/PER-005.md` 等が長大化しており、毎eventで単一ファイル全体を書き換える方式は運用コストが高い。

EVT-008ではappend-only deltaを

- `novel/state/personas/deltas/EVT-008.md`
- `novel/state/organizations/deltas/EVT-008.md`

へ保存した。

これはevent sourcingに近く、既存snapshot + event deltaからcurrent stateを復元できる。ただし、このdelta方式を正式ポリシーにするか、定期snapshot/compactionをどう行うかは未決定。

したがってWORLD_POLICY全体は`FULL PASS`ではなく`PARTIAL PASS`とする。

## 次の検証点

- state delta方式を正式化するか
- timeline / STATUS等のindex同期をどの頻度・粒度で行うか
- 実際にSYS/OBJの独立stateが必要になるeventでlazy expansionが機能するか
- exogenous eventを導入した場合も未来プロット化せず解決できるか
