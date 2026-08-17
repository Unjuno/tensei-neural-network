# 仮説

研究上の問いに対する、反証可能な仮説を管理します。

## 状態

- `PROPOSED`: 提案段階
- `TESTING`: 検証中
- `SUPPORTED`: 現在の証拠が支持している
- `NOT_SUPPORTED`: 現在の証拠では支持されない
- `INCONCLUSIVE`: 判定不能

`SUPPORTED` は「真である」と同義ではありません。

## 推奨記録形式

必要に応じて H/T/D/C/U 形式を使います。

- **H (Hypothesis)**: 反証可能な仮説。測定対象・条件・閾値・環境を明示する
- **T (Test)**: 最小の検証。データ、環境、必要サンプル数、停止条件を明示する
- **D (Decision)**: PASS / FAIL / UNCERTAIN
- **C (Counter / Alternative)**: 失敗モード、代替仮説
- **U (Uncertainty)**: 誤差要因、不確実性

## 現在

正式な仮説はまだ登録していません。最初の研究上の問いと原典確認の後に作成します。
