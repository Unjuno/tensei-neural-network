# 知見

実験・追試・調査から、現時点で言えることを管理します。

仮説やアイデアとは分離します。

## 状態

- `PROVISIONAL`: 暫定的な知見
- `REPLICATED`: 独立または追加条件で再確認された
- `CONTESTED`: 有効な反証・矛盾する証拠があり、現在の主張範囲をそのまま維持できない
- `SUPERSEDED`: より新しいFindingが同じ論点をより適切に表現し、現在の解釈を置き換えた

## 状態遷移

- 新しいFindingは原則 `PROVISIONAL` から開始する
- 同じ主張が別run、別seed、別実装、追加条件などで意味のある再確認を受けた場合、根拠を明記して `REPLICATED` にできる
- 既存Findingと両立しない有効な証拠が1件でも見つかり、単純な実行失敗として棄却できない場合は、原因解明まで `CONTESTED` とする
- 新しいFindingが古いFindingの主張範囲を明示的に置き換える場合、古いFindingを削除せず `SUPERSEDED` とし、後継Finding IDを記録する

`CONTESTED` は「誤りと確定」、`REPLICATED` は「真と確定」を意味しません。

## 記録形式

```markdown
## F-001 知見の題名

状態: PROVISIONAL

### 現在言えること
証拠が支持する範囲だけを書く。

### 根拠
- EXP-...
- REF-...

### 反証・矛盾する証拠
- EXP-...（ある場合）

### 言えないこと
この結果だけでは結論できない内容。

### 関連
- Q-...
- H-...
- L-...
- 小説章

### 置換関係
- SUPERSEDEDの場合: 後継 F-...
```

## 矛盾する新証拠が出た場合

既存Findingを結果に合わせて黙って書き換えません。

1. 新しい実験自体の有効性を確認する
2. 既存Findingと両立しない有効な証拠なら `CONTESTED` にする
3. 必要なら仮説を `INCONCLUSIVE` に戻す
4. 追加検証後、主張を修正する必要があれば新しいFindingを作り、旧Findingを `SUPERSEDED` にする

## F-001 低負荷の二状態Hopfield実装で中核的な連想記憶挙動を再現した

状態: PROVISIONAL

### 現在言えること

EXP-001の事前定義条件（N=100, P=3, 対称Hebbian重み, 自己結合なし, 閾値0, 非同期更新）では、固定seedから生成した3個の保存パターンはすべて固定点になった。

各保存パターンについて20%のbitを反転したcueを50回ずつ、合計150 trialで評価したところ、150/150 trialが対象パターンへ完全復元した。全trialが2 sweeps以内に停止し、追跡した非同期更新で `ΔE > 1e-10` のenergy increaseは0回だった。

したがって、この限定条件ではHopfield (1982) の中核的なcontent-addressable memoryの挙動――安定状態、破損cueからのpattern completion、非増加energy――を小規模な現代実装で再現できた。

### 根拠
- EXP-001: `experiments/EXP-001-hopfield-core/`
- 集計結果: `experiments/EXP-001-hopfield-core/results/summary.json`
- REF-001: Hopfield (1982)
- REF-002: Hopfield (1984、補助的文脈)

### 反証・矛盾する証拠
- 現時点では登録なし

### 言えないこと

この結果だけから次は言えない。

- Hopfield networkの一般的なstorage capacityがどの値であるか
- 20%より大きいnoiseでも同じ成功率になること
- 保存パターン数や相関を変えても同じ挙動になること
- graded-response modelでも同一条件・同一数値になること
- 生物学的な記憶がHopfield modelそのもので実装されていること
- AIや人間の意識・自己同一性がattractor dynamicsだけで説明できること

### 関連
- Q-001
- H-001
- L: 未登録
- 小説章: 未定

### 置換関係
- なし
