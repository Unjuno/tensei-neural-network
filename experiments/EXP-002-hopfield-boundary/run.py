from __future__ import annotations

import csv
import json
import platform
import sys
from collections import Counter
from pathlib import Path

import numpy as np

N = 100
P_VALUES = (5, 10, 15, 20)
NOISE_RATES = (0.10, 0.20, 0.30, 0.40)
PATTERN_SEEDS = (1982, 1983, 1984)
TRIALS_PER_CONDITION = 20
MAX_SWEEPS = 20

BASELINE_P = 5
BASELINE_NOISE = 0.10
BASELINE_THRESHOLD = 0.95
CHALLENGING_P = (15, 20)
CHALLENGING_NOISE = (0.30, 0.40)
CHALLENGING_THRESHOLD = 0.50


def generate_max_patterns(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.choice(
        np.array([-1, 1], dtype=np.int8),
        size=(max(P_VALUES), N),
        replace=True,
    )


def build_weights(patterns: np.ndarray) -> np.ndarray:
    weights = (patterns.T @ patterns).astype(np.float64) / N
    np.fill_diagonal(weights, 0.0)
    return weights


def trial_seed(
    seed_index: int,
    p_index: int,
    noise_index: int,
    trial_index: int,
) -> int:
    return (
        2_002_000
        + seed_index * 1_000_000
        + p_index * 100_000
        + noise_index * 1_000
        + trial_index
    )


def corrupt(pattern: np.ndarray, noise_rate: float, rng: np.random.Generator) -> np.ndarray:
    state = pattern.copy()
    flip_count = int(round(noise_rate * N))
    flip_indices = rng.choice(N, size=flip_count, replace=False)
    state[flip_indices] *= -1
    return state


def recall(
    initial_state: np.ndarray,
    weights: np.ndarray,
    rng: np.random.Generator,
) -> tuple[np.ndarray, bool, int]:
    state = initial_state.copy()

    for sweep in range(1, MAX_SWEEPS + 1):
        changed = 0
        for i in rng.permutation(N):
            local_field = float(weights[i] @ state)
            if local_field > 0:
                new_value = 1
            elif local_field < 0:
                new_value = -1
            else:
                new_value = int(state[i])

            if new_value != state[i]:
                state[i] = new_value
                changed += 1

        if changed == 0:
            return state, True, sweep

    return state, False, MAX_SWEEPS


def hamming_distance(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.count_nonzero(a != b))


def classify_final(
    final_state: np.ndarray,
    target_index: int,
    stored_patterns: np.ndarray,
    converged: bool,
) -> tuple[str, int, int]:
    target = stored_patterns[target_index]
    target_distance = hamming_distance(final_state, target)
    stored_distances = np.count_nonzero(stored_patterns != final_state, axis=1)
    nearest_stored_distance = int(stored_distances.min())

    exact_indices = np.flatnonzero(stored_distances == 0)
    if target_distance == 0:
        category = "TARGET_EXACT"
    elif exact_indices.size > 0:
        category = "WRONG_STORED"
    elif converged:
        category = "NONSTORED_CONVERGED"
    else:
        category = "NONCONVERGED"

    return category, target_distance, nearest_stored_distance


def aggregate_rows(rows: list[dict[str, object]]) -> dict[str, object]:
    total = len(rows)
    counts = Counter(str(row["final_category"]) for row in rows)
    seed_rates: dict[str, float] = {}
    for seed in PATTERN_SEEDS:
        seed_rows = [row for row in rows if int(row["pattern_seed"]) == seed]
        seed_exact = sum(row["final_category"] == "TARGET_EXACT" for row in seed_rows)
        seed_rates[str(seed)] = seed_exact / len(seed_rows)

    return {
        "trials": total,
        "exact_recall_count": counts["TARGET_EXACT"],
        "exact_recall_rate": counts["TARGET_EXACT"] / total,
        "wrong_stored_count": counts["WRONG_STORED"],
        "wrong_stored_rate": counts["WRONG_STORED"] / total,
        "nonstored_converged_count": counts["NONSTORED_CONVERGED"],
        "nonstored_converged_rate": counts["NONSTORED_CONVERGED"] / total,
        "nonconverged_count": counts["NONCONVERGED"],
        "nonconverged_rate": counts["NONCONVERGED"] / total,
        "mean_final_hamming_to_target": sum(
            int(row["final_hamming_to_target"]) for row in rows
        )
        / total,
        "mean_nearest_stored_hamming": sum(
            int(row["nearest_stored_hamming"]) for row in rows
        )
        / total,
        "mean_sweeps": sum(int(row["sweeps"]) for row in rows) / total,
        "seed_exact_recall_rates": seed_rates,
    }


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    results_dir = base_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    trial_rows: list[dict[str, object]] = []

    for seed_index, pattern_seed in enumerate(PATTERN_SEEDS):
        max_patterns = generate_max_patterns(pattern_seed)

        for p_index, p in enumerate(P_VALUES):
            patterns = max_patterns[:p]
            weights = build_weights(patterns)

            for noise_index, noise_rate in enumerate(NOISE_RATES):
                for trial_index in range(TRIALS_PER_CONDITION):
                    target_index = (trial_index + seed_index * 7) % p
                    target = patterns[target_index]
                    seed = trial_seed(seed_index, p_index, noise_index, trial_index)
                    rng = np.random.default_rng(seed)
                    initial = corrupt(target, noise_rate, rng)
                    final_state, converged, sweeps = recall(initial, weights, rng)
                    category, target_distance, nearest_distance = classify_final(
                        final_state,
                        target_index,
                        patterns,
                        converged,
                    )

                    trial_rows.append(
                        {
                            "pattern_seed": pattern_seed,
                            "P": p,
                            "load": p / N,
                            "noise_rate": noise_rate,
                            "trial_index": trial_index,
                            "target_index": target_index,
                            "trial_seed": seed,
                            "initial_hamming_to_target": hamming_distance(initial, target),
                            "final_hamming_to_target": target_distance,
                            "nearest_stored_hamming": nearest_distance,
                            "final_category": category,
                            "converged": converged,
                            "sweeps": sweeps,
                        }
                    )

    expected_trial_count = (
        len(PATTERN_SEEDS)
        * len(P_VALUES)
        * len(NOISE_RATES)
        * TRIALS_PER_CONDITION
    )

    trials_path = results_dir / "trials.csv"
    with trials_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(trial_rows[0].keys()))
        writer.writeheader()
        writer.writerows(trial_rows)

    grid_rows: list[dict[str, object]] = []
    grid_summary: dict[str, dict[str, object]] = {}
    for p in P_VALUES:
        for noise_rate in NOISE_RATES:
            rows = [
                row
                for row in trial_rows
                if int(row["P"]) == p and float(row["noise_rate"]) == noise_rate
            ]
            metrics = aggregate_rows(rows)
            key = f"P={p},noise={noise_rate:.2f}"
            grid_summary[key] = metrics
            grid_rows.append(
                {
                    "P": p,
                    "load": p / N,
                    "noise_rate": noise_rate,
                    **metrics,
                    "seed_exact_recall_rates": json.dumps(
                        metrics["seed_exact_recall_rates"],
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                }
            )

    grid_path = results_dir / "grid.csv"
    with grid_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(grid_rows[0].keys()))
        writer.writeheader()
        writer.writerows(grid_rows)

    baseline_key = f"P={BASELINE_P},noise={BASELINE_NOISE:.2f}"
    baseline_rate = float(grid_summary[baseline_key]["exact_recall_rate"])

    challenging_rates: dict[str, float] = {}
    for p in CHALLENGING_P:
        for noise_rate in CHALLENGING_NOISE:
            key = f"P={p},noise={noise_rate:.2f}"
            challenging_rates[key] = float(grid_summary[key]["exact_recall_rate"])

    lowest_challenging_key = min(challenging_rates, key=challenging_rates.get)
    lowest_challenging_rate = challenging_rates[lowest_challenging_key]

    baseline_pass = baseline_rate >= BASELINE_THRESHOLD
    challenging_pass = lowest_challenging_rate <= CHALLENGING_THRESHOLD
    valid_trial_count = len(trial_rows)

    decision = (
        "PASS"
        if valid_trial_count == expected_trial_count and baseline_pass and challenging_pass
        else "FAIL"
    )

    summary = {
        "experiment_id": "EXP-002",
        "status": "executed",
        "decision": decision,
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "config": {
            "N": N,
            "P_values": list(P_VALUES),
            "noise_rates": list(NOISE_RATES),
            "pattern_seeds": list(PATTERN_SEEDS),
            "trials_per_condition": TRIALS_PER_CONDITION,
            "max_sweeps": MAX_SWEEPS,
            "update": "asynchronous shuffled order per sweep",
            "weight_rule": "Hebbian outer-product, diagonal zero",
        },
        "expected_trial_count": expected_trial_count,
        "valid_trial_count": valid_trial_count,
        "decision_conditions": {
            "baseline": {
                "condition": baseline_key,
                "threshold": BASELINE_THRESHOLD,
                "observed_exact_recall_rate": baseline_rate,
                "passed": baseline_pass,
            },
            "challenging": {
                "conditions": challenging_rates,
                "threshold_at_or_below": CHALLENGING_THRESHOLD,
                "lowest_condition": lowest_challenging_key,
                "lowest_exact_recall_rate": lowest_challenging_rate,
                "passed": challenging_pass,
            },
        },
        "grid": grid_summary,
        "note": (
            "NONSTORED_CONVERGED is an observational category and is not automatically "
            "identified with a theoretical spurious attractor."
        ),
    }

    (results_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
