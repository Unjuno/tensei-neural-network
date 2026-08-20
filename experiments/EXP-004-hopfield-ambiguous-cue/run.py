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


def order_seed(
    pattern_seed: int,
    a_idx: int,
    b_idx: int,
    cue_idx: int,
    run_idx: int,
) -> int:
    return (
        8_000_000
        + pattern_seed * 10_000
        + a_idx * 1_000
        + b_idx * 100
        + cue_idx * 20
        + run_idx
    )


def make_balanced_cue(
    a: np.ndarray,
    b: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    diff = np.flatnonzero(a != b)
    if diff.size == 0 or diff.size % 2 != 0:
        raise ValueError("pair is not valid for an exactly balanced binary cue")

    cue = a.copy()
    take_from_b = rng.choice(diff, size=diff.size // 2, replace=False)
    cue[take_from_b] = b[take_from_b]
    return cue


def recall(
    cue: np.ndarray,
    weights: np.ndarray,
    rng: np.random.Generator,
) -> tuple[np.ndarray, bool, int]:
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


def classify(
    final: np.ndarray,
    patterns: np.ndarray,
    a_idx: int,
    b_idx: int,
    converged: bool,
) -> str:
    distances = np.count_nonzero(patterns != final, axis=1)
    exact = np.flatnonzero(distances == 0)

    if a_idx in exact:
        return "A_EXACT"
    if b_idx in exact:
        return "B_EXACT"
    if exact.size > 0:
        return "OTHER_STORED"
    if converged:
        return "NONSTORED_CONVERGED"
    return "NONCONVERGED"


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    results_dir = base_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    run_rows: list[dict[str, object]] = []
    cue_rows: list[dict[str, object]] = []
    valid_pair_count = 0
    distance_violations = 0

    for pattern_seed in PATTERN_SEEDS:
        patterns = generate_patterns(pattern_seed)
        weights = build_weights(patterns)

        for a_idx, b_idx in combinations(range(P), 2):
            a = patterns[a_idx]
            b = patterns[b_idx]
            pair_distance = hamming(a, b)
            if pair_distance == 0 or pair_distance % 2 != 0:
                continue

            valid_pair_count += 1

            for cue_idx in range(CUES_PER_PAIR):
                crng = np.random.default_rng(
                    cue_seed(pattern_seed, a_idx, b_idx, cue_idx)
                )
                cue = make_balanced_cue(a, b, crng)
                distance_a = hamming(cue, a)
                distance_b = hamming(cue, b)
                balanced = distance_a == distance_b == pair_distance // 2
                if not balanced:
                    distance_violations += 1

                counts = {
                    "A_EXACT": 0,
                    "B_EXACT": 0,
                    "OTHER_STORED": 0,
                    "NONSTORED_CONVERGED": 0,
                    "NONCONVERGED": 0,
                }

                for run_idx in range(ORDER_RUNS_PER_CUE):
                    seed = order_seed(
                        pattern_seed, a_idx, b_idx, cue_idx, run_idx
                    )
                    rng = np.random.default_rng(seed)
                    final, converged, sweeps = recall(cue, weights, rng)
                    category = classify(final, patterns, a_idx, b_idx, converged)
                    counts[category] += 1

                    run_rows.append(
                        {
                            "pattern_seed": pattern_seed,
                            "a_idx": a_idx,
                            "b_idx": b_idx,
                            "pair_hamming": pair_distance,
                            "cue_idx": cue_idx,
                            "cue_hamming_to_a": distance_a,
                            "cue_hamming_to_b": distance_b,
                            "run_idx": run_idx,
                            "order_seed": seed,
                            "category": category,
                            "converged": converged,
                            "sweeps": sweeps,
                        }
                    )

                bidirectional = counts["A_EXACT"] > 0 and counts["B_EXACT"] > 0
                cue_rows.append(
                    {
                        "pattern_seed": pattern_seed,
                        "a_idx": a_idx,
                        "b_idx": b_idx,
                        "pair_hamming": pair_distance,
                        "cue_idx": cue_idx,
                        "cue_hamming_to_a": distance_a,
                        "cue_hamming_to_b": distance_b,
                        "balanced": balanced,
                        **counts,
                        "BIDIRECTIONAL": bidirectional,
                    }
                )

    cue_count = len(cue_rows)
    run_count = len(run_rows)
    expected_run_count = cue_count * ORDER_RUNS_PER_CUE
    bidirectional_rows = [row for row in cue_rows if bool(row["BIDIRECTIONAL"])]

    valid_execution = (
        cue_count > 0
        and distance_violations == 0
        and run_count == expected_run_count
    )

    if not valid_execution:
        decision = "UNCERTAIN"
    elif bidirectional_rows:
        decision = "PASS"
    else:
        decision = "FAIL"

    total_category_counts = {
        category: sum(int(row[category]) for row in cue_rows)
        for category in (
            "A_EXACT",
            "B_EXACT",
            "OTHER_STORED",
            "NONSTORED_CONVERGED",
            "NONCONVERGED",
        )
    }

    with (results_dir / "runs.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(run_rows[0].keys()))
        writer.writeheader()
        writer.writerows(run_rows)

    with (results_dir / "cues.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(cue_rows[0].keys()))
        writer.writeheader()
        writer.writerows(cue_rows)

    summary = {
        "experiment_id": "EXP-004",
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
            "order_runs_per_cue": ORDER_RUNS_PER_CUE,
            "max_sweeps": MAX_SWEEPS,
            "update": "asynchronous shuffled order per sweep",
            "weight_rule": "Hebbian outer-product, diagonal zero",
        },
        "valid_pair_count": valid_pair_count,
        "cue_count": cue_count,
        "run_count": run_count,
        "expected_run_count": expected_run_count,
        "distance_violations": distance_violations,
        "bidirectional_cue_count": len(bidirectional_rows),
        "bidirectional_cue_rate": (
            len(bidirectional_rows) / cue_count if cue_count else None
        ),
        "category_counts": total_category_counts,
        "first_bidirectional_cue": bidirectional_rows[0] if bidirectional_rows else None,
        "note": (
            "Hamming-equidistant cues are not necessarily equidistant in energy or basin geometry. "
            "PASS is an existence claim for this finite setup only."
        ),
    }

    (results_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
