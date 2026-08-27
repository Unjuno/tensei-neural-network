#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

A = [-1, 1, 1, 1, -1, -1]
B = [1, -1, 1, -1, -1, 1]
C = [-1, -1, -1, -1, 1, -1]
CUE = [1, -1, 1, 1, -1, -1]
ORDERS = {
    "alpha": [1, 3, 6, 4, 5, 2],
    "beta": [4, 6, 1, 3, 5, 2],
}
EXPECTED = {"alpha": A, "beta": B}


def outer_sum(patterns: list[list[int]]) -> list[list[int]]:
    n = len(patterns[0])
    w = [[0 for _ in range(n)] for _ in range(n)]
    for p in patterns:
        for i in range(n):
            for j in range(n):
                if i != j:
                    w[i][j] += p[i] * p[j]
    return w


def sweep(state: list[int], order: list[int], weights: list[list[int]]) -> tuple[list[int], list[dict]]:
    s = state[:]
    trace: list[dict] = []
    for one_based in order:
        i = one_based - 1
        h = sum(weights[i][j] * s[j] for j in range(len(s)))
        old = s[i]
        if h > 0:
            s[i] = 1
        elif h < 0:
            s[i] = -1
        trace.append({"unit": one_based, "input_sum": h, "old": old, "new": s[i], "state": s[:]})
    return s, trace


def run_order(name: str, order: list[int], weights: list[list[int]]) -> dict:
    state = CUE[:]
    sweeps: list[list[dict]] = []
    converged = False
    for _ in range(16):
        new_state, trace = sweep(state, order, weights)
        sweeps.append(trace)
        if new_state == state:
            converged = True
            state = new_state
            break
        state = new_state
    return {
        "order_name": name,
        "order": order,
        "final_state": state,
        "converged": converged,
        "sweeps_until_no_change": len(sweeps),
        "trace": sweeps,
    }


def execute() -> dict:
    weights = outer_sum([A, B, C])
    runs = {name: run_order(name, order, weights) for name, order in ORDERS.items()}
    passed = all(
        runs[name]["converged"] and runs[name]["final_state"] == EXPECTED[name]
        for name in EXPECTED
    )
    return {
        "chapter": "001",
        "experiment": "EVT-004 minimal reproduction",
        "inputs": {"A": A, "B": B, "C": C, "cue": CUE},
        "weights": weights,
        "runs": runs,
        "expected": EXPECTED,
        "result": "PASS" if passed else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="exit non-zero unless the expected chapter result reproduces")
    parser.add_argument("--write", action="store_true", help="write results.json next to this script")
    args = parser.parse_args()

    result = execute()
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.write:
        out = Path(__file__).with_name("results.json")
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.check and result["result"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
