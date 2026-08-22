# 組織state

時間に依存する組織状態を管理する。

`novel/organizations/ORG-*.md` は定義・baseline、ここはstory timeごとの制度的state。

各snapshotには最低限、

- Bootstrap / synchronization key
- story time / event head
- Mission
- Resources
- Governance / Policies
- Membership
- Institutional memory
- External relations
- Situational state
- personaへ実際に観測可能な情報

を必要な範囲で記録する。

個人personaと同様、変化しない項目は継承してよい。eventごとに全組織を複製しない。

組織が再編・統合・解散しても過去stateを消さない。後継組織が独立した制度的記憶・目的を持つ場合は新しい `ORG-xxx` としてforkし、継承関係を記録する。