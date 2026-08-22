# 現在の状態

このファイルは詳細な正本ではなく、現在位置を示す索引です。

更新: 2026-08-23

## フェーズ

- 主目的: 小説
- 物語段階: `起 / 承 / 転`
- 本文: 第1話ドラフト `novel/chapters/001.md` 成立。採用範囲はEVT-001〜004
- 学習段階: CATCH_UP
- 研究段階: Hopfield系EXP-001〜005まで実施
- 生成方式検証: `PARTIAL PASS`
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

高橋・佐伯の所属先としてORG-001をPROVISIONALに固定した。具体所在地、職位、部門名、機種、親会社の詳細は未確定。

親会社「光陵化学株式会社」は現在、独立した制度判断をevent上で必要としていないためORG化せずworld entityのまま。

## 組織主体モデル

個人personaだけでは扱えない制度的因果を管理するため、`ORG-xxx` を導入した。

ORG化するのは、独立した

- Mission
- Resources
- Governance / Policies
- Membership
- Institutional memory
- External relations

が後続因果へ効く組織だけ。

会社・大学・学会・部署を背景に出ただけでは機械的にORG化しない。

管理先:

- 定義: `novel/organizations/`
- 時系列state: `novel/state/organizations/`
- 初期化手順: `novel/organizations/INITIALIZATION.md`
- world/persona/organization resolver: `novel/environment.md`

BOOT-002はworld + persona + organizationを同じ同期キーへ投影する形へ更新済み。

重要な境界:

- 組織を巨大personaとして擬人化しない
- 個人のBeliefと組織の公式Missionを同一視しない
- 私的ノートを自動的にInstitutional memoryへ入れない
- 組織内部の未公表判断を所属personaへ自動共有しない
- 将来の合併・再編・閉鎖を1980年代の初期stateへ未来知識として入れない

## 歴史的モデル

ORG-001は特定の実在研究所の別名ではない。

史実上の制約として、1971年設立・2010年解散の三菱化成／三菱化学生命科学研究所など、企業が長期基礎研究へ投資した実例を参照する。

1980年代は日本企業が基礎研究へ進出した時期であり、1990年代以降には企業研究所の名称・mission・組織構造が変化した実例がある。ただしORG-001が将来どうなるかはfuture eventとしてのみ解決する。

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

## 第1話ドラフト

`novel/chapters/001.md`

採用event範囲: `EVT-001`〜`EVT-004`

高橋修一・佐伯玲子の名前とpersona差は反映済み。

次の文学的改稿では、ORG-001という所属環境を本文に入れることが可能になった。ただし研究所の設備・所在地・制度を本文都合だけで捏造せず、必要な細部は歴史調査後に追加する。

## 研究分岐

- EVT-001 → Q-003 / H-003 / EXP-003 / F-003
- EVT-002 → Q-004 / H-004 / EXP-004 / F-004
- EVT-006 → Q-005 / H-005 / EXP-005 / F-005

EXP-005はFAIL、H-005はNOT_SUPPORTED。

## 次に物語側で行うこと

ORG-001を導入したことで、次から個人だけでなく制度的制約もevent因果へ入れられる。

候補はプロットではなく、現在stateから生じ得るもの:

- 共用計算資源を本当に使う段階で設備・利用手続きが必要になる
- 研究テーマを正式化すると研究所内の承認・記録が発生する
- 高橋の私的ノートと研究所の公式記録が分岐する
- 将来の経営・研究政策変化が人物に観測された時点でorganization stateが動く

EVT-007後の局所問題は引き続き、符号反転fixed point、nonstored分類、model対称性とmemory解釈。

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