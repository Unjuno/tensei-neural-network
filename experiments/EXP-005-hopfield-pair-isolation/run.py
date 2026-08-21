from __future__ import annotations

import csv
import json
import platform
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

N = 100
P = 5
PATTERN_SEEDS = (1982, 1983, 1984)
CUES_PER_PAIR = 10
ORDER_RUNS_PER_CUE = 20
MAX_SWEEPS = 20


def generate_patterns(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.choice(np.array([-1, 1], dtype=np.int8), size=(P, N), replace=True)


def build_weights(patterns: np.ndarray) -> np.ndarray:
    weights = (patterns.T @ patterns).astype(np.float64) / N
    np.fill_diagonal(weights, 0.0)
    return weights


def hamming(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.count_nonzero(a != b))


def cue_seed(pattern_seed: int, a_idx: int, b_idx: int, cue_idx: int) -> int:
    return 4_000_000 + pattern_seed * 1000 + a_idx * 100 + b_idx * 10 + cue_idx


def order_seed(pattern_seed: int, a_idx: int, b_idx: int, cue_idx: int, run_idx: int) -> int:
    return (
        8_000_000
        + pattern_seed * 10_000
        + a_idx * 1_000
        + b_idx * 100
        + cue_idx * 20
        + run_idx
    )


def make_balanced_cue(a: np.ndarray, b: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    diff = np.flatnonzero(a != b)
    if diff.size == 0 or diff.size % 2 != 0:
        raise ValueError("pair is not valid for an exactly balanced binary cue")
    cue = a.copy()
    take_from_b = rng.choice(diff, size=diff.size // 2, replace=False)
    cue[take_from_b] = b[take_from_b]
    return cue


def recall(cue: np.ndarray, weights: np.ndarray, rng: np.random.Generator) -> tuple[np.ndarray, bool, int]:
    state = cue.copy()
    for sweep in range(1, MAX_SWEEPS + 1):
        changed = 0
        for i in rng.permutation(N):
            field = float(weights[i] @ state)
            if field > 0:
                new_value = 1
            elif field < 0:
                new_value = -1
            else:
                new_value = int(state[i])
            if new_value != state[i]:
                state[i] = new_value
                changed += 1
        if changed == 0:
            return state, True, sweep
    return state, False, MAX_SWEEPS


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    results_dir = base_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    cue_rows: list[dict[str, object]] = []
    valid_pair_count = 0
    distance_violations = 0

    # PASS/FAIL対象: EXP-004の200 cueをstored set全体のHamming距離で再解析する。
    for pattern_seed in PATTERN_SEEDS:
        patterns = generate_patterns(pattern_seed)
        for a_idx, b_idx in combinations(range(P), 2):
            a = patterns[a_idx]
            b = patterns[b_idx]
            pair_distance = hamming(a, b)
            if pair_distance == 0 or pair_distance % 2 != 0:
                continue
            valid_pair_count += 1

            for cue_idx in range(CUES_PER_PAIR):
                rng = np.random.default_rng(cue_seed(pattern_seed, a_idx, b_idx, cue_idx))
                cue = make_balanced_cue(a, b, rng)
                distances = np.count_nonzero(patterns != cue, axis=1).astype(int)
                d_a = int(distances[a_idx])
                d_b = int(distances[b_idx])
                if d_a != d_b or d_a != pair_distance // 2:
                    distance_violations += 1

                other_indices = [i for i in range(P) if i not in (a_idx, b_idx)]
                other_distances = [int(distances[i]) for i in other_indices]
                d_other_min = min(other_distances)
                margin = d_other_min - d_a
                if margin < 0:
                    classification = "THIRD_CLOSER"
                elif margin == 0:
                    classification = "THIRD_TIED"
                else:
                    classification = "PAIR_ISOLATED"

                cue_rows.append(
                    {
                        "pattern_seed": pattern_seed,
                        "a_idx": a_idx,
                        "b_idx": b_idx,
                        "pair_hamming": pair_distance,
                        "cue_idx": cue_idx,
                        "d_pair": d_a,
                        "d_other_min": d_other_min,
                        "margin": margin,
                        "classification": classification,
                        "other_distances": ";".join(str(x) for x in other_distances),
                    }
                )

    cue_count = len(cue_rows)
    counts = {
        key: sum(row["classification"] == key for row in cue_rows)
        for key in ("PAIR_ISOLATED", "THIRD_TIED", "THIRD_CLOSER")
    }

    valid_execution = cue_count == 200 and distance_violations == 0
    if not valid_execution:
        decision = "UNCERTAIN"
    elif counts["THIRD_TIED"] + counts["THIRD_CLOSER"] >= 1:
        decision = "PASS"
    else:
        decision = "FAIL"

    margins = [int(row["margin"]) for row in cue_rows]
    min_margin = min(margins) if margins else None
    max_margin = max(margins) if margins else None
    first_min = next((row for row in cue_rows if row["margin"] == min_margin), None)

    # 探索的解析: EXP-004の4000 runを同じseed規則で再生成しOTHER_STOREDを確認する。
    run_category_counts = {
        "A_EXACT": 0,
        "B_EXACT": 0,
        "OTHER_STORED": 0,
        "NONSTORED_CONVERGED": 0,
        "NONCONVERGED": 0,
    }
    other_stored_rows: list[dict[str, object]] = []

    for pattern_seed in PATTERN_SEEDS:
        patterns = generate_patterns(pattern_seed)
        weights = build_weights(patterns)
        for a_idx, b_idx in combinations(range(P), 2):
            a = patterns[a_idx]
            b = patterns[b_idx]
            pair_distance = hamming(a, b)
            if pair_distance == 0 or pair_distance % 2 != 0:
                continue
            for cue_idx in range(CUES_PER_PAIR):
                cue_rng = np.random.default_rng(cue_seed(pattern_seed, a_idx, b_idx, cue_idx))
                cue = make_balanced_cue(a, b, cue_rng)
                cue_distances = np.count_nonzero(patterns != cue, axis=1).astype(int)
                d_pair = int(cue_distances[a_idx])
                other_idx = [i for i in range(P) if i not in (a_idx, b_idx)]
                d_other_min = min(int(cue_distances[i]) for i in other_idx)

                for run_idx in range(ORDER_RUNS_PER_CUE):
                    rng = np.random.default_rng(order_seed(pattern_seed, a_idx, b_idx, cue_idx, run_idx))
                    final, converged, sweeps = recall(cue, weights, rng)
                    final_distances = np.count_nonzero(patterns != final, axis=1)
                    exact = np.flatnonzero(final_distances == 0)
                    if a_idx in exact:
                        category = "A_EXACT"
                    elif b_idx in exact:
                        category = "B_EXACT"
                    elif exact.size > 0:
                        category = "OTHER_STORED"
                        reached_idx = int(exact[0])
                        other_stored_rows.append(
                            {
                                "pattern_seed": pattern_seed,
                                "a_idx": a_idx,
                                "b_idx": b_idx,
                                "cue_idx": cue_idx,
                                "run_idx": run_idx,
                                "reached_idx": reached_idx,
                                "d_pair": d_pair,
                                "d_reached_other": int(cue_distances[reached_idx]),
                                "d_other_min": d_other_min,
                                "margin": d_other_min - d_pair,
                                "sweeps": sweeps,
                            }
                        )
                    elif converged:
                        category = "NONSTORED_CONVERGED"
                    else:
                        category = "NONCONVERGED"
                    run_category_counts[category] += 1

    with (results_dir / "cue_geometry.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(cue_rows[0].keys()))
        writer.writeheader()
        writer.writerows(cue_rows)

    summary = {
        "experiment_id": "EXP-005",
        "status": "executed",
        "decision": decision,
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "config": {
            "N": N,
            "P": P,
            "pattern_seeds": list(PATTERN_SEEDS),
            "cues_per_pair": CUES_PER_PAIR,
            "parent_experiment": "EXP-004",
        },
        "valid_pair_count": valid_pair_count,
        "cue_count": cue_count,
        "distance_violations": distance_violations,
        "classification_counts": counts,
        "min_margin": min_margin,
        "max_margin": max_margin,
        "first_min_margin_cue": first_min,
        "exploratory_exp004_run_category_counts": run_category_counts,
        "exploratory_other_stored": other_stored_rows,
        "note": (
            "PASS/FAIL concerns initial Hamming geometry only. "
            "PAIR_ISOLATED does not imply basin isolation."
        ),
    }

    (results_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
