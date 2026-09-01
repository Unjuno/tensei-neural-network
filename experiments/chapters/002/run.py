#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

A = (-1, 1, 1, 1, -1, -1)
B = (1, -1, 1, -1, -1, 1)
C = (-1, -1, -1, -1, 1, -1)
D = (1, 1, 1, 1, -1, 1)
Q46 = (1, -1, 1, 1, -1, -1)
ORDERS = {f"r{k+1}": tuple(list(range(1, 7))[k:] + list(range(1, 7))[:k]) for k in range(6)}
EXPECTED_EVT005 = ["A", "D", "B", "B", "D", "D"]
EXPECTED_EVT006 = {
    "q12": ["B", "B", "A", "A", "A", "A"],
    "q14": ["D", "A", "B", "B", "A", "A"],
    "q16": ["B", "A", "C", "A", "C", "B"],
    "q24": ["D", "D", "D", "D", "D", "D"],
    "q26": ["A", "B", "D", "D", "B", "B"],
    "q46": ["A", "D", "B", "B", "D", "D"],
}


def weights(patterns):
    n = len(patterns[0])
    return tuple(tuple(0 if i == j else sum(p[i] * p[j] for p in patterns) for j in range(n)) for i in range(n))


def update_one(state, one_based, w):
    s = list(state)
    i = one_based - 1
    h = sum(w[i][j] * s[j] for j in range(len(s)))
    if h > 0:
        s[i] = 1
    elif h < 0:
        s[i] = -1
    return tuple(s)


def run(state, order, w, max_sweeps=20):
    s = tuple(state)
    for sweep_no in range(1, max_sweeps + 1):
        before = s
        for i in order:
            s = update_one(s, i, w)
        if s == before:
            return s, sweep_no, True
    return s, max_sweeps, False


def canonical_label(state):
    labels = {
        A: "A", B: "B", C: "C",
        tuple(-x for x in A): "-A",
        tuple(-x for x in B): "-B",
        tuple(-x for x in C): "-C",
    }
    return labels.get(state, "OTHER")


def evt005_006_label(state):
    # EVT-005/006 used the provisional name D before EVT-007 reclassified D as -C.
    return "D" if state == D else canonical_label(state)


def balanced_cues():
    differing = [i for i, (a, b) in enumerate(zip(A, B)) if a != b]
    out = {}
    for choose_a in itertools.combinations(differing, 2):
        s = list(A)
        chosen = set(choose_a)
        for i in differing:
            s[i] = A[i] if i in chosen else B[i]
        out["q" + "".join(str(i + 1) for i in sorted(chosen))] = tuple(s)
    return out


def is_fixed(state, w):
    return all(update_one(state, i, w) == tuple(state) for i in range(1, 7))


def execute():
    w = weights([A, B, C])

    evt005 = []
    for order in ORDERS.values():
        final, sweeps, converged = run(Q46, order, w)
        evt005.append({"label": evt005_006_label(final), "final": final, "sweeps": sweeps, "converged": converged})

    cues = balanced_cues()
    evt006 = {}
    for qname, cue in sorted(cues.items()):
        evt006[qname] = []
        for order in ORDERS.values():
            final, sweeps, converged = run(cue, order, w)
            evt006[qname].append({"label": evt005_006_label(final), "final": final, "sweeps": sweeps, "converged": converged})

    states = list(itertools.product((-1, 1), repeat=6))
    fixed = [s for s in states if is_fixed(s, w)]
    final_counter = Counter()
    invariant = dependent = max_sweeps = nonconverged = 0
    for s in states:
        finals = []
        for order in ORDERS.values():
            final, sweeps, converged = run(s, order, w)
            finals.append(final)
            final_counter[canonical_label(final)] += 1
            max_sweeps = max(max_sweeps, sweeps)
            nonconverged += 0 if converged else 1
        if len(set(finals)) == 1:
            invariant += 1
        else:
            dependent += 1

    commutation_ok = all(
        update_one(tuple(-x for x in s), i, w) == tuple(-x for x in update_one(s, i, w))
        for s in states for i in range(1, 7)
    )

    evt005_labels = [x["label"] for x in evt005]
    evt006_labels = {k: [x["label"] for x in v] for k, v in evt006.items()}
    expected_fixed = {A, B, C, tuple(-x for x in A), tuple(-x for x in B), tuple(-x for x in C)}

    checks = {
        "evt005_order_results": evt005_labels == EXPECTED_EVT005,
        "evt005_aggregate": Counter(evt005_labels) == Counter({"A": 1, "B": 2, "D": 3}),
        "evt006_six_balanced_cues": len(cues) == 6,
        "evt006_36_trials": sum(len(v) for v in evt006.values()) == 36,
        "evt006_table": evt006_labels == EXPECTED_EVT006,
        "evt007_64_states": len(states) == 64,
        "evt007_384_trials": len(states) * len(ORDERS) == 384,
        "evt007_six_fixed_points": set(fixed) == expected_fixed,
        "evt007_D_equals_minus_C": D == tuple(-x for x in C),
        "evt007_final_set": set(final_counter) == {"A", "B", "C", "-A", "-B", "-C"},
        "evt007_final_counts": final_counter == Counter({"A": 62, "B": 66, "C": 64, "-A": 62, "-B": 66, "-C": 64}),
        "evt007_invariant_18": invariant == 18,
        "evt007_dependent_46": dependent == 46,
        "evt007_all_converged_by_2": nonconverged == 0 and max_sweeps <= 2,
        "evt008_sign_inversion_commutes": commutation_ok,
    }
    passed = all(checks.values())
    return {
        "chapter": "002",
        "verification": "EVT-005 through EVT-008 independent reproduction",
        "checks": checks,
        "evt005": {"labels": evt005_labels, "aggregate": dict(Counter(evt005_labels))},
        "evt006": {"table": evt006_labels, "aggregate": dict(Counter(x for row in evt006_labels.values() for x in row))},
        "evt007": {"fixed_points": [list(s) for s in fixed], "final_counts": dict(final_counter), "order_invariant_states": invariant, "order_dependent_states": dependent, "max_sweeps": max_sweeps, "nonconverged": nonconverged},
        "evt008": {"one_unit_sign_inversion_commutation": commutation_ok},
        "result": "PASS" if passed else "FAIL",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = execute()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.write:
        Path(__file__).with_name("results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if args.check and result["result"] != "PASS" else 0


if __name__ == "__main__":
    raise SystemExit(main())
