#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

A = (-1, 1, 1, 1, -1, -1)
B = (1, -1, 1, -1, -1, 1)
C = (-1, -1, -1, -1, 1, -1)

M1 = (1,1,1,1,-1,-1,-1,-1, 1,1,-1,1,-1,1,-1,-1)
M2 = (1,1,1,1,-1,-1,-1,-1, -1,-1,1,-1,1,-1,1,1)
M3 = (1,1,-1,-1,1,1,-1,-1, 1,-1,-1,1,1,-1,-1,1)
Q  = (1,1,1,1,-1,-1,-1,-1, 1,-1,-1,1,1,-1,-1,1)


def weights(patterns):
    n = len(patterns[0])
    return tuple(
        tuple(0 if i == j else sum(p[i] * p[j] for p in patterns) for j in range(n))
        for i in range(n)
    )


def local_inputs(state, w):
    return tuple(sum(w[i][j] * state[j] for j in range(len(state))) for i in range(len(state)))


def fixed_with_zero_hold(state, w):
    h = local_inputs(state, w)
    for s_i, h_i in zip(state, h):
        if h_i > 0 and s_i != 1:
            return False
        if h_i < 0 and s_i != -1:
            return False
        # h_i == 0 retains the current value
    return True


def neg(state):
    return tuple(-x for x in state)


def execute():
    # EVT-009 side: exhaust the fixed points of the 6-unit toy.
    w6 = weights((A, B, C))
    states6 = tuple(itertools.product((-1, 1), repeat=6))
    fixed6 = tuple(s for s in states6 if fixed_with_zero_hold(s, w6))
    expected6 = {A, B, C, neg(A), neg(B), neg(C)}
    residual6 = set(fixed6) - expected6

    # EVT-011 side: reproduce the published 16-neurone candidate.
    w16 = weights((M1, M2, M3))
    hq = local_inputs(Q, w16)
    products = tuple(q_i * h_i for q_i, h_i in zip(Q, hq))
    source_class = {M1, M2, M3, neg(M1), neg(M2), neg(M3)}
    q_is_residual = Q not in source_class
    q_has_no_ties = all(h != 0 for h in hq)
    q_sign_stable = all(p > 0 for p in products)

    checks = {
        "evt009_exactly_64_states": len(states6) == 64,
        "evt009_fixed_points_match": set(fixed6) == expected6,
        "evt009_residual_empty": residual6 == set(),
        "evt011_local_inputs_match": hq == (21,21,5,5,-5,-5,-21,-21,5,-5,-5,5,5,-5,-5,5),
        "evt011_no_zero_local_input": q_has_no_ties,
        "evt011_all_signs_stable": q_sign_stable,
        "evt011_not_stored_or_negation": q_is_residual,
    }

    result = "PASS" if all(checks.values()) else "FAIL"
    return {
        "chapter": "003",
        "verification": "EVT-009 residual classification and EVT-011 published 16-neurone reproduction",
        "checks": checks,
        "evt009": {
            "fixed_points": [list(s) for s in fixed6],
            "residual_count": len(residual6),
        },
        "evt011": {
            "local_inputs": list(hq),
            "signed_margins": list(products),
            "minimum_signed_margin": min(products),
            "zero_local_inputs": sum(h == 0 for h in hq),
            "stored_or_negation_match": not q_is_residual,
        },
        "result": result,
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
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    return 1 if args.check and result["result"] != "PASS" else 0


if __name__ == "__main__":
    raise SystemExit(main())
