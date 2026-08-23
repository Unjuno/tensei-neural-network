# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-23

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話 `novel/chapters/001.md` を階層World State反映版へ改稿。採用範囲はEVT-001〜004
- 第1話最小因果骨格: `novel/chapters/001-outline.md`
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜005まで実施
- 生成方式検証: `PARTIAL PASS`
- World model: persona中心モデルからtyped hierarchical entity/state graphへ拡張
- 公開段階: GitHub Pagesは `main /docs`。今回のBootstrap / EVT / 第1話ドラフト / EXP-003以降は未公開

## branch

`work/story-bootstrap`

`main` には反映していない。PRも作成しない。

## 1980年代側

開始同期点:

`BOOT-002 @ T0-1980S @ none`

current event head:

`EVT-007`

### Active personas

- PER-005 — **高橋修一**。日本人、30代後半、数理工学・理論物理寄りから神経回路・連想記憶へ越境
- PER-006 — **佐伯玲子**。日本人、30代半ば〜後半、神経生理学・biophysics寄り

### Active organization

- ORG-001 — **光陵化学生命科学研究所**。1970〜80年代日本の企業基礎研究所文化をモデルにした架空の企業系生命科学研究所

高橋・佐伯の所属先としてORG-001をPROVISIONALに固定。具体所在地、職位、部門名、機種、親会社の詳細は未確定。

親会社「光陵化学株式会社」は現在、独立した制度判断をevent上で必要としていないためORG化せずworld entityのまま。

## 階層World Entity / State Model

人物だけを状態主体とせず、物語因果へ必要な対象をtyped entityとして扱う。

概念階層:

```text
Universe / physical regime
└─ world / global environment
   ├─ nation / jurisdiction / economy / culture
   │  └─ organization / institution
   │     └─ group / laboratory / household
   │        ├─ person / AI
   │        ├─ animal / pet
   │        └─ object / device / document
   ├─ location / infrastructure
   └─ natural / information environment
```

実装は木ではなくtyped hierarchical graph。

定義:

- `PER`: person / AI agent
- `ANI`: animal / pet
- `OBJ`: object / device / document / sample
- `ORG`: organization / institution
- `GRP`: laboratory / household / team
- `LOC`: location
- `POL`: nation / jurisdiction
- `ENV`: natural / economic / information environment
- `SYS`: infrastructure / communication / computation system
- `PHY`: physical constraints

詳細: `novel/entities/README.md`

State管理: `novel/state/README.md`

### 重要原則

- すべてをID化しない。後続因果に独立state履歴が必要になった対象だけ展開する
- 上位contextから下位entityへconstraintは伝播するが、knowledgeは自動伝播しない
- 因果はdownward / upward双方へ流れる
- 人物の行動がなくても歴史・経済・法・天候・設備故障等のexogenous eventでworldは進む
- 全宇宙を毎step解決せず、現在eventへ因果的に届く`resolution scope`だけ高解像度化する
- 解決されたfactはlocal / institutional / public / canonを区別する
- 小説本文はWorldStateのNarrativeProjectionであり、本文自体をworld-state正本にしない

## Bootstrap

`novel/bootstrap/README.md` を階層entity discoveryへ一般化済み。

今後の初期化:

```text
story time / parent head
→ global context
→ entity discovery
→ relation discovery
→ entity-specific projection
→ hierarchical constraint resolution
→ leakage check
→ synchronized WorldState
```

BOOT-002では現在、world + ORG-001 + PER-005を初期同期し、PER-006はEVT-002で独立persona stateとして成立する。

## EVT-001〜004

- EVT-001: 高橋が「止まることと、戻ることは同じか」を記録
- EVT-002: 佐伯が`correct recall`のtargetを誰が定義するか問い返す
- EVT-003: A/B等距離cueと観測protocolを作成
- EVT-004: 6-unit toy networkで同一cue・weightsからupdate orderだけの差でA/Bへ分岐する例を観測

EVT-004は数理的一貫性は確認済みだが、resolver provenanceは `UNBLINDED`。

## EVT-005〜007

- EVT-005: 6 cyclic update ordersを結果前lock。A/B/Dへ分岐
- EVT-006: balanced cue全6種類 × 6 orders = 36 trialsをpre-lock
- EVT-007: 全64 initial states × 6 orders = 384 trialsを列挙。Dは `-C` と再分類。fixed pointsは `A/B/C/-A/-B/-C`

これらは第1話へ遡及追加しない。

## 第1話

本文:

`novel/chapters/001.md`

最小因果あらすじ:

`novel/chapters/001-outline.md`

採用event範囲:

`EVT-001`〜`EVT-004`

2026-08-23改稿で階層World Stateの影響をNarrativeProjectionへ反映した。

- 舞台としてORG-001を明示
- 高橋と佐伯が異分野の企業基礎研究者として同じ制度環境で議論できる理由を本文へ組み込んだ
- 文献環境・共用計算資源を説明用設定ではなく、研究行動の可能性と制約として描写
- paper modelを手計算することを、共用計算資源以前に完全に追跡できる最小検査として位置づけた
- 高橋の私的ノートとORG-001のinstitutional memoryを分離し、第1話末で「まだ公式記録ではない」と明示
- ORG-001の将来の再編・閉鎖は未来知識として本文へ入れていない

本文からOBJ/LOCの恒常設定を増殖させない。ノート、紙上計算、研究室等は現時点ではscene realizationとし、来歴・保存・物理状態が後続因果へ効く時点で独立entity化する。

## 研究分岐

- EVT-001 → Q-003 / H-003 / EXP-003 / F-003
- EVT-002 → Q-004 / H-004 / EXP-004 / F-004
- EVT-006 → Q-005 / H-005 / EXP-005 / F-005

EXP-005はFAIL、H-005はNOT_SUPPORTED。

## 次に物語側で行うこと

第1話のNarrativeProjectionは階層World Stateへ接続した。

次のworld advancementでは、EVT-007後の状態からresolution scopeを決め、人物だけでなく必要ならORG / OBJ / SYS / 上位contextを含めて次eventを解決する。

現在の局所問題:

- `x`と`-x`のfixed-point対称性をweight/update ruleからどう説明するか
- `nonstored stable`を符号反転・mixture・その他へどう分けるか
- model対称性とmemoryとしての意味をどう分離するか
- toy modelから計算機実装・より大きな条件へ進む必要が人物側で成立するか
- その際、共用計算資源を独立`SYS` / `OBJ` stateへ展開する必要があるか

## 未確定

- ORG-001の具体所在地・設立年・所長・研究グループ構成
- 高橋・佐伯の具体職位・年齢
- 具体年月日
- 計算機・OS・programming language
- 二人の正式な上下関係
- ORG-001の将来の再編・閉鎖過程
- 現代側最初のevent
- 第2話以降の切れ目

必要になるまで一括固定しない。
