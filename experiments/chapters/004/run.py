#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

M1 = (1,1,1,1,-1,-1,-1,-1, 1,1,-1,1,-1,1,-1,-1)
M2 = (1,1,1,1,-1,-1,-1,-1, -1,-1,1,-1,1,-1,1,1)
M3 = (1,1,-1,-1,1,1,-1,-1, 1,-1,-1,1,1,-1,-1,1)
Q  = (1,1,1,1,-1,-1,-1,-1, 1,-1,-1,1,1,-1,-1,1)


def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def weights(patterns):
    n = len(patterns[0])
    return tuple(
        tuple(0 if i == j else sum(p[i] * p[j] for p in patterns) for j in range(n))
        for i in range(n)
    )


def local_inputs(state, w):
    return tuple(sum(w[i][j] * state[j] for j in range(len(state))) for i in range(len(state)))


def execute():
    patterns = (M1, M2, M3)
    component_sums = tuple(sum(p[i] for p in patterns) for i in range(16))
    majority = tuple(1 if c > 0 else -1 for c in component_sums)
    unanimity = sum(abs(c) == 3 for c in component_sums)
    splits = sum(abs(c) == 1 for c in component_sums)

    minority = Counter()
    for i, c in enumerate(component_sums):
        if abs(c) != 1:
            continue
        maj = 1 if c > 0 else -1
        for name, p in zip(("M1", "M2", "M3"), patterns):
            if p[i] != maj:
                minority[name] += 1

    q_distances = {name: hamming(Q, p) for name, p in zip(("M1", "M2", "M3"), patterns)}
    pair_distances = {
        "M1-M2": hamming(M1, M2),
        "M1-M3": hamming(M1, M3),
        "M2-M3": hamming(M2, M3),
    }
    overlaps = {name: dot(Q, p) for name, p in zip(("M1", "M2", "M3"), patterns)}

    w = weights(patterns)
    direct_h = local_inputs(Q, w)
    derived_h = tuple(8 * component_sums[i] - 3 * Q[i] for i in range(16))
    expected_h = (21,21,5,5,-5,-5,-21,-21,5,-5,-5,5,5,-5,-5,5)

    checks = {
        "evt012_majority_all_16": majority == Q,
        "evt012_unanimity_4": unanimity == 4,
        "evt012_split_12": splits == 12,
        "evt012_minority_balanced": dict(minority) == {"M3": 4, "M2": 4, "M1": 4},
        "evt012_q_distances_4_4_4": list(q_distances.values()) == [4, 4, 4],
        "evt012_pair_distances_8_8_8": list(pair_distances.values()) == [8, 8, 8],
        "evt013_overlaps_8_8_8": list(overlaps.values()) == [8, 8, 8],
        "evt013_direct_h_matches_expected": direct_h == expected_h,
        "evt013_derived_h_matches_direct": derived_h == direct_h,
        "evt013_all_signed_margins_positive": all(q * h > 0 for q, h in zip(Q, direct_h)),
    }

    return {
        "chapter": "004",
        "verification": "EVT-012 componentwise majority and EVT-013 overlap-to-stability derivation",
        "checks": checks,
        "evt012": {
            "component_sums": list(component_sums),
            "majority_matches_q": sum(a == b for a, b in zip(majority, Q)),
            "unanimity_positions": unanimity,
            "split_positions": splits,
            "minority_counts": dict(minority),
            "q_distances": q_distances,
            "pair_distances": pair_distances,
        },
        "evt013": {
            "overlaps": overlaps,
            "direct_local_inputs": list(direct_h),
            "derived_local_inputs": list(derived_h),
            "minimum_signed_margin": min(q * h for q, h in zip(Q, direct_h)),
        },
        "result": "PASS" if all(checks.values()) else "FAIL",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    result = execute()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.write:
        Path(__file__).with_name("results.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    return 1 if args.check and result["result"] != "PASS" else 0


if __name__ == "__main__":
    raise SystemExit(main())
