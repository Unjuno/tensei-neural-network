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

## F-001 低負荷の二値Hopfield networkで乱れたcueから保存パターンへの回復を確認

状態: PROVISIONAL

### 現在言えること
EXP-001の宣言条件では、100ユニットに5個の固定二値パターンをHebbian outer-productで保存し、非同期更新したHopfield networkは、10%および20%のbitを反転したcueから元の保存パターンへexact recallした。

- 10% noise: 100/100 trials exact recall
- 20% noise: 100/100 trials exact recall
- 200/200 trialsが収束
- 最大observed sweeps: 2

したがって、**低負荷かつ今回の固定pattern setという条件では、保存パターンがattractorとして働き、乱れた状態から元の記憶状態へ戻るcontent-addressable recallを実装上確認した**と言える。

### 根拠
- EXP-001 — 事前基準PASS
- REF-001 — Hopfield (1982)

### 反証・矛盾する証拠
現在なし。

### 言えないこと
- Hopfield networkが任意のpattern setや任意のnoise率で同様に回復すること
- 容量限界付近でも同じ性能を保つこと
- 20%を超えるnoiseでも回復すること
- 欠損cue、構造化noise、連続値ニューロンでも同じ結果になること
- この実験が人間の記憶機構を説明したこと
- LLMの内部記憶・人格・意識がHopfield networkと同じ機構であること
- 原論文の全条件を完全に再現したこと

### 状態判断
独立実装・別seed・追加条件による再確認はまだないため `REPLICATED` には上げず、`PROVISIONAL` とする。

### 関連
- Q-001
- H-001
- EXP-001
- L-001
- 小説章: 未定

### 置換関係
なし。

## 現在

F-001が最初の正式Finding。次のExtensionでは負荷またはnoiseを広げ、回復が崩れる境界とspurious attractorの出現を測る候補とする。
